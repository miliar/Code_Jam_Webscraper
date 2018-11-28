#include <algorithm>
#include <cmath>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <vector>

using namespace std;

#define fore(i,a) for(int i = 0; i < (a); i++)
#define fort(i,a) for(typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define x first
#define y second

typedef pair<int,int> pi;
typedef vector<int> vi;
typedef long long ll;

#define err(...)
#define err(...) fprintf(stderr, __VA_ARGS__)

int c[111];
int g[111][111];
int t[111][33];
int dp[1<<17];
int good[1<<17];
int n,k;

void test()
{
	scanf("%d%d", &n, &k);
	fore(i,n) c[i] = 0;
	fore(i,n) fore(j,k) scanf("%d", &t[i][j]);
	fore(i,n) fore(j,n)
	{
		g[i][j] = 1;
		fore(q,k) if(t[i][q] == t[j][q]) g[i][j] = 0;
		fore(q,k-1) if(t[i][q] > t[j][q] != t[i][q+1] > t[j][q+1]) g[i][j] = 0;
	}
	fore(mask, (1<<n))
	{
		good[mask] = 1;
		if(mask == 0) continue;
		int pos = 0;
		fore(i,n) if(mask & (1<<i)) pos = i;
		good[mask] = good[mask ^ (1<<pos)];
		fore(i,pos) if(mask & (1<<i)) if(g[i][pos] == 0) good[mask] = 0;
	}
	fore(mask, (1<<n))
	{
		dp[mask] = __builtin_popcount(mask);
		for(int w = mask; w; w = (w-1)&mask) if(good[w])
		{
			dp[mask] = min(dp[mask], 1 + dp[mask ^ w]);
		}
	}
	printf("%d\n", dp[(1<<n)-1]);
}

int main()
{
	int T;
	scanf("%d", &T);
	for(int tt = 1; tt <= T; tt++)
	{
		printf("Case #%d: ", tt);
		test();
	}
}
