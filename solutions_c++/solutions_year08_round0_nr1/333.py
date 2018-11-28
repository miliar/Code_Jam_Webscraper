#include <cctype>
using std::tolower;
#include <string>
using std::string;
#include <iostream>
using std::cout;
using std::cerr;
using std::endl;
#include <fstream>
using std::ifstream;
using std::ofstream;
#include <vector>
using std::vector;

#define DEBUG 0

struct SearchEngineT {
  string name;
  int inQuery;
  SearchEngineT() {
    inQuery=false;
  }
};

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

  int numSE, numQ;
  for (int i=1; i<=numEntries; i++) {
    infile >> numSE; infile.ignore();
    vector<SearchEngineT> se(numSE);
    for (vector<SearchEngineT>::iterator j=se.begin(); j!=se.end(); j++)
      getline(infile, (*j).name);
    
    infile >> numQ; infile.ignore();
    int numSwitches=0;
    string nextQ;
    int numQueried=0;
    int j=0;
    while (j<numQ) {
      while (numQueried < numSE-1 && j<numQ) {
        getline(infile, nextQ);
        for (vector<SearchEngineT>::iterator k=se.begin(); k!=se.end(); k++) {
          if (nextQ == (*k).name) {
            if (!(*k).inQuery) {
              (*k).inQuery=true;
              numQueried++;
            }              
          }
        }
        j++;
      }

      if (j<numQ) {
        vector<SearchEngineT>::iterator notQueried=se.begin();
        while ((*notQueried).inQuery)
          notQueried++;
        while (nextQ != (*notQueried).name && j<numQ) {
          getline(infile, nextQ);
          j++;
        }

        if (j<numQ) {
          numSwitches++;
          for (vector<SearchEngineT>::iterator k=se.begin(); k!=se.end(); k++) {
            (*k).inQuery=false;
          }
          (*notQueried).inQuery=true;
          numQueried=1;
        }
        else if (nextQ == (*notQueried).name)
          numSwitches++;
      }
    }    
    outfile << "Case #" << i << ": " << numSwitches << endl;
  }
  
  infile.close();
  outfile.close();
  
  return 0;
}
