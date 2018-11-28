#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<queue>
#include<stack>
#include<vector>
#include<algorithm>
#include<numeric>
#include<string>
#include<sstream>
#include<set>
#include<map>
#include<complex>
#include<cassert>
using namespace std;
#define rep(i,s,e) for(int i=(s),___e=(e);i<___e;++i)
#define REP(i,n) rep(i,0,n)
#define ITER(c) __typeof((c).begin())
#define FOR(i,c) for(ITER(c) i=(c).begin(),___e=(c).end();i!=___e;++i)
#define ALL(c) (c).begin(), (c).end()
#define MP make_pair
typedef unsigned int ui;
typedef long double ld;
typedef long long ll;
const double PI = atan(1.0) * 4.0;
int in_c() { int c; while ((c = getchar()) <= ' ') { if (!~c) throw ~0; } return c; }
int in() {
  int x = 0, c;
  while ((ui)((c = getchar()) - '0') >= 10) { if (c == '-') return -in(); if (!~c) return ~0; }
  do { x = 10 * x + (c - '0'); } while ((ui)((c = getchar()) - '0') < 10);
  return x;
}
int R, K, N;
int g[1000];
ll score[1000];
int ride[1000];

int main()
{
  int T = in();
  REP(turn, T) {
    R = in();
    K = in();
    N = in();
    REP(i, N) g[i] = in();
    REP(i, N) {
      ll s = 0;
      int gs = 0;
      for(int j = i, k = i; j < i + N; ++j, k = j % N) {
        if(s + g[k] > K) break;
        s += g[k];
        ++gs;
      }
      score[i] = s;
      ride[i] = gs;
    }
    ll res = 0;
    for(int i = 0, cur = 0; i < R; ++i) {
      res += score[cur];
      cur = (cur + ride[cur]) % N;
    }
    printf("Case #%d: %lld\n", turn + 1, res);
  }
  return 0;
}

