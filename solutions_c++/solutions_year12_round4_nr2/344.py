#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;
#define sqr(x) ((x)*(x))
typedef long long LL;

struct cor{ LL x,y; } a[101000],aa[101000];
struct ss{ LL r;int cod; }r[101000];
int T,CASES,n,W,L;

bool cmp(ss a,ss b ){ return a.r>b.r; }

bool chk(int x)
{
	for (int i=1;i<x;i++)
	{
		if ((sqr(a[x].x-a[i].x)+sqr(a[x].y-a[i].y))<sqr(r[x].r+r[i].r)) return false;
	}
	return true;
}

int main()
{
	freopen("b.in","r",stdin);freopen("b.out","w",stdout);
	
	for (scanf("%d",&T);T;T--)
	{
		scanf("%d%d%d",&n,&W,&L);
		for (int i=1;i<=n;i++) scanf("%d",&r[i].r),r[i].cod=i;
		sort(&r[1],&r[n+1],cmp);
		for (int i=2;i<=n;i++)
		{
			do { a[i].x=(LL(rand())*rand())%(W+1);a[i].y=(LL(rand())*rand())%(L+1); } while (!chk(i));
		}
		for (int i=1;i<=n;i++) aa[r[i].cod]=a[i];
		printf("Case #%d:",++CASES);
		for (int i=1;i<=n;i++) printf(" %I64d.0 %I64d.0",aa[i].x,aa[i].y);
		printf("\n");
	}
	
	return 0;
}