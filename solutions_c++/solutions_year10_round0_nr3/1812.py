#include<cstdio>
#define NM 1005
#define LL unsigned long long
LL euro,s[NM];
int v[NM],R,N,K;
short int incep;
int caut(int x)
{
	int p,u,m;
	p=incep;
	u=N;
	while(p!=u)//cat timp intervalul in care caut are mai mult de un element
	{
		m=(p+u)>>1;
		if((LL)x<=s[m]-s[incep-1])
			u=m;
		else
			p=m+1;
	}
	if(s[p]-s[incep-1]>(LL)x)
		return p-1;
	return p;
}
void solve()
{
	incep=1;
	short int poz,poz1;
	int ramas;
	while (R--)
	{
		poz=caut(K);
		if (poz==N)
			if (s[poz]-s[incep-1]<(LL)K)
			{
				euro+=s[poz]-s[incep-1];
				ramas=K-s[poz]+s[incep-1];
				if (s[1]<=K-s[poz]+s[incep-1])
				{
					incep=1;
					poz1=caut(ramas);
				}
				else
				{
					incep=1;
					poz1=0;
				}
				if (poz1<poz)
				{
					euro+=s[poz1];
					incep=poz1+1;
					
				}
				else
				{
					euro+=s[poz-1];
					incep=poz;
					
				}
			}
			else
			{
				euro+=s[poz]-s[incep-1];
				incep=1;
			}
		else
		{
			euro+=s[poz]-s[incep-1];
			incep=poz+1;
			
		}
	}
}
int main()
{
	freopen("park.in","r",stdin);
	freopen("park.out","w",stdout);
	short int t,test=0;
	scanf("%hd",&t);
	while (t--)
	{
		++test;
		scanf("%d%d%d",&R,&K,&N);
		for (int i=1; i<=N; ++i)
		{
			scanf("%d",&v[i]);
			s[i]=s[i-1]+(LL)v[i];
		}
		if (s[N]<=(LL)K)
		{
			printf("Case #%hd: %llu\n",test,(LL)s[N]*R);
			continue;
		}
		euro=0;
		solve();
		printf("Case #%hd: %llu\n",test,euro);
	}
	return 0;
}
