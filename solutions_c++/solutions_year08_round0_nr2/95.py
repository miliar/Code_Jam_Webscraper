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
// }}}

/////////////////// PRE-WRITTEN CODE FOLLOWS, LOOK DOWN FOR THE SOLUTION ////////////////////////////////

// pre-written code {{{
/*
  compute the size of a maximum matching in the bipartite graph G
	G[i][j] = (are part1[i] and part2[j] connected?)
*/
int BIPARTITE_MATCHING_SIZE(const vector< vector<int> > G) {
  int A = G.size(), B = G[0].size();
  if (A==0 || B==0) return 0;
  
  vector<int> matched(A,0), match(A,0);

  for (int j=0; j<B; j++) {
    vector<int> seen(A,0), from(A,-1);
    
    queue<int> Q;
    for (int i=0; i<A; i++) if (G[i][j]) { Q.push(i); seen[i]=1; }
    int found = 0;
    
    while (!Q.empty()) {
      int where = Q.front(); Q.pop();
      if (!matched[where]) {
        found = 1;
        // update
        matched[where]=1;
        while (1) {
          if (from[where]==-1) { match[where]=j; break; }
          match[where] = match[ from[where] ];
          where = from[where];
        }
        break; // stop looking (this is necessary)!
      }
      
      int neighbor = match[where];
      for (int i=0; i<A; i++) if (G[i][neighbor]) if (!seen[i]) { Q.push(i); seen[i]=1; from[i]=where; }
    }
  }
  int res = 0;
  for (int i=0; i<A; i++) res += matched[i];
  return res;
}
// }}}

/////////////////// CODE WRITTEN DURING THE COMPETITION FOLLOWS ////////////////////////////////

int parsetime(string time) { int h,m; sscanf(time.c_str(),"%d:%d",&h,&m); return 60*h+m; }

int main() {
  int N;
  cin >> N;
  for (int n=1; n<=N; n++) {
    int T, NA, NB;
    cin >> T >> NA >> NB;
    vector< vector<int> > A(NA,2), B(NB,2);
    string t1,t2;
    for (int i=0; i<NA; i++) { cin >> t1 >> t2; A[i][0]=parsetime(t1); A[i][1]=parsetime(t2); }
    for (int i=0; i<NB; i++) { cin >> t1 >> t2; B[i][0]=parsetime(t1); B[i][1]=parsetime(t2); }
    int resA, resB;
    {
      vector< vector<int> > G(NB,NA);
      for (int i=0; i<NB; i++)
        for (int j=0; j<NA; j++)
          if (B[i][1] + T <= A[j][0])
            G[i][j] = 1;
      resA = NA - BIPARTITE_MATCHING_SIZE(G);
    }
    {
      vector< vector<int> > G(NA,NB);
      for (int i=0; i<NA; i++)
        for (int j=0; j<NB; j++)
          if (A[i][1] + T <= B[j][0])
            G[i][j] = 1;
      resB = NB - BIPARTITE_MATCHING_SIZE(G);
    }
    cout << "Case #" << n << ": " << resA << " " << resB << endl;
  }
  return 0;
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
