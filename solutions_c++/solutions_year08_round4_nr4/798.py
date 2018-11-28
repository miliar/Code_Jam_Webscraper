#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <inttypes.h>
#include <ctype.h>
#include <algorithm>
#include <utility>
#include <iostream>
using namespace std;
#define TRACE(x...)
#define PRINT(x...) TRACE(printf(x))
#define WATCH(x) TRACE(cout << #x" = " << x << "\n")
#define _inline(f...) f() __attribute__((always_inline)); f
#define _foreach(it, b, e) for (typeof(b) it = (b); it != (e); it++)
#define foreach(x...) _foreach(x)
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
const int INF = 0x3F3F3F3F;
const int NULO = -1;
const double EPS = 1e-10;
_inline(int cmp)(double x, double y = 0, double tol = EPS) {
  return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}
int main() {
  TRACE(setbuf(stdout, NULL));
	int _43;
	scanf("%d", &_43);
	foreach(_42, 1, _43+1) {
         int n;
         char buf[1010], buf2[1010];
		printf("Case #%d:", _42);
		scanf(" %d %s ", &n, buf);
		int k = strlen(buf);
		int perm[50];
		foreach(i, 0, n) perm[i] = i;
		int m = 100000;
		do {
            foreach(i, 0, k/n) foreach(j, 0, n) {
                       buf2[n*i + perm[j]] = buf[n*i + j];
            }
            int g = 1;
            int ult = buf2[0];
            foreach(i, 1, k) {
                       if (buf2[i] != ult)
                          g++;
                       ult = buf2[i];
            }
            m = min(g, m);
      } while (next_permutation(perm, perm + n));
      printf(" %d\n", m);
	}
  return 0;
}
