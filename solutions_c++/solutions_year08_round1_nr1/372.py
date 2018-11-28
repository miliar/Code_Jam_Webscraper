/*
 * ¶þ·ÖÍ¼×î¼ÑÆ¥Åä
 */
#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
const int maxn = 1000;
const long long infi = 210000000000000000LL;
int n, i, j, k, t, test;
long long w[maxn][maxn], lx[maxn], ly[maxn], ans, d;
int link[maxn];
bool vx[maxn], vy[maxn];
long long a[maxn], b[maxn];

bool find(int x)
{
	vx[x] = true;
	for (int i=1; i<=n; i++)
		if ((!vy[i]) && (lx[x] + ly[i] == w[x][i]))
		{
			vy[i] = true;
			if (link[i] == 0 || (find(link[i])))
			{
				link[i] = x;
				return true;
			}
		}
	return false;
}

void work()
{
	scanf("%d", &n);
	for (i=1;i<=n;++i)
		scanf("%I64d", &a[i]);
	for (i=1;i<=n;++i)
		scanf("%I64d", &b[i]);
	ans = 0;
	for (i=1;i<=n;i++)
		for (j=1;j<=n;j++)
			w[i][j] = -a[i] * b[j];
	for (i=1;i<=n;++i)
		lx[i] = -infi;
	memset(lx, 0, sizeof(lx));
	memset(ly, 0, sizeof(ly));
	memset(link, 0, sizeof(link));
	for (i=1;i<=n;i++)
		for (j=1;j<=n;j++)
			if (w[i][j] > lx[i])
				lx[i] = w[i][j];
	for (k=1;k<=n;k++)
		while (true)
		{
			memset(vx, 0, sizeof(vx));
			memset(vy, 0, sizeof(vy));
			if (find(k)) break;
			d = infi;
			for (i=1;i<=n;i++)
				if (vx[i])
					for (j=1;j<=n;j++)
						if ((!vy[j]) && (lx[i] + ly[j] - w[i][j] < d))
							d = lx[i] + ly[j] - w[i][j];
			for (i=1;i<=n;i++)
				if (vx[i])
					lx[i] -= d;
			for (i=1;i<=n;i++)
				if (vy[i])
					ly[i] += d;
		}
	ans = 0;
	for (i=1;i<=n;++i)
		ans += w[link[i]][i];
	printf("Case #%d: %I64d\n", t, -ans);
}

void paixu()
{
	scanf("%d", &n);
	for (i=1;i<=n;++i)
		scanf("%I64d", &a[i]);
	for (i=1;i<=n;++i)
		scanf("%I64d", &b[i]);
	sort(a + 1, a + n + 1);
	sort(b + 1, b + n + 1);
	ans = 0;
	for (i=1;i<=n;++i)
		ans += a[i] * b[n - i + 1];
	printf("Case #%d: %I64d\n", t, ans);
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d", &test);
	for (t=1;t<=test;++t)
	{
		paixu();
		//work();
	}
}
