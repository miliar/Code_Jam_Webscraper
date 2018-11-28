#include <stdio.h>
#include <string.h>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int _cn,_cc,i,j,k,kk,idx,n;
	long long h[2048];
	int q[2048];
	long long a,b;
	scanf("%d",&_cn);
	for (_cc=1;_cc<=_cn;++_cc)
	{
		scanf("%d",&n);
		for (i=0;i<n-1;++i) scanf("%d",q+i);
		for (i=0;i<n;++i) h[i]=0;
		while (1)
		{
		kk=0;
		for (i=0;i<n-1;++i) 
		{
			for (j=i;j>=0;--j)
			{
				a=-10000000000LL;
				b=1;
				idx=0;
				for (k=j+1;k<n;++k)
				{
					if ((h[k]-h[j])*b>(k-j)*a)
					{
						a=h[k]-h[j];
						b=k-j;
						idx=k;
					}
				}
				if (idx!=q[j]-1)
				{
					++kk;
					a=a*(q[j]-1-j);
					if ((a%b)==0)
					{
						if (idx>q[j]-1) a=a/b; else a=(a/b)+1;
					} else
					{
						a=(a+b-1)/b;
					}
					h[q[j]-1]=h[j]+a;
					if (h[q[j]-1]>1000000000) break;
				}
			}
			if (j>=0) break;
		}
		if (i!=n-1) break;
		if (kk==0) break;
		}
		if (i==n-1)
		{
			for (i=0;i<n-1;++i) 
			{
				a=-10000000000LL;
				b=1;
				idx=0;
				for (k=i+1;k<n;++k)
				{
					if ((h[k]-h[i])*b>(k-i)*a)
					{
						a=h[k]-h[i];
						b=k-i;
						idx=k;
					}
				}
				if (idx!=q[i]-1) break;
			}
		}
		if (i<n-1)
		{
			printf("Case #%d: Impossible\n",_cc);
		} else
		{
			printf("Case #%d: ",_cc);
			for (i=0;i<n;++i) printf("%lld ",h[i]);
			printf("\n");
		}
	}
	return 0;
}
