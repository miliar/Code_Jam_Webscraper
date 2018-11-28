#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<algorithm>

using namespace std;

const int MAXN=10010;

int n,D;
struct IN
{
	int d;
	int l;
}s[MAXN];
int res[MAXN];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t,cas;
	scanf("%d",&t);
	for(cas=1;cas<=t;cas++)
	{
		scanf("%d",&n);
		int i,j;
		s[0].d=s[0].l=0;
		for(i=1;i<=n;i++)
		scanf("%d%d",&s[i].d,&s[i].l);
		scanf("%d",&D);
		memset(res,-1,sizeof(res));
		res[1]=0;
		int last=2;
		for(i=1;i<=n && last<=n;i++)
		{
			if(res[i]==-1) break;
			if(s[i].d-s[res[i]].d>=s[i].l) j=s[i].d+s[i].l;
			else j=s[i].d+s[i].d-s[res[i]].d;
			while(s[last].d<=j && last<=n) res[last++]=i;
		}
		int fast=0;
		for(i=1;i<=n;i++)
		{
			if(res[i]==-1) break;
			if(s[i].d-s[res[i]].d>=s[i].l) j=s[i].d+s[i].l;
			else j=s[i].d+s[i].d-s[res[i]].d;
			if(j>fast) fast=j;
		}
		printf("Case #%d: ",cas);
		if(fast>=D) printf("YES\n");
		else printf("NO\n");
	}
	return 0;
}
