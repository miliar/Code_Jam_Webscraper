#include<algorithm>
using namespace std;
int p[201],v[201];
double aabs(double a)
{
	return a<0?-a:a;
}
int main()
{
	bool fg;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int c,d,i,j,k,l,t,tt,n,pp,cn,dn,nm;
	double ans,tti,ppl;
	__int64 pl,low,up,ti;
	scanf("%d",&t);
	for(tt=1;tt<=t;tt++)
	{
		scanf("%d%d",&c,&d);
		for(i=0;i<c;i++)
			scanf("%d %d",&p[i],&v[i]);
		low=0;up=1000000;
		up*=1000000+100001;
		while(low<up)
		{
			ti=(low+up)/2;
			pl=p[0]-ti;
			for(i=0;i<c;i++)
				for(j=0;j<v[i];j++)
				{
					if(pl<p[i]-ti)pl=p[i]-ti+d;
					else if(pl>p[i]+ti)goto loop;
					else pl+=d;
				}
loop:		if(i==c)up=ti;
			else low=ti+1;
		}
		for(tti=up+2;tti>up-3;tti-=0.5)
		{
			nm=tti+0.001;
			if(aabs(nm-tti)<0.1)tti=nm;
			ppl=p[0]-tti;
			for(i=0;i<c;i++)
				for(j=0;j<v[i];j++)
				{
					if(ppl<p[i]-tti)ppl=p[i]-tti+d;
					else if(ppl>p[i]+tti&&aabs(ppl-p[i]-tti)>0.0001)goto loop2;
					else ppl+=d;
				}
loop2:		if(i==c)ans=tti;
		}
		printf("Case #%d: %f\n",tt,ans);
	}
	return 0;
}
