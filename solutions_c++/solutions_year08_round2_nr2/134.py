#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cmath>
using namespace std;
int c,a,b,p,primes[1001],pn,i,j,k,l,usd[1001],ans;
bool good[1001][1001],pr,yes;
double g;
int dfs(int x)
{
	int v;
	usd[x]=ans;
	for(v=a;v<b+1;v++)
	{
		if ((usd[v]==0)&&(good[v][x]))
		{
			dfs(v);
		}
	}
	return(0);
}
int main()
{
	freopen("b-small.in","r",stdin);
	freopen("b-small.out","w",stdout);
	primes[0]=2;
	pn=1;
	for(i=3;i<1001;i++)
	{
		pr=true;
		g=i;
		g=sqrt(g);
		for(j=2;j<=g;j++)
		{
			if ((i%j)==0) {pr=false;}
		}
		if (pr)
		{
			primes[pn]=i;
			pn++;
		}
	}
	scanf("%d\n",&c);
	for(j=1;j<=c;j++)
	{
		scanf("%d%d%d",&a,&b,&p);
		for(i=a;i<b;i++)
		{
			for(k=a+1;k<b+1;k++)
			{
				yes=false;
				for(l=0;l<pn;l++)
				{
					if (((i%primes[l])==0)&&((k%primes[l])==0)&&(primes[l]>=p))
					{
						yes=true;
					}
				}
				if (yes) {good[i][k]=true;good[k][i]=true;} else {good[i][k]=false;good[k][i]=false;}
			}
		}
		for(i=a;i<b+1;i++) {usd[i]=0;good[i][i]==false;}
		i=a;
		ans=0;	
		while(i<b+1)
		{
			while(usd[i]!=0) {i++;}
			if (i<b+1)
			{
				ans++;
				dfs(i);
			}
		}
		printf("Case #%d: %d\n",j,ans);
	}
	return 0;
}