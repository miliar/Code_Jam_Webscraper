#include <iostream>
#define M 1010
using namespace std;
int h[M];
long long pto[M];
long long sumh[M];
int main()
{	
	int T,r,k,n,cases=0;
	freopen("D:\\C-large.in","r",stdin);
	freopen("D:\\C-large.out","w",stdout);
	scanf("%d",&T);
	while (T--)
	{
		memset(pto,0,sizeof(pto));
		memset(sumh,0,sizeof(sumh));
		int i,j;
		scanf("%d%d%d",&r,&k,&n);
		for (i=0;i<n;i++) 
			scanf("%d",&h[i]);
		for (i=0;i<n;i++)
		{
			j=i;
			int cnt=0;
			long long sum=0;
			while (1)
			{
				cnt++;
				if (sum+h[j]<=k)
					sum+=h[j];
				else 
				{
					pto[i]=j;
					sumh[i]=sum;
					break;
				}
				j++;
				if (j==n) j=0;
				if (cnt==n) 
				{
					pto[i]=j;
					sumh[i]=sum;
					break;
				}
			}
		}
		int pos=0;
		long long ans=0;
		while (r--)
		{
			ans+=sumh[pos];
			pos=pto[pos];
			if (pos==n) pos=0;
		}
		printf("Case #%d: %lld\n",++cases,ans);
	}
	return 0;
}

