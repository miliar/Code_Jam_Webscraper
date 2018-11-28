#include <stdio.h>
#include <string.h>
const int maxn = 300;
struct arr
{
	int st, ed;
} a[200], b[200];
int t, T, n, na, nb, link[maxn], i, j, ans;
bool v[maxn], g[maxn][maxn];

void gettime(arr &p)
{
	int x, y;
	scanf("%d:%d", &x, &y);
	p.st = x * 60 + y;
	scanf("%d:%d", &x, &y);
	p.ed = x * 60 + y;
}

bool find(int x)
{
	for (int i=1; i<=n; i++)
		if ((!v[i]) && (g[x][i]))
		{
			v[i] = true;
			if (link[i] == 0 || (find(link[i])))
			{
				link[i] = x;
				return true;
			}
		}
	return false;
}

void doit()
{
	n = na + nb;
	memset(link, 0, sizeof(link));
	ans = 0;
	for (i=1;i<=n;++i)
	{
		memset(v, 0, sizeof(v));
		if (find(i))
			++ans;
	}
	ans = n - ans;
	int ansa = 0;
	for (i=1;i<=na;++i)
		if (link[i] == 0)
			++ansa;
	printf("Case #%d: %d %d\n", t, ansa, ans - ansa);
}

void add(int a, int b)
{
	g[a][b] = true;
}

void work()
{
	scanf("%d", &T);
	scanf("%d%d", &na, &nb);
	for (i=1;i<=na;++i)
		gettime(a[i]);
	for (i=1;i<=nb;++i)
		gettime(b[i]);
	memset(g, 0, sizeof(g));
	for (i=1;i<=na;++i)
		for (j=1;j<=nb;++j)
		{
			if (a[i].ed + T <= b[j].st)
				add(i, na + j);
			if (b[j].ed + T <= a[i].st)
				add(na + j, i);
		}
	doit();
}

int main()
{
	freopen("i.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int test;
	scanf("%d", &test);
	for (t=1;t<=test;++t)
		work();
}
