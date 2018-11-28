/*
	Author : ChnLich
*/
#include<cstdio>
#include<cmath>
#include<iomanip>
#include<cstring>
#include<cstdlib>
#include<ctime>
#include<iostream>
#include<sstream>
#include<fstream>
#include<algorithm>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<deque>
#include<set>
#include<map>
#include<string>
#include<bitset>
#include<functional>
#include<utility>

using namespace std;

typedef long long llint;
typedef pair<int,int> ipair;
#define fi first
#define se second
#define mp make_pair

void read(int &k)
{
	k=0; char x=getchar();
	while(x<'0'||x>'9') x=getchar();
	while(x>='0'&&x<='9') { k=k*10-48+x; x=getchar(); }
}

int n,w,l,len;
ipair ans[2010],ps[2010],a[2010],lis[4010],b[2010];

bool sect(int x,int y)
{
	return abs(ps[x].fi-ps[y].fi)<a[x].fi+a[y].fi&&abs(ps[x].se-ps[y].se)<a[x].fi+a[y].fi;
}

bool dfs(int k)
{
	if (!k)
		return 1;
	for(int i=1;i<=len;i++)
	{
		if (lis[i].fi!=0) ps[k].fi=lis[i].fi+a[k].fi; else ps[k].fi=0;
		if (lis[i].se!=0) ps[k].se=lis[i].se+a[k].fi; else ps[k].se=0;
		if (ps[k].fi<=w&&ps[k].se<=l)
		{
			int ok=1;
			for(int j=k+1;j<=n&&ok;j++) if (sect(k,j)) ok=0;
			if (!ok) continue;
			lis[++len]=mp(lis[i].fi+2*a[k].fi,lis[i].se);
			lis[++len]=mp(lis[i].fi,lis[i].se+2*a[k].fi);
			if (dfs(k-1)) return 1;
			len-=2;
		}
	}
	return 0;
}

void doit()
{
	lis[len=1]=mp(0,0);
	dfs(n);
}

bool sectb(int x,int y)
{
	return abs(ans[x].fi-ans[y].fi)<b[x].fi+b[y].fi&&abs(ans[x].se-ans[y].se)<b[x].fi+b[y].fi;
}

bool check()
{
	for(int i=1;i<=n;i++) if (ans[i].fi>w||ans[i].se>l||ans[i].fi<0||ans[i].se<0) return 0;
	int ok=1;
	for(int i=1;i<=n&&ok;i++)
		for(int j=i+1;j<=n&&ok;j++)
			if (sectb(i,j)) ok=0;
	return ok;
}

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++)
	{
		scanf("%d%d%d",&n,&w,&l);
		for(int i=1;i<=n;i++) scanf("%d",&a[i].fi),a[i].se=i,b[i]=a[i];
		sort(a+1,a+n+1);
		doit();
		for(int i=1;i<=n;i++) ans[a[i].se]=ps[i];
		
		if (!check())
		{
			puts("Error!");
			while(1);
		}
		
		printf("Case #%d: ",tt);
		for(int i=1;i<=n;i++) printf("%d %d ",ans[i].fi,ans[i].se);
		puts("");
	}
	
	return 0;
}