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

#define MAX 1001010

int testq;
int test;

int n, s, r;
double t;
int k;

int	b[MAX], e[MAX], w[MAX];

int color[MAX];

void Read() {
	int i;
	scanf("%d %d %d", &n, &s, &r);
	scanf("%lf", &t);
	scanf("%d", &k);

	t = min(t, (double)n);

	ZERO(b);
	ZERO(e);
	ZERO(w);

	fi(1, k) {
		scanf("%d %d %d", &b[i], &e[i], &w[i]);
		e[i]--;
	}
}

pair <double, double> g[MAX];

void Solve() {
	double ans;
	double u;
	int i, j;
	ZERO(color);
	fi(1, k) {
		fj(b[i], e[i]) {
			color[j] = 1;
			g[j] = mp(1. / (r + w[i]) - 1. / (s + w[i]), w[i]);
		}
	}

	fi(0, n - 1) {
		if (color[i]) continue;
		g[i] = mp(1. / (r) - 1. / (s), 0);
	}

	double S;

	sort(g, g + n);
	ans = 0;
	fi(0, n - 1) {
		
		u = 1 / (r + g[i].second);

		if (u <= t) {

			t -= u;
			ans += 1 / (r + g[i].second);

		} else {

			S = 1 - (r + g[i].second) * t;

			ans += t + S / (s + g[i].second);

			t = 0;

		}	
		
	}
	
	printf("%.10lf\n", ans);
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