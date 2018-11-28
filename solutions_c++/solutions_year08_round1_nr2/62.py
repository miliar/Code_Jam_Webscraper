#include<iostream>
#include<sstream>
#include<cstdlib>
#include<cmath>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
typedef vector<int>VI;typedef vector<VI>VVI;
typedef vector<string>VS;
typedef pair<int,int>PII;
#define FOR(i,n) for((i)=0;(i)<(n);(i)++)
#define FORN(i,n) for((i)=(n)-1;(i)>=0;(i)--)
#define BE(a) ((a).begin()),((a).end())
#define SI(a) ((a).size())
#define PB push_back
#define MP make_pair
#define FORIT(i,a) for((i)=(a).begin();(i)!=(a).end();(i)++)
#define CLR(a,v) memset((a),(v),sizeof(a))

VI a[2005], b[2005], c, d, e;

int main() {
	int cases, casen, n, m, i, j, k;
	bool changed, sux;
	cin >> cases;
	for (casen = 1; casen <= cases; casen++) {
		cin >> n >> m;
		c = VI(n, 0);
		d = VI(m, 0);
		e = VI(m, -1);
		FOR (i,m) {
			cin >> k;
			a[i].resize(k);
			b[i].resize(k);
			FOR (j,k) {
				cin >> a[i][j] >> b[i][j];
				a[i][j]--;
				if (b[i][j]) e[i] = a[i][j];
			}
		}
		cout << "Case #" << casen << ":";
		changed = true;
		while (changed) {
			changed = false;
			sux = false;
			FOR (i,m) {
				FOR (j,SI(a[i])) if (c[a[i][j]] == b[i][j]) break;
				if (j < SI(a[i])) continue;
				if (e[i] >= 0) {
					c[e[i]] = 1;
					changed = true;
				} else {
					sux = true;
					break;
				}
			}
			if (sux) {
				cout << " IMPOSSIBLE" << endl;
				break;
			}
		}
		if (!sux) {
			FOR (i,n) cout << " " << c[i];
			cout << endl;
		}
	}
	return 0;
}
