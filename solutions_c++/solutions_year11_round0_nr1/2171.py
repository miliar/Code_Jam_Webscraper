#include <algorithm>

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
#include <cstring>

#define SIZE(s) ((int)((s).size()))
#define FOREACH(it,vec) for(typeof((vec).begin())it=(vec).begin();it!=(vec).end();++it)
#define REP(i,n) for(int i=0;i<(int)(n);++i)

using namespace std;

int posb,poso;
int cas;
char who;
int what;
int N,T;
vector<pair<int,int> > B,O;

void moveb(int b) {
  if (b >= SIZE(B)) return;
  if (posb == B[b].second) return;
  if (posb < B[b].second) ++posb;
  else --posb;
}

void moveo(int o) {
  if (o >= SIZE(O)) return;
  if (poso == O[o].second) return;
  if (poso < O[o].second) ++poso;
  else --poso;
}

int main(void) {
  cin >> T;
  REP(t,T) {
    cas = 0;
    poso = 1;
    posb = 1;

    cin >> N;
    B.resize(0); O.resize(0);
    REP(n,N) {
      cin >> who >> what;
      if (who=='O') O.push_back(make_pair(n,what));
      if (who=='B') B.push_back(make_pair(n,what));
    }

    int b=0;
    int o=0;
    while(b<SIZE(B) && o < SIZE(O)) {
      if (B[b].first < O[o].first && posb == B[b].second) { ++cas; ++b; moveo(o); continue; }
      if (B[b].first > O[o].first && poso == O[o].second) { ++cas; ++o; moveb(b); continue; }
      moveo(o);
      moveb(b);
      ++cas;
    }
    while(b<SIZE(B)) {
      while(B[b].second != posb) { ++cas; moveb(b); }
      ++cas;
      ++b;
    }
    while(o<SIZE(O)) {
      while(O[o].second != poso) { ++cas; moveo(o); }
      ++cas;
      ++o;
    }
        
    cout << "Case #" << (t+1) << ": " <<  cas << endl;
  }
  return 0;
}
