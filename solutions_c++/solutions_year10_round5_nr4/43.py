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

int sum, base;
int ans;

int d1[15], d2[15];
int dq;
int s;

int color[100][80];

bool Can(int x) {
	int i;
	i = 1;
	while (x) {
		if (color[i][x % base]) return false;
		x /= base;
		i++;
	}
	return true;
}

void Set(int x) {
	int i;
	i = 1;
	while (x) {
		color[i][x % base] = 1;
		x /= base;
		i++;
	}
}

void UnSet(int x) {
	int i;
	i = 1;
	while (x) {
		color[i][x % base] = 0;
		x /= base;
		i++;
	}
}

void Fun(int p) {
	if (s > sum) return;
	if (s == sum) {
		ans++;
		return;
	}
	int i;
	fi(p + 1, sum) {
		if (!Can(i)) continue;
		Set(i);
		s += i;
		Fun(i);
		s -= i;
		UnSet(i);
	}
}

void Solve() {
	scanf("%d %d", &sum, &base);
	ans = 0;

	ZERO(color);
	s = 0;
	Fun(0);
	printf("%d\n", ans);
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
