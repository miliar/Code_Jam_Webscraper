#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

ifstream in("prod.in");
ofstream out("prod.out");

int main() {
  int T;
  in >> T;

  for (int casenum = 1; casenum <= T; casenum++) {
    int n;
    in >> n;
    vector<int> v(n),w(n),x(n);
    for (int i=0; i<n; i++) {
      in >> v[i];
      x[i] = i;
    }
    for (int i=0; i<n; i++) {
      in >> w[i];
    }
    int bestsum = 2000000000,cursum;
    do {
      cursum = 0;
      for (int i=0; i<n; i++) {
	cursum += v[i]*w[x[i]];
      }
      if (cursum < bestsum) {
	bestsum = cursum;
      }      
    } while (next_permutation(x.begin(),x.end()));
	     
    out << "Case #" << casenum << ": " << bestsum << endl;
  }
  return 0;
}
