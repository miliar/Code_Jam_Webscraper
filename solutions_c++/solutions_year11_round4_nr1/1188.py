#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <queue>
#include <vector>
#include <algorithm>
#include <time.h>
#include <cmath>
#include <cassert>
using namespace std;

#define MAXN 2000

int start[MAXN];
int end[MAXN];
pair<int, int> w[MAXN];

void solve() {
  double X, S, R, t;
  int n;
  cin >> X >> S >> R >> t >> n;
  int sum_len = 0;
  double tm = 0;
  for(int i = 0; i < n; i++) {
    w[i].second = i;
    cin >> start[i] >> end[i] >> w[i].first;
    sum_len += end[i] - start[i];
    tm += (end[i] - start[i]) / (w[i].first + S + 0.);
  }
  sort(w, w + n);
  sum_len = X - sum_len;
  tm += sum_len / (S + 0.);
  double tt = sum_len / (R + 0.);
  if(tt > t) {
    tm -= (R - S) * t / (S + 0.);
    printf("%.10lf\n", tm);
    return;
  }
  t -= tt;
  tm -= (R - S) * tt / (S + 0.);
  for(int i = 0; i < n; i++) {
    double len = end[w[i].second] - start[w[i].second];
    double tt = len / (w[i].first + R + 0.);
    if(tt > t) {
      tm -= (R - S) * t / (w[i].first + S + 0.);
      printf("%.10lf\n", tm);
      return;
    }
    t -= tt;
    tm -= (R - S) * tt / (w[i].first + S + 0.);
  }
  printf("%.10lf\n", tm);
}

int main() {
#ifdef shindo
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
#endif

  int t; scanf("%d", &t);
  for(int tt = 1; tt <= t; tt++) {
    printf("Case #%d: ", tt);
    solve();
  }

#ifdef shindo
  //printf("\n\n%lf\n", clock() * 1e-3);
#endif
}
