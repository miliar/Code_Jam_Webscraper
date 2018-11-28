#include<cstdio>
#include<algorithm>
#define INF 0x7fffffff
using namespace std;
int n,value;
int f[20000][2];
int gate[20000];
int v[20000];
int change[20000];
void DFS(int now)
{
	if (now * 2 > n)
	{
		f[now][v[now]] = 0;
		return;
	}
	int left = now * 2, right = now * 2 + 1;
	DFS(left);
	DFS(right);
	if (gate[now] == 0)
	{
		if (f[left][0] != INF && f[right][0] != INF) f[now][0] <?= f[left][0] + f[right][0];
		if (f[left][0] != INF && f[right][1] != INF) f[now][1] <?= f[left][0] + f[right][1]; 
		if (f[left][1] != INF && f[right][1] != INF) f[now][1] <?= f[left][1] + f[right][1];
		if (f[left][1] != INF && f[right][0] != INF) f[now][1] <?= f[left][1] + f[right][0];
	}
	else
	{
		if (f[left][1] != INF && f[right][1] != INF) f[now][1] <?= f[left][1] + f[right][1];
		if (f[left][0] != INF && f[right][1] != INF) f[now][0] <?= f[left][0] + f[right][1]; 
		if (f[left][0] != INF && f[right][0] != INF) f[now][0] <?= f[left][0] + f[right][0];
		if (f[left][1] != INF && f[right][0] != INF) f[now][0] <?= f[left][1] + f[right][0];
	}
	if (change[now] == 1)
	{
		if (gate[now] == 1)
		{
			if (f[left][0] != INF && f[right][0] != INF) f[now][0] <?= f[left][0] + f[right][0] + 1;
			if (f[left][0] != INF && f[right][1] != INF) f[now][1] <?= f[left][0] + f[right][1] + 1; 
			if (f[left][1] != INF && f[right][1] != INF) f[now][1] <?= f[left][1] + f[right][1] + 1;
			if (f[left][1] != INF && f[right][0] != INF) f[now][1] <?= f[left][1] + f[right][0] + 1;
		}
		else
		{
			if (f[left][1] != INF && f[right][1] != INF) f[now][1] <?= f[left][1] + f[right][1] + 1;
			if (f[left][0] != INF && f[right][1] != INF) f[now][0] <?= f[left][0] + f[right][1] + 1; 
			if (f[left][0] != INF && f[right][0] != INF) f[now][0] <?= f[left][0] + f[right][0] + 1;
			if (f[left][1] != INF && f[right][0] != INF) f[now][0] <?= f[left][1] + f[right][0] + 1;
		}
	}
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int cases;
	scanf("%d",&cases);
	for (int ca = 1; ca <= cases; ++ca)
	{
		scanf("%d%d",&n,&value);
		for (int i = 1;  i <= (n - 1) / 2; ++i)
			scanf("%d%d",&gate[i],&change[i]);
		for (int i = (n - 1) / 2 + 1; i <= n; ++i)
			scanf("%d",v + i);
		for (int i = 1; i <= n; ++i) f[i][0] = f[i][1] = INF;
		DFS(1);
		printf("Case #%d: ",ca);
		if  (f[1][value] == INF) puts("IMPOSSIBLE"); else printf("%d\n",f[1][value]);
	}
}
