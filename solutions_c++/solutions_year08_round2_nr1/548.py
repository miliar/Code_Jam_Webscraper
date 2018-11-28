#include <cctype>
#include <string>
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

#define DEBUG 0

typedef long long MyT;
typedef struct {
  MyT x;
  MyT y;      
} myXYpair;
  

int main (int argc, char** argv) {

  string infilename, outfilename;
  if (argc > 1) {
    if (tolower(argv[1][0]) == 'l') {
      infilename = "A-large.in";
      outfilename = "A-large.out";
    }
    else if (tolower(argv[1][0]) == 's') {
      infilename = "A-small.in";
      outfilename = "A-small.out";
    }
    else if (tolower(argv[1][0]) == 't') {
      infilename = "A-test.in";
      outfilename = "A-test.out";
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

  MyT numTrees, xMult, xAdd, yMult, yAdd, xBase, yBase, modFactor;
  for (int i=1; i<=numEntries; i++) {
    infile >> numTrees >> xMult >> xAdd >> yMult >> yAdd
           >> xBase >> yBase >> modFactor;
    vector<myXYpair> trees(numTrees);
    trees[0].x = xBase; trees[0].y = yBase;
    for (vector<myXYpair>::iterator j=trees.begin(); j+1 != trees.end(); j++) {
      (*(j+1)).x = ((*j).x*xMult + xAdd) % modFactor;
      (*(j+1)).y = ((*j).y*yMult + yAdd) % modFactor;
    }

    MyT numTriangles = 0;
    vector<myXYpair>::iterator p1, p2, p3;
    for (p1=trees.begin(); p1+2 != trees.end(); p1++) {
      for (p2=p1+1; p2+1 != trees.end(); p2++) {
        for (p3=p2+1; p3 != trees.end(); p3++) {
          if ((((*p1).x+(*p2).x+(*p3).x)%3) == 0 &&
              (((*p1).y+(*p2).y+(*p3).y)%3) == 0)
            numTriangles++;
        }
      }
    }

    outfile << "Case #" << i << ": " << numTriangles << endl;
  }

  infile.close();
  outfile.close();

  return 0;
}
