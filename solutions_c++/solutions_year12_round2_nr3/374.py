#include <cmath>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

#define eprintf(...) fprintf(stderr, __VA_ARGS__)

#define sz(c) ((int) (c).size())
#define pb push_back
#define mp make_pair
#define f first
#define s second

int n;
int a[555];
int p[2222222];

void solve(int testcase) {
  printf("Case #%d:\n", testcase);
  eprintf("Case #%d:\n", testcase);
  scanf("%d", &n);
  for (int i=0; i<n; ++i)
    scanf("%d", &a[i]);
  memset(p, 0, sizeof(p));
  int nn=(1<<n);
  int res1=0, res2=0;
  for (int t=0; t<nn; ++t) {
    int sum=0;
    for (int i=0; i<n; ++i)
      if ((t>>i)&1) sum += a[i];
    if (p[sum] == 0) {
      p[sum] = t;
    } else {
      res1 = p[sum] ^ (p[sum]&t);
      res2 = t ^ (p[sum]&t);
    }
  }
  vector <int> r1, r2;
  for (int i=0; i<n; ++i)
    if ((res1>>i)&1) r1.pb(i);
  for (int i=0; i<n; ++i)
    if ((res2>>i)&1) r2.pb(i);
  if (res1 == 0 || res2 == 0) {
    printf("Impossible\n");
    eprintf("Impossible\n");
  } else {
    for (int i=0; i<sz(r1); ++i)
      printf("%d%c", a[r1[i]], " \n"[i+1 == sz(r1)]);
    for (int i=0; i<sz(r2); ++i)
      printf("%d%c", a[r2[i]], " \n"[i+1 == sz(r2)]);
    for (int i=0; i<sz(r1); ++i)
      eprintf("%d%c", a[r1[i]], " \n"[i+1 == sz(r1)]);
    for (int i=0; i<sz(r2); ++i)
      eprintf("%d%c", a[r2[i]], " \n"[i+1 == sz(r2)]);
  }
}

int main() {
  int T;
  scanf("%d", &T);
  for (int i = 1; i <= T; ++i)
    solve(i);
  return 0;
}
