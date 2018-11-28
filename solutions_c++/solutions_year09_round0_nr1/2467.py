#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <math.h>
#include <algorithm>
#define VLENGTH 15 // maximum L

using namespace std;

int main(int argc, char** argv) {
  if(argc!=2) {
    cout << "Usage: " << argv[0] << " DATAFILE" << endl;
    exit(1);
  }
  
  ifstream infile(argv[1]);
  if(!infile.good()) {
    cout << "Error: could not open " << argv[1] << endl;
    exit(2);
  }
  
  int L;
  int D;
  int N; // total cases
  string aForward, aBackward;
  infile >> L >> D >> N;
  string aStr;
  vector<string> vStr;

  for(int iD=0; iD<D; iD++) {
    infile >> aStr;
    vStr.push_back(aStr);
  }
  
  for(int iN=0; iN<N; iN++){
    vector<string> vL[VLENGTH];
    infile >> aStr;
    int index=0;
    int isize=0;
    int iL=0;
    while(isize<aStr.length()) {
      if(aStr.substr(isize,1)=="("){
	isize++;
	while(aStr.substr(isize,1)!=")") {
	  vL[iL].push_back(aStr.substr(isize,1));
	  //	  cout << iL << " " << vL[iL].back() << endl;
	  isize++;
	}
	iL++;
      }else if (aStr.substr(isize,1)==")"){
	isize++;
      } else {
	vL[iL].push_back(aStr.substr(isize,1));
	//	cout << iL << " " << vL[iL].back() << endl;
	iL++;
	isize++;
      }
    }
    vector<string>tmpV;
    tmpV.resize(vStr.size());
    copy(vStr.begin(), vStr.end(), tmpV.begin());

    //    cout << iL << endl;
    for(int j=0; j< iL; j++) {
      for(int i=tmpV.size()-1; i>=0; i--) {
	if(find(vL[j].begin(), vL[j].end(),tmpV.at(i).substr(j,1))==vL[j].end()) tmpV.erase(tmpV.begin()+i);
      }
    }

    cout << "Case #" << iN+1 << ": " << tmpV.size() << endl;
    
  }
  
  return 0;
}
