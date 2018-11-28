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

#define MAX 1100
#define INF 100000000000000LL

int64 n;

int64 m[MAX];

int64 v[MAX][MAX];

int64 d[MAX][MAX][12];

int64 Fun(int64 l, int64 r, int64 q) {
	if (l == r) {
		if (q > m[l]) return INF;
		return 0;
	}
	if (d[l][r][q] != -1) return d[l][r][q];
	int64 res;
	int64 h;
	h = (l + r) / 2;
	res = 0;
	res = min( Fun(l, h, q + 1) + Fun(h + 1, r, q + 1), Fun(l, h, q) + Fun(h + 1, r, q) + v[l][r]);
	d[l][r][q] = res;
	return res;
}

int64 ans;

int main() {
	int i, j;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%lld", &testq);
	for (test = 1; test <= testq; test++) {
		printf("Case #%lld: ", test);
		scanf("%lld", &n);
		n = 1LL << n;
		fi(1, n) {
			scanf("%lld", &m[i]);
		}
		memset(d, -1, sizeof(d));
		for (j=2; j <= n; j *= 2) {
			for (i=1; i<=n; i+=j) {
				scanf("%lld", &v[i][i + j - 1]);
			}
		}
		ans = Fun(1, n, 0);
		printf("%lld\n", ans);
	}
	return 0;
}
