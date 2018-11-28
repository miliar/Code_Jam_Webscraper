#include <iostream>
#include <cstring>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>

using namespace std;

const int maxn = 1050;

int p;
int a[maxn];
int f[11][maxn];

int ans[11][maxn][11];
int b[11][maxn][11];

void init()
{
	memset(a,0,sizeof(a));
	memset(f,0,sizeof(f));
	memset(ans, 0, sizeof(ans));
	memset(b, 0, sizeof(b));
	scanf("%d", &p);
	for (int i=0; i<(1<<p); i++)
	{
		scanf("%d",&a[i]);
		a[i] = p - a[i];
	}
	for (int i=0; i<p; i++)
		for (int j=0; j<(1<<(p-i-1)); j++)
			scanf("%d", &f[i][j]);
}

void calc(int k, int kk, int l)
{
	if (k==0)
	{
		if (a[kk*2]<=l && a[kk*2+1]<=l)
			ans[k][kk][l] = 0;
		else if (a[kk*2]<=l+1 && a[kk*2+1]<=l+1)
			ans[k][kk][l] = f[k][kk];
		else
			ans[k][kk][l] = -1;
		return;
	}
	if (b[k][kk][l] == 1)
		return;

	int best = -1;
	for (int i = 0; i<=l + 1; i++)
		for (int j = 0; j<=l + 1; j++)
		{
			int cur = 0;
			calc(k-1, kk*2, i);
			calc(k-1, kk*2+1, j);
			if (i==l+1 || j==l+1)
				cur += f[k][kk];
			if (ans[k-1][kk*2][i]>=0&&ans[k-1][kk*2+1][j]>=0)
			{
				cur += ans[k-1][kk*2][i]+ans[k-1][kk*2+1][j];
				if (cur<best || best == -1)
					best = cur;
			}
		}

	ans[k][kk][l] = best;
	b[k][kk][l] = 1;
}

int solve()
{
	calc(p-1, 0, 0);
	return ans[p-1][0][0];
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T = 0;
	scanf("%d", &T);
	for (int i=0; i<T; i++) {
		init();
		printf("Case #%d: %d\n", i+1, solve());
	}
}