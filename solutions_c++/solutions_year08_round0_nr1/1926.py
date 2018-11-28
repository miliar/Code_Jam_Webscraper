#include <iostream>
#include <string>
#include <vector>
#include <sstream>
using namespace std;

int main() {
  int c =1;
  string line;
  getline(cin, line);
  stringstream t(line);
  int ncases;
  t >> ncases;
  while(ncases--) {
    getline(cin,line);
    stringstream t2(line);
    int ne;
    t2 >> ne;
    vector<string> e;
    while(ne--) {
      getline(cin,line);
      e.push_back(line);
    }
    getline(cin,line);
    stringstream t3(line);
    int nq;
    t3 >> nq;
    vector<string> q;
    while(nq--) {
      getline(cin,line);
      q.push_back(line);
    }

    int n=0;
    int p=0;
    for(;;) {
      int max=-1;
      int t = 0;
      for(int j=0;j<e.size();j++) {
	for(int k=p;k<q.size();k++) {
	  if(q[k]==e[j]) {
	    t++;
	    if(k>max) max=k;
	    break;
	  }
	}
      }
      if(t<e.size()) break;
      n++;
      p = max;
    }
    cout << "Case #" << c++ << ": " << n << endl;
  }
  return 0;
}
