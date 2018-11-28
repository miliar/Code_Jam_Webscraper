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
bool seen[105][105];
int memo[105][105];
int n, m, t;

int doit(int i, int j) {
	if (i < 0 || j < 0) return 0;
	int & ret = memo[i][j];
	if (seen[i][j]) return ret;
	seen[i][j] = true;
	if (i == 0 && j == 0) return ret = 1;
	if (g[i][j] == '#') return ret = 0;
	ret = (doit(i - 1, j - 2) + doit(i - 2, j - 1)) % 10007;
	return ret;
}

int main() {
	int cases, casen, i, j, k;
	cin >> cases;
	for (casen = 1; casen <= cases; casen++) {
		cin >> n >> m >> t;
		CLR(g, '.');
		FOR (k, t) {
			cin >> i >> j;
			g[i - 1][j - 1] = '#';
		}
		CLR(seen, 0);
		cout << "Case #" << casen << ": " << doit(n - 1, m - 1);
		cout << endl;
	}
	return 0;
}
