#include<iostream>
#include<math.h>
#include<algorithm>
using namespace std;
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,g=0,j,k,r,a,b,c;
	int d,i,m,n,arr[10],dp[50][500];
	scanf("%d",&t);
	while(t--)
	{
		g++;
		scanf("%d %d %d %d",&d,&i,&m,&n);
		for(j=0;j<n;j++)scanf("%d",&arr[j]);
		printf("Case #%d: ",g);
		if(n==1)
		{
			printf("0\n");
			continue;
		}
		for(j=0;j<n;j++)
		{
			for(k=0;k<256;k++)
			{
				dp[j][k]=abs(arr[j]-k)+j*d;
			}
		}
		for(j=1;j<n;j++)
		{
			for(k=j-1;k>=0;k--)
			{
				for(r=0;r<256;r++)
				{
					c=abs(r-arr[j]);
					for(int rr=0;rr<256;rr++)
					{
						a=abs(rr-r);
						if(m==0&&r!=rr)continue;
						if(a<=m||m==0)
						{
							dp[j][r]=min(dp[j][r],dp[k][rr]+(j-k-1)*d+c);
						}
						else
						{
							b=a-m;
							if(b%m==0)
							{
								b=min(b,i*b/m);
							}
							else b=min(b,i*(b/m+1));
							dp[j][r]=min(dp[j][r],dp[k][rr]+b+(j-k-1)*d+c);

						}
					}
				}
			}

		}
		int ans=dp[n-1][0];
		for(i=1;i<256;i++)ans=min(ans,dp[n-1][i]);
		printf("%d\n",ans);
	}
	return 0;
}