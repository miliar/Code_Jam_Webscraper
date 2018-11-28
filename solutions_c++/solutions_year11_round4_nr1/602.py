#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <iostream>
#include <math.h>
#include <assert.h>
#include <vector>

using namespace std;
typedef long long ll;
typedef unsigned int uint;
typedef unsigned long long ull;
static const double EPS = 1e-9;
static const double PI = acos(-1.0);

#define REP(i, n) for (int i = 0; i < (int)(n); i++)
#define FOR(i, s, n) for (int i = (s); i < (int)(n); i++)
#define FOREQ(i, s, n) for (int i = (s); i <= (int)(n); i++)
#define FORIT(it, c) for (__typeof((c).begin())it = (c).begin(); it != (c).end(); it++)
#define MEMSET(v, h) memset((v), h, sizeof(v))

void solve();
int main() {
  int test;
  scanf("%d", &test);
  int test_case = 0;
  while (test--) {
    test_case++;
    printf("Case #%d: ", test_case);
    solve();
  }
}

double X, S, R, T;
int N;
pair<double, double> way[1100];

void solve() {
  //puts("");
  cin >> X >> S >> R >> T >> N;
  double rest = T;
  double all = X;
  double run = R - S;
  REP(i, N) {
    double w, b, e;
    cin >> b >> e >> w;
    way[i] = make_pair(S + w, e - b);
    all -= e - b;
    assert(all >= 0);
  }
  way[N++] = make_pair(S, all);
  sort(way, way + N);
  double ans = 0;
  REP(i, N) {
    double speed = way[i].first;
    double length = way[i].second;
    double runTime = length / (speed + run);
    runTime = min(runTime, rest);
    rest -= runTime;
    double runLength = runTime * (speed + run);
    double walkTime = max((length - runLength), 0.0) / speed;
    ans += runTime + walkTime;
    assert(runTime >= 0 && walkTime >= 0);
  }
  printf("%.8f\n", ans);
}
