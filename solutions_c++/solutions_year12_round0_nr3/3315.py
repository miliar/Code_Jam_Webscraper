#include<cstdio>
#include <cstring>
int ok[2000009];

int rotate(int x,int nr)
{
	x=x/nr+(x%nr)*10;
	return x;
}

int main()
{
	int tt,t,A,B,i,j,nr,cif,x;
	
	freopen("r.in","r",stdin);
	freopen("w.out","w",stdout);
	scanf("%d",&t);
	for (tt=1;tt<=t;++tt)
	{
		scanf("%d %d",&A,&B);
		memset(ok,0,sizeof(ok));
		long long sol=0;
		i=A/10;nr=1;cif=1;
		while (i)
			nr*=10,i/=10,++cif;
		for (i=A;i<B;++i)
		{
			for (x=rotate(i,nr),j=1;j<cif;++j,x=rotate(x,nr))
				if ((x>i) && (x<=B) && (ok[x]!=i))
					{++sol;
				     ok[x]=i;
				     //printf("%d - %d\n",i,x);
					}
		}
		printf("Case #%d: %lld\n",tt,sol);
	}
return 0;

}			