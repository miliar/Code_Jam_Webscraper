#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<memory.h>
#include <string>
using namespace std;
struct press
{
  string ob;
  int d;
};
press a[1005];
int next[1005];
int o,b,oo,bb,preb,preo,nexto,nextb,foo,fbb;
int main()
{
	int tcase,cas,n,i,j,ans;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	cin>>tcase;
	for(cas=1;cas<=tcase;cas++)
	{
		cin>>n;
		for(i=1;i<=n;i++)
		{
			cin>>a[i].ob>>a[i].d;
		}
		memset(next,0,sizeof(next));	
		for(i=1;i<=n;i++)
			{
				for(j=i+1;j<=n;j++)
					if (a[j].ob==a[i].ob)
					{
						next[i]=j;
					   break;
					}
			}
		ans=0;
		a[0].d=0;
		o=1;b=1;oo=bb=0;
		foo=fbb=0;
		for(i=1;i<=n;i++)
			if (a[i].ob=="O") {foo=i;break;}
        for(i=1;i<=n;i++)
			if (a[i].ob=="B") {fbb=i;break;}
		for(i=1;i<=n;i++)
		{
			if (oo==0)
			{
				preo=1;
				nexto=a[foo].d;
			}
			else
			{
				preo=a[oo].d;
				nexto=a[next[oo]].d;
			}
			if (bb==0)
			{
				preb=1;
			    nextb=a[fbb].d;
			}
				else
			{
				preb=a[bb].d;
				nextb=a[next[bb]].d;
			}
		if (a[i].ob=="O")
			{
				int d=abs(a[i].d-o)+1;
                ans+=d;
				oo=i;
				o=a[i].d;
				if (abs(nextb-b)<=d)
				{
					b=nextb;
				}
				else
				{
                   if (nextb>b) b+=d;
				   else b-=d;
				}
			}
			if (a[i].ob=="B")
			{
				int d=abs(a[i].d-b)+1;
                ans+=d;
				bb=i;
				b=a[i].d;
				if (abs(nexto-o)<=d)
				{
					o=nexto;
				}
				else
				{
                   if (nexto>o) o+=d;
				   else o-=d;
				}
			}
		}
		printf("Case #%d: %d\n",cas,ans);
	}
}