#include<cstdio>
int t,n,s,p,nsol,npl,x,xbkp,xmod;
int main()
{
	freopen("googledance.in","r",stdin);
	freopen("googledance.out","w",stdout);
	scanf("%d",&t);
	int i;
	for(int test=1;test<=t;++test)
	{
		nsol=0; npl=0;
		scanf("%d%d%d",&n,&s,&p);
		for(i=1;i<=n;++i)
		{
			scanf("%d",&x);
			xbkp=x;
			xmod=x%3; 
			if(xmod==2)
				xmod=-1;
			x=x-xmod;
			x/=3;
			if(x>=p)
				nsol++;
			else if((x==p-1)&&(xmod!=1)&&(npl<s)&&(xbkp>=2)&&(xbkp<=28))
				npl++;
			else if((x==p-1)&&(xmod==1))
				nsol++;
		}
		nsol=nsol+npl;
		printf("Case #%d: %d\n",test,nsol);
	}
	return 0;
}