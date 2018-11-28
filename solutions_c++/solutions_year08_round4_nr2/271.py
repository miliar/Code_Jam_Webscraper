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

int main() {
	int cases, casen, n, m, a;
	int x1, y1, x2, y2, x3, y3;
	bool ok;
	cin >> cases;
	for (casen = 1; casen <= cases; casen++) {
		cin >> n >> m >> a;
		x1 = y1 = 0;
		x2 = 0;
		y3 = 0;
		ok = false;
		/*for (y2 = 1; y2 <= m; y2++) if (a % y2 == 0) {
			// y2 * x3 == a;
			x3 = a / y2;
			if (x3 >= 0 && x3 <= n) {
				ok = true;
				break;
			}
		}*/
		for (x2 = 0; x2 <= n; x2++) for (y2 = 0; y2 <= m; y2++)
			for (x3 = 0; x3 <= n; x3++) for (y3 = 0; y3 <= m; y3++)
				if (x1 * y2 - x2 * y1 + x2 * y3 - x3 * y2 + x3 * y1 - x1 * y3 == a) {
					ok = true;
					goto lbl;
				}
lbl:
		cout << "Case #" << casen << ": ";
		if (ok) cout << x1 << " " << y1 << " " << x2 << " " << y2 << " " << x3 << " " << y3;
		else cout << "IMPOSSIBLE";
		cout << endl;
	}
	return 0;
}
