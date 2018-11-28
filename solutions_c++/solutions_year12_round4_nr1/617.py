#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int MAXN = 10010;

int d[MAXN], l[MAXN];
int n, D;

int f[MAXN];

int check() {
  f[0] = d[0];
  if (d[0] * 2 >= D) return 1;
  for (int i = 1; i < n; ++i) {
    f[i] = 0;
    for (int j = i-1; j >= 0; --j) {
      int dist = d[i] - d[j];
      if (f[j] >= dist && l[j] >= dist)
	if (min(dist, l[i]) > f[i]) f[i] = min(dist, l[i]);
    } 
    //      printf("f[%d] = %d\n", i,f[i]);
    if (f[i] + d[i] >= D) return 1;
  }
  return 0;
}

int main() {
  int t;
  scanf("%d", &t);
  for (int c = 1; c <= t; ++c) {
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) scanf("%d%d", d + i, l + i);
    scanf("%d", &D);

    printf("Case #%d: %s\n", c, check() ? "YES" : "NO");
  }
}
