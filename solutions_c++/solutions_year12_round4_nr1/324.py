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
int d[11111], l[11111], f[11111];

void solve(int testcase) {
  printf("Case #%d: ", testcase);
  eprintf("Case #%d: ", testcase);
  scanf("%d", &n);
  for (int i=0; i<n; ++i)
    scanf("%d%d", &d[i], &l[i]);
  scanf("%d", &d[n]);
  for (int i=0; i<=n; ++i)
    f[i]=0;
  f[0]=d[0];
  bool yes=false;
  for (int i=0; i<n; ++i) {
    if (d[n]-d[i]<=f[i])
      yes=true;
    for (int j=i+1; j<n && d[j]-d[i]<=f[i]; ++j) {
      f[j] = max(f[j], min(d[j]-d[i], l[j]));
    }
  }
  printf("%s\n", (yes ? "YES" : "NO"));
  eprintf("%s\n", (yes ? "YES" : "NO"));
}

int main() {
  int T;
  scanf("%d", &T);
  for (int i = 1; i <= T; ++i)
    solve(i);
  return 0;
}
