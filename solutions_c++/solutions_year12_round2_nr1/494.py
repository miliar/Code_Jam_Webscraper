#include <iostream>
#include <cstdio>
using namespace std;
int i,g,t,j,n,sum;
int a[10010];
double l,r,mid,cur,tmp;
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&t);
	for(g=1;g<=t;g++)
	{
		scanf("%d",&n);
		sum=0;
		for(i=1;i<=n;i++)
		{
			scanf("%d",&a[i]);
			sum+=a[i];
		}
		printf("Case #%d:",g);
		if(sum<1e-10)
			for(i=1;i<=n;i++) printf(" 0");
		else
		{
			for(i=1;i<=n;i++)
			{
				l=0; r=1; mid=(l+r)/2;
				while(r-l>1e-10)
				{
					cur=a[i]+mid*sum;
					tmp=mid;
					for(j=1;j<=n;j++)
						if(i!=j)
						{
							if(a[j]>=cur) continue;
							tmp+=((cur-a[j])/sum);
						}
					if(tmp>1) r=mid; else l=mid;
					mid=(l+r)/2;
				}
				printf(" %.8lf",mid*100);
			}
		}
		printf("\n");
	}
}
