#include <stdio.h>
#include <string>
#include <map>
using namespace std;
const int maxn = 200;
const int maxm = 1010;
const int infi = 1000000;
map <string, int> name;
string s;
char st[1000];
int n, m, i, j, k, t, ans, a[maxm];
int f[maxm][maxn];

void readln()
{
	gets(st);
}

void doit()
{
	memset(f, 0, sizeof(f));
	for (i=1;i<=m;++i)
		for (j=1;j<=n;++j)
		{
			f[i][j] = infi;
			if (a[i] == j)
				continue;
			for (k=1;k<=n;++k)
				if (f[i - 1][k] + (k != j) < f[i][j])
					f[i][j] = f[i - 1][k] + (k != j);
		}
	ans = infi;
	for (i=1;i<=n;++i)
		if (f[m][i] < ans)
			ans = f[m][i];
	printf("Case #%d: %d\n", t, ans);
			
}

void work()
{
	name.clear();
	scanf("%d", &n);
	readln();
	for (i=1;i<=n;++i)
	{
		gets(st);
		s = st;
		name[s] = i;
	}
	scanf("%d", &m);
	readln();
	for (i=1;i<=m;++i)
	{
		gets(st);
		s = st;
		a[i] = name[s];
	}
	doit();
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int test;
	scanf("%d", &test);
	for (t=1;t<=test;++t)
		work();
}
