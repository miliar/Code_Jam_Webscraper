#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;
const int MAXN=109;
struct oper
{
	int pos,order;
}	b[MAXN],o[MAXN];
int T,n,lo,lb,ans;

void init()
{
	scanf("%d",&n);	lo=lb=0;
	for (int i=1;i<=n;i++)
	{
		char s[3];	int p;
		scanf("%s %d",s,&p);
		if (s[0]=='O') { o[++lo].pos=p;	o[lo].order=i;}
		else			{ b[++lb].pos=p;	b[lb].order=i;}
	}
}

void work()
{
	int po=1,pb=1,qo=1,qb=1;
	ans=0;	o[lo+1].order=b[lb+1].order=n+1;
	for (int i=1;i<=n;i++)
		if (o[qo].order>b[qb].order)
		{
			int ti=abs(b[qb].pos-pb)+1;
			ans+=ti;		pb=b[qb++].pos;
			if (abs(o[qo].pos-po)<=ti)	po=o[qo].pos;
				else	if (o[qo].pos>po) po+=ti;	else po-=ti;
		}
		else
		{
			int ti=abs(o[qo].pos-po)+1;
			ans+=ti;		po=o[qo++].pos;
			if (abs(b[qb].pos-pb)<=ti) pb=b[qb].pos;
				else	if (b[qb].pos>pb) pb+=ti;	else pb-=ti;
		}
}
			
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("a_l.out","w",stdout);
	scanf("%d",&T);
	for (int t=1;t<=T;t++)
	{
		init();
		work();
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}
