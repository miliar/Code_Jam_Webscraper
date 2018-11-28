#include <cctype>
using std::tolower;
#include <string>
using std::string;
#include <iostream>
using std::cout;
using std::cerr;
using std::endl;
using std::fixed;
using std::showpoint;
using std::noshowpoint;
#include <iomanip>
using std::setprecision;
#include <fstream>
using std::ifstream;
using std::ofstream;
#include <cmath>
using std::sqrt;
using std::atan;
using std::sin;
#include <vector>
using std::vector;
#include <algorithm>
using std::sort;

#include "utilities.hpp"
using klb::PI;
using klb::Pair;

#define DEBUG 0

inline double getX(const double&, const double&);
inline double chordArea(const double&, const Pair&, const Pair&);

int main (int argc, char** argv) {
  
  string infilename, outfilename;
  if (argc > 1) {
    if (tolower(argv[1][0]) == 'l') {
      infilename = "C-large.in";
      outfilename = "C-large.out";
    }
    else if (tolower(argv[1][0]) == 's') {
      infilename = "C-small.in";
      outfilename = "C-small.out";
    }
    else if (tolower(argv[1][0]) == 't') {
      infilename = "C-test.in";
      outfilename = "C-test.out";
    }
  }
  if (infilename.empty()) {
    cerr << "You forgot to specify the size! Try \"" << argv[0]
        << " large\" or \"" << argv[0] << " small\"\n";
    return 1;
  }
  
  ifstream infile(infilename.c_str());
  if (!infile) {
    cerr << "Failed to open " << infilename << "!\n";
    return 1;
  }

  ofstream outfile(outfilename.c_str());
  if (!outfile) {
    cerr << "Failed to open " << outfilename << "!\n";
    return 1;
  }

  int numEntries;
  infile >> numEntries;

  outfile << fixed << setprecision(6);

  double flyRad, outerRad, frameWidth, stringRad, gapWidth, p;
  for (int i=1; i<=numEntries; i++) {
#if DEBUG
    cout << noshowpoint << "Processing case " << i << ":" << endl;
#endif
    infile >> flyRad >> outerRad >> frameWidth >> stringRad >> gapWidth;

    gapWidth -= 2*flyRad;
    if (gapWidth <= 0.0) {
      p=1.0;
#if DEBUG
      cout << "Fly can't get away!\n";
#endif
    }
    else {
      stringRad += flyRad;
      frameWidth += flyRad;
      double innerRad = outerRad - frameWidth;

      Pair low, high, lowCorner;
      low.y = lowCorner.y = stringRad;
      low.x = lowCorner.x = getX(innerRad, low.y);
      high.y = low.y + gapWidth;
      high.x = getX(innerRad, high.y);

#if DEBUG
      cout << fixed << showpoint;
      long lastNumFullSquares=0;
#endif
      vector<double> openAreas;
      long numFullSquares=0;
      while (high.y < lowCorner.x) {
#if DEBUG
        cout << "y={" << low.y << "," << high.y << "}\n";
#endif
        double xAvail = high.x - stringRad;

        // whole squares
        while (xAvail > gapWidth) {
          numFullSquares++;
          xAvail -= gapWidth + 2*stringRad;
        }
#if DEBUG > 1
        cout << "\t" << numFullSquares-lastNumFullSquares
             << " whole square(s)...\n";
        lastNumFullSquares = numFullSquares;
#endif

        if (xAvail > 0) {
          // Cases 1 and 2
          openAreas.push_back( xAvail*gapWidth );
          Pair bottom;
          bottom.x = high.x - xAvail + gapWidth;
          if (low.x < bottom.x) {
            // Case 1
#if DEBUG > 1
            cout << "\tCase 1...\n";
#endif
            openAreas.push_back( (low.x-high.x)*gapWidth/2.0 );
            openAreas.push_back( chordArea(innerRad, low, high) );
          }
          else {
            // Case 2
#if DEBUG > 1
            cout << "\tCase 2...\n";
#endif
            bottom.y = getX(innerRad, bottom.x);
            openAreas.push_back( (bottom.x-high.x)*(bottom.y-low.y) );
            openAreas.push_back( (bottom.x-high.x)*(high.y-bottom.y)/2.0 );
            openAreas.push_back( chordArea(innerRad, bottom, high) );
          }
          xAvail -= gapWidth + 2*stringRad;
        }
        // Cases 3 and 4
        Pair left, right;
        left.x = high.x - xAvail;
        left.y = getX(innerRad, left.x);
        right.x = left.x + gapWidth;
        right.y = getX(innerRad, right.x);
        while (right.y > low.y) {
          // Case 4
#if DEBUG > 1
          cout << "\tCase 4...\n";
#endif
          openAreas.push_back( gapWidth*(right.y-low.y) );
          openAreas.push_back( gapWidth*(left.y-right.y)/2.0 );
          openAreas.push_back( chordArea(innerRad, right, left) );

          left.x = right.x + 2*stringRad;
          left.y = getX(innerRad, left.x);
          right.x = left.x + gapWidth;
          right.y = getX(innerRad, right.x);
        }

        if (left.y > low.y) {
          // Case 3
#if DEBUG > 1
          cout << "\tCase 3...\n";
#endif
          openAreas.push_back( (low.x-left.x)*(left.y-low.y)/2.0 );
          openAreas.push_back( chordArea(innerRad, low, left) );
        }

        low.y = high.y + 2*stringRad;
        low.x = getX(innerRad, low.y);
        high.y = low.y + gapWidth;
        high.x = getX(innerRad, high.y);
      }
      // fractional-height row
      if (low.y < lowCorner.x) {
#if DEBUG
        cout << "y={" << low.y << "," << high.y << "}\n";
#endif
        Pair left, right;
        left.x = lowCorner.y;
        left.y = getX(innerRad, left.x);
        right.x = left.x + gapWidth;
        right.y = getX(innerRad, right.x);
        while (right.y > low.y) {
          // Case 4
#if DEBUG
          cout << "\tx={" << left.x << "," << right.x << "}\n";
#if DEBUG > 1
          cout << "\t\tCase 4...\n";
#endif
#endif
          openAreas.push_back( gapWidth*(right.y-low.y) );
          openAreas.push_back( gapWidth*(left.y-right.y)/2.0 );
          openAreas.push_back( chordArea(innerRad, right, left) );

          left.x = right.x + 2*stringRad;
          left.y = getX(innerRad, left.x);
          right.x = left.x + gapWidth;
          right.y = getX(innerRad, right.x);
        }

        if (left.y > low.y) {
          // Case 3
#if DEBUG
          cout << "\tx={" << left.x << "," << right.x << "}\n";
#if DEBUG > 1
          cout << "\t\tCase 3...\n";
#endif
#endif
          openAreas.push_back( (low.x-left.x)*(left.y-low.y)/2.0 );
          openAreas.push_back( chordArea(innerRad, low, left) );
        }
      }
      sort(openAreas.begin(), openAreas.end());
      double totalArea=0;
      for (vector<double>::iterator j=openAreas.begin(); j!=openAreas.end(); j++)
        totalArea += (*j);
#if DEBUG
      cout << "totalArea = " << totalArea << " + ";
#endif
      totalArea += numFullSquares*gapWidth*gapWidth;
#if DEBUG
      cout << numFullSquares*gapWidth*gapWidth << " = " << totalArea << endl;
#endif

      p = 1.0 - totalArea/(PI*outerRad*outerRad/4);
#if DEBUG
      cout << "racquetArea = " << PI*outerRad*outerRad/4 << endl;
#endif
    }
    outfile << "Case #" << i << ": " << showpoint << p << noshowpoint << endl;
  }  
  
  infile.close();
  outfile.close();
  
  return 0;
}

inline double getX(const double &r, const double &y) {
  return sqrt(r*r - y*y);
}

inline double chordArea(const double &r, const Pair &l, const Pair &h) {
  double theta = atan(h.y/h.x) - atan(l.y/l.x);
  return (theta - sin(theta))*r*r/2.0;
}

