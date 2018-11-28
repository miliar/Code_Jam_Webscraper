#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cmath>

using namespace std;

const int MAXN=10010;

int n,i,d[MAXN],l[MAXN],len,DAT;
bool f[MAXN][MAXN],flag;

void dfs(int now,int cat)
{
	if (f[now][cat]) return;
	if (min(d[cat]-d[now],l[cat])>=len-d[cat]) 
	{
		flag=true;
		return;
	}
	int c=min(d[cat]-d[now],l[cat]);
	for (int i=cat+1;i<=n;i++)
	{
		if (flag) return;
		if (d[i]-d[cat]>c) break;
		dfs(cat,i);
	}
	f[now][cat]=true;
}

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&DAT);
	for (int cas=1;cas<=DAT;cas++)
	{
		flag=false;
		printf("Case #%d: ",cas);
		scanf("%d",&n);
		for (i=1;i<=n;i++)
			scanf("%d%d",&d[i],&l[i]);
		scanf("%d",&len);
		memset(f,false,sizeof(f));
		dfs(0,1);
		if (flag) printf("YES\n");
		else printf("NO\n");
	}
	return 0;
}
