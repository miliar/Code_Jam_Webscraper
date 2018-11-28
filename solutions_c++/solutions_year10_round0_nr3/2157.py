#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
using namespace std;

int t,tt;
long long r,k,n,i;
long long g[2010];
long long sum[2010];
long long res;
int s,f,lt,rt,c,d;

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);

	scanf("%d",&tt);
	for (t=1; t<=tt; t++)
	{
		scanf("%I64d %I64d %I64d",&r,&k,&n);
		for (i=0; i<n; i++)
		{
			scanf("%I64d",&g[i]);
			g[n+i]=g[i];
		}
		printf("Case #%d: ",t);
		sum[0]=g[0]; 
		for (i=1; i<2*n; i++) 
			sum[i]=sum[i-1]+g[i];
		if (sum[n-1]<=k)
		{
			printf("%I64d\n",sum[n-1]*r);
			continue;
		}
		res=0;
		s=0; f=n-1;
		for (i=1; i<=r; i++)
		{
			if (s>0) d=sum[s-1];
			else	 d=0;
			lt=s; rt=f;
			while (rt-lt>1)
			{
				c=(rt+lt)/2;
				if (sum[c]-d<=k) lt=c;
				else			 rt=c;
			}
			res+=sum[lt]-d;
			s=(lt+1)%n;
			f=s+n-1;
		}
		printf("%I64d\n",res);
	}

    return 0;
}
