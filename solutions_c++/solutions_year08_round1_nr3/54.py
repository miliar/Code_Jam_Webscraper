#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <inttypes.h>
// For this program, you have to download the GMP from gmplib.org.
// Compile running "g++ -o numbers numbers.cpp -lgmp"
#include <ctype.h>
#include <algorithm>
#include <utility>
#include <iostream>
#include <gmp.h>
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
	mpf_set_default_prec(1000000);
	mpf_t base, resp, temp;
	mpf_init(base);
	mpf_init(resp);
	mpf_init(temp);
	mpf_set_ui(base, 5);
	mpf_sqrt(base, base);
	mpf_add_ui(base, base, 3);
	int T;
	scanf("%d", &T);
	for (int _42 = 1; _42 <= T; _42++) {
		printf("Case #%d: ", _42);
		int n;
		scanf("%d", &n);
		mpf_pow_ui(resp, base, n);
		mpf_floor(resp, resp);
		mpf_div_ui(temp, resp, 1000);
		mpf_floor(temp, temp);
		mpf_mul_ui(temp, temp, 1000);
		mpf_sub(resp, resp, temp);
		int r = mpf_get_si(resp);
		printf("%03d\n", r);
	}

	mpf_clear(base);
	mpf_clear(resp);

  return 0;
}
