#include<cstdlib>
#include<cmath>
#include<vector>
#include<string>
#include<algorithm>
#include<cstdio>
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

int n, m;
int memo[105][1005];
bool seen[105][1005];
int a[1005];

int doit(int i, int j) {
	int & ret = memo[i][j];
	if (seen[i][j]) return ret;
	seen[i][j] = true;
	if (j >= m) return ret = 0;
	int k;
	ret = 10000;
	FOR (k,n) if (k != i && a[j] != k) ret = min(ret, 1 + doit(k, j + 1));
	if (a[j] != i) ret = min(ret, doit(i, j + 1));
	return ret;
}

int main() {
	string names[105];
	int cases, casen, i, j, ans;
	char cs[105];
	scanf("%d\n", &cases);
	for (casen = 1; casen <= cases; casen++) {
		scanf("%d\n", &n);
		FOR (i,n) {
			gets(cs);
			names[i] = string(cs);
		}
		scanf("%d\n", &m);
		FOR (i,m) {
			gets(cs);
			FOR (j,n) if (names[j] == string(cs)) break;
			a[i] = j;
		}
		CLR(seen, 0);
		ans = 10000;
		FOR (i,n) ans = min(ans, doit(i, 0));
		printf("Case #%d: %d\n", casen, ans);
	}
	//system("PAUSE");
	return 0;
}
