#include <cstdio>
#include <iostream>
#include <vector>
#include <set>
#include <cstring>
#include <string>
#include <map>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <bitset>
#include <queue>
#include <sstream>

using namespace std;

#define mp make_pair
#define pb push_back
#define rep(i,n) for(int i = 0; i < n; i++)
#define re return
#define fi first
#define se second
#define sz(x) ((int) (x).size())
#define all(x) (x).begin(), (x).end()
#define sqr(x) ((x) * (x))
#define y0 y3487465
#define y1 y8687969

typedef vector<int> vi;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<string> vs;
typedef vector<vi> vvi;

template<class T> T abs(T x) {
	re x > 0 ? x : -x;
}

int n;
int m;
ii x[2][100];
int l[2], p[2], q[2];

int main() {
	int tt;
	cin >> tt;
	for (int it = 0; it < tt; it++) {
		cin >> n;
		l[0] = l[1] = 0;
		for (int i = 0; i < n; i++) {
			char a;
			int b;
			cin >> a >> b;
			if (a == 'O') x[0][l[0]++] = mp (b, i); else x[1][l[1]++] = mp (b, i);
		}
		p[0] = p[1] = 0;
		q[0] = q[1] = 1;
		int ans = 0;
		while (p[0] < l[0] || p[1] < l[1]) {
			int op = p[0];
			if (p[0] < l[0]) {
				if (q[0] < x[0][p[0]].fi) q[0]++; else
				if (q[0] > x[0][p[0]].fi) q[0]--; else
				if (p[1] == l[1] || x[0][p[0]].se < x[1][p[1]].se) p[0]++;
			}
			if (p[1] < l[1]) {
				if (q[1] < x[1][p[1]].fi) q[1]++; else
				if (q[1] > x[1][p[1]].fi) q[1]--; else
				if (op == l[0] || x[1][p[1]].se < x[0][op].se) p[1]++;
			}
			ans++;
		}
		printf ("Case #%d: %d\n", it + 1, ans);
	}
	return 0;
}
