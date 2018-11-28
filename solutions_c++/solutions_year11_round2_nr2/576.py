#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <queue>
#include <map>
#include <vector>
#include <algorithm>
#include <time.h>
#include <cmath>
#include <cassert>
using namespace std;

typedef long long ll;

#define MAXN 1000

#define STEP_NUM 5000

double p[MAXN];
int cnt[MAXN];
double d;
int n;

bool check(double t) {
  double r = -1e15;
  for(int i = 0; i < n; i++) {
    double rr = p[i] - t;
    rr = max(rr, r);
    double dist = fabs(p[i] - (rr + (cnt[i] - 1)*d));
    if(dist > t + 1e-15) return false;
    r = rr + cnt[i] * d;
  }
  return true;
}

void solve() {
  cin >> n >> d;
  for(int i = 0; i < n; i++) {
    cin >> p[i] >> cnt[i];
  }
  double l = 0, r = 2000;
  for(int step = 1; step <= STEP_NUM; step++) {
    double m = (l + r) / 2;
    if(check(m)) r = m;
    else l = m;
  }
  printf("%.15lf\n", (l + r) / 2);
}

int main() {
#ifndef ONLINE_JUDGE
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
#endif

  int test; cin >> test;
  for(int t = 1; t <= test; t++) {
    printf("Case #%d: ", t);
    solve();
  }  
  
}
