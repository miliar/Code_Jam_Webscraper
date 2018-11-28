#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

ifstream in("perm.in");
ofstream out("perm.out");

int main() {
  int n;
  in >> n;

  for (int casenum = 1; casenum <= n; casenum++) {
    int k,c;
    in >> k;
    string s,z;
    in >> s;
    
    int bestsize = s.size();
    vector<int> p(k);
    for (int i=0; i<k; i++) {
      p[i] = i;
    }    

    do {
      z = "";
      for (int i=0; i<s.size()/k; i++) {
	for (int j=0; j<k; j++) {
	  z += s[i*k+p[j]];
	}
      }

      int c=1;
      for (int i=1; i<z.size(); i++) {
	if (z[i] != z[i-1]) {
	  c++;
	}
      }
      if (c < bestsize) {
	bestsize = c;
      }
      
    } while (next_permutation(p.begin(),p.end()));
    
    out << "Case #" << casenum << ": " << bestsize << endl;   
  }
  return 0;
}
