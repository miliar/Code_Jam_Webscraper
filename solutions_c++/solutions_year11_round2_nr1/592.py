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

#define MAXN 300
char m[MAXN][MAXN];
int cnt[MAXN];
double wp[MAXN];
double owp[MAXN];
double oowp[MAXN];

void solve() {
  int n; scanf("%d\n", &n);
  for(int i = 0; i < n; i++) {
    gets(m[i]);
  }
  memset(cnt, 0, sizeof cnt);
  memset(wp, 0, sizeof wp);
  for(int i = 0; i < n; i ++) {
    for(int j = 0; j < n; j++) {
      if(m[i][j] == '1') wp[i] += 1;
      if(m[i][j] != '.') cnt[i]++;
    }
    wp[i] /= cnt[i];
  }
  memset(owp, 0, sizeof owp);
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < n; j++) {
      if(i == j) continue;
      if(m[i][j] == '.') continue;
      owp[i] += (wp[j] - (m[j][i] == '1' ? 1. : 0.)/cnt[j]) * cnt[j] / (cnt[j] - 1.);
    }
    owp[i] /= cnt[i];
  }
  memset(oowp, 0, sizeof oowp);
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < n; j++) {
      if(i == j) continue;
      if(m[i][j] == '.') continue;
      oowp[i] += owp[j];
    }
    oowp[i] /= cnt[i];
  }
  for(int i = 0; i < n; i++) {
    printf("%.10lf\n", 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
  }
}

int main() {
#ifndef ONLINE_JUDGE
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
#endif

  int test; cin >> test;
  for(int t = 1; t <= test; t++) {
    printf("Case #%d:\n", t);
    solve();
  }  
  
}
