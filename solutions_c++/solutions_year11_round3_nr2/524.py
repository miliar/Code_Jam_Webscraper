#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

#define FOR(i,s,t) for (int i = s; i < t; i++)
#define LL long long

int l, n, m, a[1010], f[1010];
double t;

void solve(int test) {
	cin >> l >> t >> n >> m;
	cout << "Case #" << test << ": ";
	FOR(i,0,m)
		cin >> a[i];
	FOR(i,m,n)
		a[i] = a[i % m];
	double ret = 0;
	FOR(i,0,n)
		ret += 2 * a[i];
	if (l == 1) {
		int s = 0;
		double maxi = 0;
		FOR(i,0,n) {
			if (s >= t)
				maxi = max(maxi, (double) a[i]);
			else if (s + 2 * a[i] >= t) {
				maxi = max(maxi, a[i] - (t - s) / 2);
			}
			s += 2 * a[i];
		}
		ret -= maxi;
	} else if (l == 2) {
		f[n] = 0;
		for (int i = n - 1; i >= 0; i--)
			f[i] = max(a[i], f[i + 1]);
		int s = 0;
		double maxi = 0;
		FOR(i,0,n) {
			if (s >= t) {
				maxi = max(maxi, (double) a[i] + f[i + 1]);
			} else if (s + 2 * a[i] >= t) {
				maxi = max(maxi, a[i] - (t - s) / 2 + f[i + 1]);
			}
			s += 2 * a[i];
		}
		ret -= maxi;
	}
	cout << (long long) ret << endl;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int nTest;
	cin >> nTest;

	FOR(i,0,nTest) {
		solve(i + 1);
	}

	return 0;
}
