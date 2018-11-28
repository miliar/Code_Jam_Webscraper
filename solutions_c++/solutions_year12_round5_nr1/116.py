#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <stack>

#define MAX_N 1005
#define PA pair<int, int>
#define PA2 pair<double, int>

using namespace std;

int tests;
int n;
int l[MAX_N];
double p[MAX_N];
PA2 tmp[MAX_N];

inline void getInput() {
  scanf("%d", &n);
  for (int i = 0 ; i < n ; i ++) {
    scanf("%d", &l[i]);
  }
  for (int i = 0 ; i < n ; i ++) {
    scanf("%lf", &p[i]);
    //p[i] = 1 - p[i] / 100;
  }
  return ;
}

inline void solve() {
  for (int i = 0 ; i < n ; i ++) {
    if (p[i] != 0) tmp[i] = PA2(l[i] / p[i], i);
    else tmp[i] = PA2(1000000000, i);
  }
  sort(tmp, tmp + n);
  for (int i = 0 ; i < n ; i ++) {
    printf(" %d", tmp[i].second);
  }
  return ;
}

int main() {
  scanf("%d", &tests);
  for (int test = 1 ; test <= tests ; test ++) {
    getInput();
    printf("Case #%d:", test);
    solve();
    printf("\n");
  }
  return 0;
}