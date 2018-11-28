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

int64 test;
int64 testq;

#define MAX 5000

int64 r, k, n;
int64 q[MAX];
int64 color[MAX];

bool Try() {
	int64 sum;
	int64 i;
	sum = 0;
	fi(1, n) {
		sum += q[i];
	}
	if (sum <= k) {
		printf("%lld\n", sum * r);
		return true;
	}
	return false;
}

bool Try2() {
	if (r >= 4 * n) return false;
	int64 ans;
	int64 g;
	int64 i;
	int64 c;
	ans = 0;
	c = 1;
	fi(1, r) {
		g = 0;
		while (1) {
			if (g + q[c] > k) break;
			g += q[c];
			c++;
			if (c > n) c = 1;
		}
		ans += g;
	}
	printf("%lld\n", ans);
	return true;
}

void Solve() {
	if (Try()) return;
	if (Try2()) return;
	int64 ans;
	int64 u;
	int64 g;
	int64 i;
	int64 c;
	int64 p;
	ans = 0;
	ZERO(color);
	c = 1;
	i = 0;
	while (1) {
		i++;
		if (color[c]) break;
		color[c] = i;
		g = 0;
		while (1) {
			if (g + q[c] > k) break;
			g += q[c];
			c++;
			if (c > n) c = 1;
		}
		ans += g;
	}
	p = i - color[c];
	r = r - i + 1;
	u = 0;
	fi(1, p) {
		g = 0;
		while (1) {
			if (g + q[c] > k) break;
			g += q[c];
			c++;
			if (c > n) c = 1;
		}
		ans += g;
		u += g;
	}
	r -= p;
	ans += u * (r / p);
	r = r % p;
	fi(1, r) {
		g = 0;
		while (1) {
			if (g + q[c] > k) break;
			g += q[c];
			c++;
			if (c > n) c = 1;
		}
		ans += g;
		u += g;
	}
	printf("%lld\n", ans);
}

int main() {
	int64 i;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%lld", &testq);
	for (test = 1; test <= testq; test++) {
		scanf("%lld %lld %lld", &r, &k, &n);
		fi(1, n) {
			scanf("%lld", &q[i]);
		}
		printf("Case #%lld: ", test);
		Solve();
	}
	return 0;
}
