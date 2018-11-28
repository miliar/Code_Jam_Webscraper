#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <utility>
#include <vector>
#include <cmath>
#include <fstream>
#include <queue>
#include <list>
#include <set>
using namespace std;

#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define fill(x, y) memset(x, y, sizeof(x))
#define deb(x) cerr << #x << " = " << (x) << "; "
#define debln(x) cerr << #x << " = " << (x) << endl
#define EPS 1e-30

typedef pair<int, int> ii;
typedef pair<int, ii> iii;

int group[2000001];
int gsize[2000001];

void rpair(int x, int g) {
	group[x] = g;

	int digit = 0;
	int mult = 1;
	while (mult <= x) {
		digit++;
		mult *= 10;
	}
	int y = pow(10, digit - 1);

	for (int i = 0; i < digit - 1; i++) {
		x = (x / 10) + (x % 10) * y;
		if (x <= 2000000) group[x] = g;
	}
}

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	int t;
	scanf("%d\n", &t);

	for (int i = 1; i <= t; i++) {
		fill(group, 0);
		fill(gsize, 0);

		int a, b;
		scanf("%d %d\n", &a, &b);
		int ans = 0;
		int g = 0;
		for (int j = a; j <= b; j++) {
			if (group[j] == 0) rpair(j, ++g);
			gsize[group[j]]++;
		}

		for (int j = 1; j <= g; j++) {
			ans += gsize[j] * (gsize[j] - 1) / 2;
		}

		printf("Case #%d: %d\n", i, ans);
	}

	return 0;
}
