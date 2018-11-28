#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <list>
#include <set>
#include <map>
#include <sstream>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cstdio>

using namespace std;

typedef long long ll;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<string> VS;
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define sz(v) (int)v.size()
#define clr(x, v) memset(x, v, sizeof(x))
#define rep(i, l, u) for(int i = (l); i < (u); i++)
#define repv(i, v) for(i = 0; i < (int)v.size(); i++)
#define repi(it, c) for(typeof(c.begin()) it = c.begin(); it != c.end(); ++it)
#define PI acos(-1.0)

int d[200][200];

int f (int x, bool flag) {
	if (flag) {
		if (x % 3 == 0) {
			if (x < 3) return -100;
			else return (x - 3) / 3 + 2;
		}
		else if (x % 3 == 1) {
			if (x < 4) return -100;
			else return (x - 4) / 3 + 2;
		}
		else if (x % 3 == 2) {
			if (x < 2) return -100;
			else return (x - 2) / 3 + 2;
		}
	}
	else {
		if (x % 3 == 0) return x / 3;
		else if (x % 3 == 1) return (x - 1) / 3 + 1;
		else if (x % 3 == 2) return (x - 2) / 3 + 1;
	}
}

int main () {
	int i, j, k, T, ca;
	int a[200], n, s, p;

	freopen ("/home/shuo/Desktop/A.in", "r", stdin);
	freopen ("/home/shuo/Desktop/ot", "w", stdout);

	scanf ("%d", &T);
	for (ca = 1; ca <= T; ca ++) {
		scanf ("%d%d%d", &n, &s, &p);
		for (i = 1; i <= n; i++) scanf ("%d", &a[i]);
		clr (d, 0);
		for (j = 1; j <= s; j++)
			d[0][j] = -100;

		for (i = 1; i <= n; i++)
			for (j = 0; j <= s; j++) {
				d[i][j] = max (d[i][j], d[i-1][j] + (f (a[i], false) >= p ? 1 : 0));
				if (j >= 1) d[i][j] = max (d[i][j], d[i-1][j-1] + (f (a[i], true) >= p ? 1 : 0));
			}
		printf ("Case #%d: %d\n", ca, d[n][s]);
	}
	return 0;
}

