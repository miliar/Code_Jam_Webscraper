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
long long int V1[1000], V2[1000];
int main() {
  TRACE(setbuf(stdout, NULL));
	int T;
	scanf("%d", &T);
	for (int _42 = 1; _42 <= T; _42++) {
		printf("Case #%d: ", _42);
		int n;
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			scanf("%lld", &V1[i]);
		}
		for (int i = 0; i < n; i++) {
			scanf("%lld", &V2[i]);
		}
		sort(V1, V1+n);
		sort(V2, V2+n);
		reverse(V2, V2+n);
		long long int M1 = 0LL;
		for (int i = 0; i < n; i++)
			M1 += V1[i]*V2[i];
		printf("%lld\n", M1);
	}
  return 0;
}
