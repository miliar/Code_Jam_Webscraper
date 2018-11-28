#include <iostream>
#include <cstdio>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <numeric>
#include <functional>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <deque>
#include <stack>
#include <queue>
#include <string>
#include <sstream>
#include <fstream>
#include <complex>
#include <iterator>
#include <memory>
#include <utility>
using namespace std;
#define REP(i,n) for(int i=0;i<(int)n;++i)
#define rep(i,s,n) for(int i=s;i<(int)n;++i)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define ALL(c) (c).begin(), (c).end()
#define MP(a, b) make_pair((a), (b))
typedef unsigned int ui;
typedef unsigned long long ull;
typedef long double ld;
typedef long long ll;

enum {
  DEBUG = 0
};

ll gcd(ll a, ll b) {
  return a == 0 ? b : gcd(b % a, a);
}

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    int N;
    cin >> N;
    char schedule[N+1][N+1];
    for (int i = 0; i < N; ++i) {
      scanf("%s", schedule[i]);
    }
    if (DEBUG) {
      for (int i = 0; i < N; ++i) {
	printf("%s\n", schedule[i]);
      }
    }
    double rpis[N];
    double owps[N];
    for (int r = 0; r < N; ++r) {
      double RPI = 0.0;
      int nw = 0, ng = 0;
      for (int c = 0; c < N; ++c) {
	if (schedule[r][c] == '.') continue;
	if (schedule[r][c] == '1') ++nw;
	++ng;
      }
      double WP = (double)nw / ng;
      if (DEBUG) {
	printf("WP: %f\n", WP);
      }
      RPI += 0.25 * WP;

      int no = 0;
      double swp = 0.0;
      for (int rr = 0; rr < N; ++rr) {
	if (schedule[r][rr] == '.') continue;
	++no;
	int nw = 0, ng = 0;
	for (int cc = 0; cc < N; ++cc) {
	  if (cc == r) continue;
	  if (schedule[rr][cc] == '.') continue;
	  if (schedule[rr][cc] == '1') ++nw;
	  ++ng;
	}
	double WP = (double)nw / ng;
	swp += WP;
      }
      double OWP = swp / no;
      if (DEBUG) {
	printf("OWP: %f\n", OWP);
      }
      RPI += 0.5 * OWP;

      rpis[r] = RPI;
      owps[r] = OWP;
    }

    for (int r = 0; r < N; ++r) {
      double sowp = 0.0;
      int ng = 0;
      for (int c = 0; c < N; ++c) {
	if (schedule[r][c] == '.') continue;
	sowp += owps[c];
	++ng;
      }
      double OOWP = sowp / ng;
      rpis[r] += 0.25 * OOWP;
    }
    printf("Case #%d:\n", t);
    for (int i = 0; i < N; ++i) {
      printf("%f\n", rpis[i]);
    }
  }
}
