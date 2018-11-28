#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>

#include <cstdio>
#include <cstring>
#include <cassert>
#include <cmath>
#include <ctime>

using namespace std;

typedef long long int64;
typedef long double ldouble;

#define PB(a) push_back(a)
#define MP(a, b) make_pair(a, b)

#define PROBLEM "A"

typedef pair<int, int> pii;

const int MAXN = 10100;
pii v[MAXN];
int a[MAXN];

int n;

int main() {
	freopen(PROBLEM ".in", "rt", stdin);
	freopen(PROBLEM ".out", "wt", stdout);

	int T;
	scanf("%d\n", &T);

	for (int t = 1; t <= T; t++) {
		printf("Case #%d: ", t);

		scanf("%d", &n);
		for (int i = 1; i <= n; i++) {
			int x, y;
			scanf("%d %d", &x, &y);
			v[i] = MP(x, y);
		}
		n++;
		int D;
		scanf("%d", &D);
		v[n] = MP(D, 0);

		stable_sort(v+1, v+n+1);

		memset(a, -1, sizeof(a));
        a[1] = v[1].first;

		for (int i = 1; i <= n; i++) {
			if (a[i] == -1) continue;
			int s = v[i].first + a[i];
			for (int j = i+1; j <= n; j++) {
				if (v[j].first > s) break;
				
				int cand = min(v[j].first - v[i].first, v[j].second);
				if (cand > a[j]) a[j] = cand;
			}
		}

		if (a[n] == -1) printf("NO");
		else printf("YES");

		printf("\n");
	}

	return 0;
}
