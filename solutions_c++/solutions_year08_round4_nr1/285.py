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

bool seen[10005][2];
int memo[10005][2];
int val[10005], mod[10005], op[10005];
int n;

int doit(int i, int v) {
	int & ret = memo[i][v];
	if (seen[i][v]) return ret;
	seen[i][v] = true;
	ret = -1;
	int cur, a, b, ra, rb;
	// Leaf
	if (val[i] >= 0) {
		if (val[i] == v) return ret = 0;
		else return ret = -1;
	}
	// AND
	if (op[i] == 1 || mod[i]) {
		FOR (a,2) FOR (b,2) if ((a & b) == v) {
			ra = doit(2 * i, a);
			rb = doit(2 * i + 1, b);
			if (ra < 0 || rb < 0) continue;
			cur = ra + rb;
			if (op[i] != 1) cur++;
			if (ret < 0 || cur < ret) ret = cur;
		}
	}
	// OR
	if (op[i] == 0 || mod[i]) {
		FOR (a,2) FOR (b,2) if ((a | b) == v) {
			ra = doit(2 * i, a);
			rb = doit(2 * i + 1, b);
			if (ra < 0 || rb < 0) continue;
			cur = ra + rb;
			if (op[i] != 0) cur++;
			if (ret < 0 || cur < ret) ret = cur;
		}
	}
	return ret;
}

int main() {
	int cases, casen, ans, v, i;
	cin >> cases;
	for (casen = 1; casen <= cases; casen++) {
		cin >> n >> v;
		for (i = 1; i <= n; i++) {
			if (i <= (n - 1) / 2) {
				cin >> op[i] >> mod[i];
				val[i] = -1;
			} else {
				cin >> val[i];
				mod[i] = op[i] = -1;
			}
		}
		CLR(seen, 0);
		ans = doit(1, v);
		cout << "Case #" << casen << ": ";
		if (ans < 0) cout << "IMPOSSIBLE";
		else cout << ans;
		cout << endl;
	}
	return 0;
}
