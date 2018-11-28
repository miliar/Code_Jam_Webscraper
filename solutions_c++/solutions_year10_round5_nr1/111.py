#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <utility>

using namespace std;

#define abs(x) ((x) < 0 ? (-(x)) : (x))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define max(x, y) ((x) > (y) ? (x) : (y))

#define mp make_pair
#define pb push_back

typedef long long i64;

bool _p[10000001];
int p[10000001];
int a[1000];

int gcd(int x, int y) {
	x = abs(x); y = abs(y);
	while (x && y) {
		if (x > y) x %= y;
		else y %= x;
	}
	return x + y;
}

int solve(int a, int b, int c) {
	int d = gcd(a, b);
	if (c % d != 0) return -1;
	i64 x1 = 1, y1 = 0;
	i64 x2 = 0, y2 = 1;
	i64 B = b;
	a /= d, b /= d, c /= d;
	while (a && b) {
		if (a > b) {
			i64 t = a / b;
			x1 -= x2 * t;
			y1 -= y2 * t;
			a -= b * t;
		} else {
			i64 t = b / a;
			x2 -= x1 * t;
			y2 -= y1 * t;
			b -= a * t;
		}
	}
	x1 += x2, y1 += y2;
	x1 *= c;
	x1 %= B;
	if (x1 < 0) x1 += B;
	return (int)x1;
}

int main() {
	int pc = 0;
	for (int i = 2; i <= 1000000; ++i) {
		if (!_p[i]) {
			p[pc++] = i;
			if (1000000 / i < i) continue;
			for (int j = i * i; j <= 1000000; j += i) {
				_p[j] = true;
			}
		}
	}
	int T; scanf("%d", &T);
	for (int tt = 0; tt < T; ++tt) {
		int d, k; scanf("%d %d", &d, &k);
		int x = 0;
		for (int i = 0; i < k; ++i) {
			scanf("%d", &a[i]);
			if (a[i] > x) x = a[i];
		}
		
		int z = -1;
		for (int i = 0; i < k - 1; ++i) {
			if (a[i] == a[k - 1]) {
				z = a[i + 1];
				break;
			}
		}
		int D = 1;
		while (d--) {
			D *= 10;
		}
		if ((z == -1) && (k > 2)) {
			int A = -1, B = -1;
			for (int i = 0; (i < pc) && (p[i] < D); ++i) {
				if (p[i] <= x) continue;
				for (int j = 0; j < k - 2; ++j) {
					int q = (a[j] - a[j + 1]) % p[i], r = (a[j + 1] - a[j + 2]) % p[i];
					if (r < 0) r += p[i];
					if (q < 0) q += p[i];
					A = solve(q, p[i], r);
					if (A != -1) {
						B = (a[1] - A * (i64)a[0]) % p[i];
						if (B < 0) B += p[i];
/*						if ((A * (i64)q) % p[i] != r) {
							cout << "OOPS2 " << " " << A << " " << q << " " << p[i] << " " << r << endl;
							return 0;
						}*/
/*						if ((A * (i64)a[0] + B) % p[i] != a[1]) {
							cout << "OOPS " << " " << A << " " << q << " " << p[i] << " " << r << endl;
						}*/
						int Z = (a[k - 1] * (i64)A + B) % p[i];
						for (int j = 0; j < k - 1; ++j) {
							if ((A * (i64)a[j] + B) % p[i] != a[j + 1]) {
								Z = -1;
								break;
							}
						}
						if (Z != -1) {
							if ((z != -1) && (z != Z)) {
								z = -2;
								break;
							} else {
								z = Z;
							}
						}
					}
				}
				if (z == -2) break;
			}
		}
/*		if ((z == -1) && (k > 2)) {
			for (int i = 0; p[i] < D; ++i) {
				if (p[i] <= x) continue;
				for (int A = 0; A < p[i]; ++A) {
					int B = (a[1] - A * (i64)a[0]) % p[i];
					if (B < 0) B += p[i];
					for (int j = 0; j < k - 1; ++j) {
						if ((a[j] * (i64)A + B) % p[i] != a[j + 1]) {
							B = -1;
							break;
						}
					}
					if (B != -1) {
						int Z = (A * (i64)a[k - 1] + B) % p[i];
						if ((z != -1) && (Z != z)) {
							z = -2;
							break;
						}
						z = Z;
					}
				}
				if (z == -2) break;
			}
		}*/
		
		printf("Case #%d: ", tt + 1);
		if (z < 0) printf("I don't know.\n");
		else printf("%d\n", z);
		fflush(stdout);
	}
	return 0;
}
