#define _CRT_SECURE_NO_DEPRECATE

#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <memory.h>
#include <string.h>

using namespace std;

#define pb push_back
#define pf push_front
#define mp make_pair
#define fi(a, b) for(i=a; i<=b; i++)
#define fj(a, b) for(j=a; j<=b; j++)
#define fo(a, b) for(o=a; o<=b; o++)
#define fdi(a, b) for(i=a; i>=b; i--)
#define fdj(a, b) for(j=a; j>=b; j--)
#define fdo(a, b) for(o=a; o>=b; o--)
#define ZERO(x) memset(x, 0, sizeof(x));
#define COPY(x, y) memcpy(x, y, sizeof(y));
#define SIZE(x) (int)x.size()
#define LEN(x) (int)x.length()

typedef long long int64;

int64 test, testq;

#define MAX 2000001

bool f[MAX];
int64 p[MAX];
int64 pq;

int64 l, n;

int64 a[MAX];

int64 PowMod(int64 x, int64 y, int64 p) {
	int64 res;
	res = 1;
	while (y) {
		if (y & 1) res = (int64)(((int64)res * (int64)x) % (int64)p);
		y >>= 1;
		x = (int64)(((int64)x * (int64)x) % (int64)p);
	}
	return res;
}

int64 mult(int64 x, int64 y, int64 p) {
	return int64(((int64)x * (int64)y) % (int64)p);
}

int64 div(int64 x, int64 y, int64 p) {
	return mult(x, PowMod(y, p - 2, p), p);
}

bool IsPrime(int64 x) {
	int64 i;
	fi(2, x - 1) {
		if (x % i == 0) return false;
	}
	return true;
}

int64 Solve2() {
	if (a[1] == a[2]) return a[1];

	return -1;
}

int64 Solve() {
	int64 A, B;
	if (test == 16) {
		test = test;
	}
	int64 i, j;
	int64 h;
	int64 x;
	int64 diff[100];
	int64 g;
	int64 res;
	scanf("%lld %lld", &l, &n);
	fi(1, n) {
		scanf("%lld", &a[i]);
	}
	if (n == 1) return -1;
	if (n == 2) return Solve2();
	g = 1;
	fi(1, l) {
		g *= 10;
	}
	res = -1;
	for (i = 1; p[i] <= g; i++) {
		h = 1;
		for (j=1; j<=n; j++) {
			if (a[j] >= p[i]) {
				h = 0;
				break;
			}
		}
		if (!h) continue;
		h = 1;
		fj(1, n - 1) {
			diff[j] = ((a[j + 1] - a[j] % p[i]) + p[i]) % p[i];
		}
		A = mult(diff[2], PowMod(diff[1], p[i] - 2, p[i]), p[i]);
		B = a[2] - mult(A, a[1], p[i]);
		B %= p[i];
		B = (B + p[i]) % p[i];
		
		x = a[1];
		for (j = 2; j <= n; j++) {
			x = int64(((int64)A * (int64)x + (int64)B) % p[i]);
			if (x != a[j]) {
				h = 0;
				break;
			}
		}
		if (h) {
			x = int64(((int64)A * (int64)x + (int64)B) % p[i]);
			if (res != -1 && x != res) {
				return -1;
			}
			res = x;
		}
	}
	return res;
}

void Init() {
	int64 i, j;
	for (j=2; j<=1000010; j++) {
		if (f[j]) continue;
		pq++;
		p[pq] = j;
		for (i=2*j; i <= 1000010; i += j) {
			f[i] = 1;
		}
	}
}

void Temp() {
	int64 i;
	int64 x;
	x = 2;
	fi(1, 100) {
		x = (2 * x + 5) % 37;
		printf("%lld ", x);
	}
	exit(0);
}

int64 ans;

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	Init();
	//Temp();
	scanf("%lld", &testq);
	for (test = 1; test <= testq; test++) {
		printf("Case #%lld: ", test);
		ans = Solve();
		if (ans == -1) {
			printf("I don't know.\n");
		} else {
			printf("%lld\n", ans);
		}
	}
	return 0;
}
