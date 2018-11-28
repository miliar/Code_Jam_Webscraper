#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define SZ(x) (int)(x.size())
#define F0(i,n) for(i=0;i<n;i++)
#define F1(i,n) for(i=1;i<=n;i++)
const int inf = 1000000009;
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;

int i, j, k, m, n, l, ans, x, y;
int times;
string s;

int dx[] = {-1,0,1,0};
int dy[] = {0,1,0,-1};
int X[100000], Y[100000];

int main() {

//	freopen("x.in", "r", stdin);

	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);

//	freopen("A-large.in", "r", stdin);
//	freopen("A-large.out", "w", stdout);

	int tt, tn; cin >> tn;
	F1(tt,tn) {
		printf("Case #%d: ", tt);
		n = 0;
		cin >> l;
		set<pii> S1, S2;
		set<pii>::iterator it;
	
		k = 0;
		pii cur;
		S1.insert(cur);
		S2.insert(cur);
		n = 0;
		while (l--) {
			cin >> s >> times;
			while (times--) {
				F0(i,SZ(s)) {
					if (s[i] == 'F') {
						cur.first += dx[k];
						cur.second += dy[k];
						S1.insert(cur);
						S2.insert(pii(cur.second, cur.first));
						cur.first += dx[k];
						cur.second += dy[k];
						S1.insert(cur);
						S2.insert(pii(cur.second, cur.first));
						X[++n] = cur.first/2;
						Y[n] = cur.second/2;
					} else if (s[i] == 'R') { k = (k+1) % 4; }
					else { k = (k+3) % 4; }
				}
			}
		}
		ll ans = 0;
		for (i = 0; i < n; i++) {
			ans += (X[i] * Y[i+1] - X[i+1] * Y[i]);
		}
		ans /= 2;
		if (ans > 0) ans = -ans;
		for (x = -102; x <= 102; x++) {
			for (y = -102; y <= 102; y++) {
				pii p;
				p = pii(2*x+1, 2*y+1);
				it = S1.lower_bound(p);
				if (it != S1.begin() && it != S1.end() && it->first == p.first) {
					it--;
					if (it->first == p.first) {
						ans++;
						continue;
					}
				}
				p = pii(2*y+1, 2*x+1);
				it = S2.lower_bound(p);
				if (it != S2.begin() && it != S2.end() && it->first == p.first) {
					it--;
					if (it->first == p.first) {
						ans++;
						continue;
					}
				}
			}
		}
		cout << ans;
		printf("\n");
	}
	return 0;
}
