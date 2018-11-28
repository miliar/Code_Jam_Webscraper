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

char g[105][105];
int n, m;
bool seen[105][105][1 << 10][2];
int memo[105][105][1 << 10][2];

int doit(int i, int j, int mask, int b) {
	if (i >= n) return 0;
	if (j >= m) return doit(i + 1, 0, mask, 0);
	int & ret = memo[i][j][mask][b];
	if (seen[i][j][mask][b]) return ret;
	seen[i][j][mask][b] = true;
	ret = doit(i, j + 1, mask & ~(1 << j), (mask >> j) & 1);
	if (g[i][j] != 'x' && (j == 0 || !((mask >> (j - 1)) & 1)) && (i == 0 || j == 0 || !b) && (i == 0 || j == m - 1 || !((mask >> (j + 1)) & 1)))
		ret = max(ret, 1 + doit(i, j + 1, mask | (1 << j), (mask >> j) & 1));
	return ret;
}

int main() {
	int cases, casen, i, j;
	cin >> cases;
	for (casen = 1; casen <= cases; casen++) {
		cin >> n >> m;
		FOR (i,n) FOR (j,m) cin >> g[i][j];
		CLR(seen, 0);
		cout << "Case #" << casen << ": " << doit(0, 0, 0, 0);
		cout << endl;
	}
	return 0;
}
