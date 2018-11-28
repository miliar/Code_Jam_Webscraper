#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cassert>
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <string>
#include <set>
#include <map>
#include <algorithm>

#define sz(a) int((a).size())
#define tr(c, i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define all(c) (c).begin(),(c).end()
#define INF 2000000000
#define EPS 1e-5
#define PB push_back
#define MP make_pair
#define S second
#define F first
#define X first
#define Y second
#define DEBUG(x) printf("debugging.. %d\n", x);
using namespace std;

typedef long long ll;
typedef pair <int, int> ii;

string tobin(int x, int len) {
	string c;
	while(x) { c.PB(x%2+'0'); x /= 2; }
	while(sz(c) < len) c.PB('0');
	reverse(all(c));
	return c;
}
//------------------------------

int T, n, d[105], l[105], D;
int dp[105][105];

int f(int i, int j) {
	int &ret = dp[i][j];
	if(ret != -1) return ret;
	
	ret = 0;
	
	int range = min(d[j] - d[i], l[j]);
	if(d[j] + range >= D) return ret = 1;
	
//	printf("f(%d, %d), di=%d, dj=%d, range=%d\n", i, j, d[i], d[j], range);
	for(int k = j + 1; k <= n; ++k)
		if(d[k] - d[j] <= range) {
			if(f(j, k) == 1)
				return ret = 1;
		}
		else break;
	
	return ret;
}

int main() {
	scanf("%d", &T);
	
	for(int tc = 0; tc < T; ++tc) {
		printf("Case #%d: ", tc + 1);
		
		scanf("%d", &n);
		
		d[0] = l[0] = 0;
		for(int i = 1; i <= n; ++i)
			scanf("%d%d", &d[i], &l[i]);
		
		scanf("%d", &D);
		
		memset(dp, -1, sizeof(dp));
		printf("%s\n", f(0, 1) ? "YES" : "NO");
	}
	
	return 0;
}
