#define _CRT_SECURE_NO_DEPRECATE

#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#define ZERO(x) memset(x, 0, sizeof(x))
#define COPY(x,y) memcpy(x, y, sizeof(y))
#define LEN(x) (int)x.length()
#define SIZE(x) (int)x.size()

typedef long long int64;

int testq;
int test;

int64 pd, pg, n;

void Read() {
	scanf("%lld %lld %lld", &n, &pd, &pg);
}

int64 gcd(int64 x, int64 y) {
	while (x != 0 && y != 0) {
		if (x > y) x %= y;
		else y %= x;
	}
	if (x == 0) return y;
	return x;
}

int64 d;
int64 g;

int64 qd;
int64 qg;

void Solve() {
	int64 t;

	t = gcd(pd, 100);
	d = pd / t;
	qd = 100 / t;

	t = gcd(pg, 100);
	g = pg / t;
	qg = 100 / t;


	if (qd > n) {
		printf("Broken\n");
		return;
	}

	if (g == qg && d != qd) {
		printf("Broken\n");
		return;
	}

	if (g == 0 && d > 0) {
		printf("Broken\n");
		return;
	}

	printf("Possible\n");

}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d", &testq);
	for (test = 1; test <= testq; test++) {
		Read();
		printf("Case #%d: ", test);
		Solve();
		fflush(stdout);
	}
	return 0;
}