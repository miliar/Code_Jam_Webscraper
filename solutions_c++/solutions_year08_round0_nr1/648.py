#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

ifstream in("univ.in");
ofstream out("univ.out");

int main() {
  int N,S,Q;
  in >> N;
  for (int casenum=1; casenum<=N; casenum++) {
    in >> S;
    vector<string> engines(S);
    getline(in, engines[0]);
    for (int i=0; i<S; i++) {
      getline(in, engines[i]);
    }
    vector<int> dp(S,0), dpnext;
    in >> Q;
    string q;
    getline(in,q);
    for (int i=0; i<Q; i++) {
      getline(in,q);
      int eng = -1;
      for (int j=0; j<S; j++) {
	if (q == engines[j]) {
	  eng = j;
	}
      }
      if (i==0) {
	dpnext.clear();
	dpnext.resize(S,0);
	if (eng != -1) {
	  dpnext[eng] = 1000000;
	}
      } else {
	dpnext.resize(S);
	for (int j=0; j<S; j++) {
	  if (j == eng) {
	    dpnext[j] = 1000000;
	  } else {
	    dpnext[j] = dp[j];
	    for (int k=0; k<S; k++) {
	      if (dp[k] + 1 < dpnext[j]) {
		dpnext[j] = dp[k] + 1;
	      }
	    }
	  }
	}
      }
      dp = dpnext;
    }
    int bestswitch = 1000000;
    for (int i=0; i<S; i++) {
      if (dp[i] < bestswitch) {
	bestswitch = dp[i];
      }
    }
    out << "Case #" << casenum << ": " << bestswitch << endl;
  }
  return 0;
}
