#include <cctype>
using std::tolower;
#include <string>
using std::string;
#include <iostream>
using std::cout;
using std::cerr;
using std::endl;
using std::fixed;
using std::noshowpoint;
#include <fstream>
using std::ifstream;
using std::ofstream;
#include <vector>
using std::vector;
#include <algorithm>
using std::sort;

#define DEBUG 0

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

  outfile << fixed << noshowpoint;
  
  int numEntries;
  infile >> numEntries;

  int numComp;
  for (int i=1; i<=numEntries; i++) {
    infile >> numComp;
    vector<int> a(numComp), b(numComp);
    for (vector<int>::iterator j=a.begin(); j!=a.end(); j++)
      infile >> *j;
    for (vector<int>::iterator j=b.begin(); j!=b.end(); j++)
      infile >> *j;
    sort(a.begin(),a.end());
    sort(b.begin(),b.end());

    long product=0;
    vector<int>::reverse_iterator k=b.rbegin();
    for (vector<int>::iterator j=a.begin(); j!=a.end(); j++) {
      product += (*j)*(*k);
      k++;
    }
    
    outfile << "Case #" << i << ": " << product << endl;
  }

  infile.close();
  outfile.close();

  
  return 0;
}
