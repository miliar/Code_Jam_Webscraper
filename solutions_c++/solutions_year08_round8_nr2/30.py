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
#include <cstring>

#include <cmath>
#include <complex>
using namespace std;
// }}}

/////////////////// PRE-WRITTEN CODE FOLLOWS, LOOK DOWN FOR THE SOLUTION ////////////////////////////////

// pre-written code {{{
#define REP(i,n) for(int i=0;i<(int)(n);++i)
// }}}

/////////////////// CODE WRITTEN DURING THE COMPETITION FOLLOWS ////////////////////////////////

int T; string Tline;

int F[500],LO[500],HI[500];
int C, N;

class interval {
  public: 
    int lo, hi;
    interval(int lo, int hi) : lo(lo), hi(hi) { }
};

bool operator< (const interval &A, const interval &B) {
  if (A.hi != B.hi) return A.hi < B.hi;
  return false;
}

bool firstcmp (const interval &A, const interval &B) {
  if (A.lo != B.lo) return A.lo < B.lo;
  return false;
}


int doit(int x, int y, int z) {
  vector<interval> cand;
  for (int i=0; i<N; i++) if (F[i]==x || F[i]==y || F[i]==z) cand.push_back( interval( LO[i], HI[i] ) );
  cand.push_back(interval(10047,10047));
  sort( cand.begin(), cand.end(), firstcmp );
  //printf("colors %d %d %d : ",x,y,z);
  //REP(i,N) printf("[%d %d] ",cand[i].lo,cand[i].hi); printf("\n");
  priority_queue<interval> Q;
  int kde = 1, k = 0;
  int used = 0;
  while (true) {
    while (cand[k].lo <= kde) { 
      Q.push( cand[k] );
      //printf(" vlkadam %d %d\n",cand[k].lo,cand[k].hi);
      k++;
    }
    if (Q.empty()) return 999;
    interval pouzi = Q.top(); Q.pop();
    //printf("pouzi: %d %d\n",pouzi.lo,pouzi.hi);
    if (pouzi.hi < kde) return 999;
    used++;
    kde = pouzi.hi + 1;
    if (kde == 10001) break;
  }
  //printf("colors %d %d %d returns %d\n",x,y,z,used);
  return used;
}

int main() {
  getline(cin,Tline); stringstream(Tline) >> T;
  for (int t=1; t<=T; t++) {
    cin >> N;
    map<string,int> color;
    C=0;
    string ccc;
    REP(i,N) { cin >> ccc >> LO[i] >> HI[i]; if (!color.count(ccc)) color[ccc]=C++; F[i]=color[ccc]; }

    fprintf(stderr,"test case %d\n",t);
    //REP(i,N) fprintf(stderr,"color %d paint %d %d\n",F[i],LO[i],HI[i]);

    int res = 999;
    for (int i=0; i<C; i++) for (int j=0; j<=i; j++) for (int k=0; k<=j; k++) res = min(res, doit(i,j,k) );
    if (res == 999) {
      printf("Case #%d: IMPOSSIBLE\n",t);
    } else {
      printf("Case #%d: %d\n",t,res);
    }
  }
  return 0;
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
