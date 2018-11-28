#include <iostream>
#include <sstream>
#include <unordered_map>
#include <algorithm>
#include <iterator>
#include <functional>
#include <vector>
#include <string>
#include <map>

using namespace std;


int main() {
 
  int nr = 0;
  int maxNr;
  cin >> maxNr;
  cin.ignore(10,'\n');
  cerr <<  "maxNr= " << maxNr << endl;

  string line;
  getline(cin,line);

  while(nr < maxNr && !cin.eof() && !line.empty()) { 
    stringstream sin(line,stringstream::in);
    int A,B;
    sin >> A >> B;

    map<string,vector<string> > numbermap;
    
    for(int i = A; i <= B; ++i) {
      stringstream sn;
      sn << i;
      string s = sn.str();
      string ss = s;
      sort(ss.begin(),ss.end());
      numbermap[ss].push_back(s);
    }

    int pairs = 0;
    for_each(numbermap.begin(),numbermap.end(),[&pairs](pair<string,vector<string> > const &val) {
	vector<string> vn = val.second;
	for(int i = 0; i < vn.size()-1; ++i) {
	  for(int j = i+1; j<vn.size(); ++j) {
	    // check if is a recycled pair
	    string n = vn[i];
	    string m = vn[j];
	    string cn = n;
	    
	    // rotate m to simulate char movement
	    for(int k = 0; k < n.size()-1; ++k) {
	      rotate(n.begin(),n.end()-1,n.end());
	      if(m==n) {
		pairs++;
		//cerr << cn << ", " << m << endl;
		break;
	      }
	    }
	    
	  }
	}
      });
    

    // output
    cout << "Case #" << ++nr << ": " << pairs << endl;
    // read next line
    getline(cin,line);
  }
  

  if(nr != maxNr) {
    cerr << "unexpected end of stream..." << nr << " " << maxNr << endl;
  }

  return 0;
}

