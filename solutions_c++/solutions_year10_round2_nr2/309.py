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

#define MAX 100

int n, k, b, t;

int x[MAX];
int v[MAX];

int ans;

bool Can(int x, int v) {
	if ((b - x) % v == 0) {
		return (b - x) / v <= t;
	} else {
		return (b - x) / v + 1 <= t;
	}
}

void Swap(int a, int b) {
	//swap(x[a], x[b]);
	swap(v[a], v[b]);
}

double eps = 1e-9;

double Time(int x, int v) {
	return (double)(b - x) / v;
}

void Solve() {
	int i, j;
	int f;
	int g;
	ans = 0;
	g = 0;
	fdj(n, 1) {
		if (k == 0) break;
		if (!Can(x[j], v[j])) {
			g++;
		} else {
			ans += g;
			k--;
		}
	}
	if (k != 0) {
		printf("IMPOSSIBLE\n");
		return;
	}
	printf("%d\n", ans);
	
}

int main() {
	int i;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d", &testq);
	for (test = 1; test <= testq; test++) {
		printf("Case #%d: ", test);
		scanf("%d %d %d %d", &n, &k, &b, &t);
		ZERO(x);
		ZERO(v);
		fi(1, n) {
			scanf("%d", &x[i]);
		}
		fi(1, n) {
			scanf("%d", &v[i]);
		}
		Solve();
	}
	return 0;
}
