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

int test, testq;

#define INF 1000000000

#define MAX 200

#define MAXD 1000000

int64 l;
int n;
int64 b[MAX];

int64 d[MAXD];

int64 ans;

void Solve () {
	int64 q;
	int i, j;
	scanf("%lld %d", &l, &n);
	fi(1, n) {
		scanf("%lld", &b[i]);
	}
	ZERO(d);
	ans = 0;
	sort(b + 1, b + n + 1);
	if (l >= MAXD / 2) {
		q = (l - MAXD / 2) / b[n];
		ans += q;
		l -= q * b[n];
	}
	fj(1, l) {
		d[j] = INF;
	}
	d[0] = 0;
	fj(1, l) {
		fi(1, n) {
			if (j - b[i] < 0) continue;
			d[j] = min(d[j], d[j - b[i]] + 1);
		}
	}
	ans += d[l];
	if (d[l] == INF) {
		printf("IMPOSSIBLE\n");
	} else {
		printf("%lld\n", ans);
	}
}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d", &testq);
	for (test = 1; test <= testq; test++) {
		printf("Case #%d: ", test);
		Solve();
	}
	return 0;
}
