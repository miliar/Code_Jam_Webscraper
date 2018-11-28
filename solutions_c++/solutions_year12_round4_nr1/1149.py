#include <iostream>
#include <deque>
#include <cmath>
#include <map>
#include <vector>
#include <string>
#include <set>
#include <ctime>
#include <algorithm>
#include <cstdio>

using namespace std;

#define ll long long
#define pii pair <int, int>
#define mp make_pair

const int MN = 10000 + 10;

int most_left[MN], d[MN], l[MN], n;

inline void upd(int st, int fin, int curr) {
	for(int i = st + 1; i <= n + 1; i ++) {
		if (d[i] > fin)
			break;
		most_left[i] = min(most_left[i], curr);
	}
}
		
inline void solve() {
	for(int i = 1; i <= n; i ++) {
		if (most_left[i] == i)
			continue;
		int lf = most_left[i];
		int len = min(l[i], d[i] - d[lf]);
		upd(lf, d[i] + len, i);
	}
}

int main () {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int k = 0; k < t; k ++) {
		scanf("%d", &n);
		d[0] = l[0] = 0;
		for(int i = 1; i <= n; i ++)
			scanf("%d%d", &d[i], &l[i]);
		scanf("%d", &d[n + 1]);
		l[n + 1] = 0;
		for(int i = 0; i <= n + 1; i ++)
			most_left[i] = i;
		most_left[1] = 0;
		solve();
		printf("Case #%d: ", k + 1);
		if (most_left[n + 1] == n + 1)
			printf("NO\n");
		else printf("YES\n");
	}
	return 0;
}