#include<iostream>
using namespace std;
int main()
{
	int i,t,k,r,j,n,ans;
	int lef,righ,base,mid,tmp;
	int g[3000];
	freopen("C-small-attempt1.in","r",stdin);
	freopen("C-small-attempt1.out","w",stdout);
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		scanf("%d%d%d",&r,&k,&n);
		for(j=1;j<=n;j++)
		{
			scanf("%d",&g[j]);
			g[n+j]=g[j];
		}
		g[0]=0;
		for(j=2;j<=2*n;j++)
			g[j]+=g[j-1];
		ans=0;
		lef=1;righ=n;base=0;
		while(r--)
		{
			tmp=g[base]+k;
			while(lef+1<righ)
			{
				mid=(lef+righ)/2;
				if(g[mid]<=tmp)lef=mid;
				else righ=mid;
			}
			if(g[righ]<=tmp)lef=righ;


			ans+=g[lef]-g[base];
			lef=lef+1;
			if(lef>n)lef-=n;
			righ=lef+n-1;
			base=lef-1;
		}
		printf("Case #%d: %d\n",i,ans);


	}
	return 0;
}