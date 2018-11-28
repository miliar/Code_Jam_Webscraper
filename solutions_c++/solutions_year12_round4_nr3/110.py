#include <iostream>
#include <cstring>
#include <algorithm>
#include <cstdio>
#include <ctime>
#include <vector>
#include <fstream>
#include <sstream>
#include <queue>
#include <cmath>
#include <set>
using namespace std;
#define L(s) (int)((s).size())
#define pb push_back
#define pii pair<int, int>
#define mp make_pair
#define x first
#define y second
#define inf 1000000000
#define all(s) (s).begin(), (s).end()
#define ll long long
#define VI vector<int>
#define ull unsigned ll
int n, t;
int a[2222];
int h[2222];
int main() {
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> t;
	for(int curt = 1; curt <= t; ++curt) {
		cerr << curt << endl;
		cin >> n;
		for(int i = 0; i < n - 1; ++i) {
			cin >> a[i]; --a[i];
		}
		printf("Case #%d:", curt);
		bool ok = 1;
		for(int i = 0; i < n - 1 && ok; ++i) {
			for(int j = i + 1; j < a[i]; ++j)
				if (a[j] > a[i]) {
					ok = 0; break;
				}
		}
		if (!ok) {
			printf(" Impossible\n");
			continue;
		}
		a[n - 1] = n;
		for(int i = 0; i < n; ++i) h[i] = -1;
		for(int cur = 0; cur < n; cur = a[cur]) h[cur] = 1000000000;
		bool upd = 1;
		while(upd) {
			upd = 0;
			for(int i = 0; i < n;) if (h[i] == -1) {
				int j = i + 1;
				while(j < n && h[j] == -1) ++j;
				int nxt = a[j];
	//			cerr << i << " " << j << " " << nxt << endl;
				double diff = h[nxt] - h[j];
	//			cerr << diff << endl;
	//			cerr << nxt - j << endl;
	//			cerr << j - i << endl;
				diff /= (nxt - j);
				diff *= (j - i);
	//			cerr << diff << endl;
				int inter = (int)(h[j] - diff) - 1;
	//			cerr << inter << endl;
				if (nxt == n) inter = h[j] - 1;
				while(i < j) {
					if (a[i] == j) {
						upd = 1;
						h[i] = inter;
					}
					++i;
				}
			} else ++i;
		}
	//	for(int i = 0; i < n; ++i) {
	//		cerr << i << " " << h[i] << endl;
	//	}
	//	cerr << endl;
		for(int i = 0; i < n; ++i) {
			if (h[i] < 0 || h[i] > 1000000000) {
				cerr << "ERROR " << i << endl;
				return 0;
			}
			for(int j = i + 1; j < n; ++j) {
				ll right = (ll)h[i] * (a[i] - i) + (ll)(h[a[i]] - h[i]) * (j - i);
				ll left = (ll)h[j] * (a[i] - i);
				if (j < a[i] && left >= right) {
					cerr << i << " " << j << endl;
					cerr << "ERROR\n";
					return 0;
				}
				if (j > a[i] && left > right) {
					cerr << i << " " << j << endl;
					cerr << "ERROR\n";
					return 0;
				}
			}
		}
		for(int i = 0; i < n; ++i) {
			printf(" %d", h[i]);
		}
		printf("\n");
	}
}
