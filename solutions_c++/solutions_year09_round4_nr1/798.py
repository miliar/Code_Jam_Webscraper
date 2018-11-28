#include <iostream>



using namespace std;

char dp[50][50];
int pailie[100];

int main()
{
	int t;
	int i,j;
	int oo=1;
	freopen("f.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		int n;
		int p=0;
		scanf("%d",&n);
		for(i=0;i<n;++i)
				scanf("%s",dp[i]);
		for(i=0;i<n;++i)
		{
			int max=0;
			for(j=0;j<n;++j)
				if(dp[i][j]=='1')
					max=j;
			pailie[i]=max+1;
		}
		int sum=0;
		for(i=0;i<n;++i)
		{
			if(pailie[i]>i+1)
			{
				for(j=i+1;j<n;++j)
				{
					if(pailie[j]<=i+1)
						break;
				}
				int hj=pailie[j];
				sum+=j-i;
				for(j=j;j>=i+1;--j)
				{
					pailie[j]=pailie[j-1];
				}
				pailie[i]=hj;
			}
		}
		printf("Case #%d: %d\n",oo++,sum);
	}
}