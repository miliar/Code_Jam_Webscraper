#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctype.h>
#include <bitset>
#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
#include <queue>
#include <map>
#include <set>

using namespace std;

typedef long long ll;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef istringstream iss;
typedef ostringstream oss;

#define d2(x1, y1, x2, y2) (sqr((x1)-(x2)) + sqr((y1)-(y2)))
#define sqr(a) ((a)*(a))
#define ab(a) (((a)>0)?(a):(-(a))) 
#define cl(a, val) memset(a, val, sizeof(a))
#define deb(x) cout<<#x<<" = "<<(x)<<endl
#define FG(a, b) for((a) = (b); (a) >= 0; (a)--)
#define FD(a, b) for((a) = 0; (a) < (b); (a)++)
#define all(a) (a).begin(),(a).end() 
#define sz(a) int((a).size())
#define PB push_back
#define INF 0x3fffffff
#define Y second
#define X first

char in[] = "C-small-attempt0.in";
char out[] = "C-small-attempt0.out";

int n, m;

int main()
{
	freopen(in, "rt", stdin);
	freopen(out, "wt", stdout);

	int i, j, k, tt;
	int T, t;
	scanf("%d", &T);

	for(t = 1; t <= T; t++)
	{
		ll res = 0;
		ll x, y, z, n, m;
		scanf("%lld%lld%lld%lld%lld", &n, &m, &x, &y, &z);
		vi a(m);
		for(i = 0; i < m; i++) scanf("%d", &a[i]);

		vi seq;
		for(i = 0; i <= n - 1; i++)
		{
			seq.PB( a[i%m] );
			//printf("%d\n", seq.back());
			a[i%m] = (x * a[i%m] + y * (i + 1) ) % z;
		}
		vector<long> dp(n + 1, 1);
		for(i = 1; i < n; i++)
			for(j = 0; j < i; j++)
				if( seq[i] > seq[j] )
					dp[i] = (dp[i] + dp[j]) % 1000000007;

		for(i = 0; i < n; i++) res = (dp[i] + res) % 1000000007;
		printf("Case #%d: %d\n", t, res);
	}


	return 0;
}