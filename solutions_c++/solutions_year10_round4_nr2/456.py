#include <stdio.h>
#include <cstring>
#include <algorithm>
using namespace std;
#define INF 0x3f3f3f3f

int f[5000][20], n, tot, w[5000], m[5000];
int vis[5000][20];

void init()
{
	tot = 1 << n;
	for(int i=tot; i<tot*2; ++i) scanf("%d", &m[i]);

	for(int i=n; i>=1; --i)
	{
		int x = 1 << (i - 1);
		for(int j=x; j<2*x; ++j) scanf("%d", &w[j]);
	}

	//for(int i=1; i<tot; ++i) printf("%d ", w[i]);
	//puts("");
}

int dp(int now, int pre)
{
	if(vis[now][pre] != -1) return f[now][pre];

	if(now >= tot)
	{
		if(n - pre > m[now]) return INF;
		else return 0;
	}

	int a = dp(now * 2, pre) + dp(now * 2 + 1, pre);
	int b = dp(now * 2, pre + 1) + dp(now * 2 + 1, pre + 1) + w[now];

	f[now][pre] = min(f[now][pre], min(a, b));
	vis[now][pre] = 1;

	return f[now][pre];
}

void solve()
{
	memset(f, 0x3f, sizeof f);
	memset(vis, -1, sizeof vis);

	int k = dp(1, 0);

	printf("%d\n", k);
}

int main()
{
	int t, tc = 0;
	scanf("%d", &t);
	while(t--)
	{
		scanf("%d", &n);
		init();
		printf("Case #%d: ", ++tc);
		solve();
	}
	return 0;
}

