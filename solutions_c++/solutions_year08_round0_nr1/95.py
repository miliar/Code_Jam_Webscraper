// another fine solution by misof
// #includes {{{
#include <algorithm>
#include <numeric>

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cassert>

#include <cmath>
#include <complex>
using namespace std;

int main() {
  int N;
  string line;
  getline(cin,line); stringstream(line) >> N;
  for (int n=1; n<=N; n++) {
    int S,Q;
    getline(cin,line); stringstream(line) >> S;
    map<string,int> ID;
    for (int s=0; s<S; s++) { getline(cin,line); ID[line]=s; }
    
    getline(cin,line); stringstream(line) >> Q;
    vector<int> query(Q);
    for (int q=0; q<Q; q++) { getline(cin,line); query[q]=ID[line]; }

    vector< vector<int> > best(Q+1, vector<int>(S,987654321));
    for (int s=0; s<S; s++) best[0][s] = 0;
    for (int q=0; q<Q; q++) {
      for (int s=0; s<S; s++) {
        if (query[q]==s) continue;
        best[q+1][s] = min( best[q+1][s], best[q][s] );
        for (int s2=0; s2<S; s2++)
          best[q+1][s] = min( best[q+1][s], best[q][s2]+1 );
      }
    }
    int res = 987654321;
    for (int s=0; s<S; s++) res = min(res, best[Q][s] );
    cout << "Case #" << n << ": " << res << endl;
  }
  return 0;
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
