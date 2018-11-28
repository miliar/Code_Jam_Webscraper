
#include <stdio.h>
#include <math.h>
double binomial[100][100];


int main()
{
	
	
	for(int n=0;n<100;n++)
		for(int k=0;k<100;k++)
		{
			if(k==0)
			{
				binomial[n][k]=1;
				continue;
			}
			if(n==0)
			{
				binomial[n][k]=0;
				continue;
			}
			binomial[n][k]=binomial[n-1][k]+binomial[n-1][k-1];
				
		}
	
	int tc;
	scanf("%d",&tc);
	double answer[1000];
	for(int t=1;t<=tc;t++)
	{
		int N,C;
		scanf("%d %d",&C,&N);
		answer[C]=0;
		for(int k=C-1;k>=0;k--)
		{
			double summ=1;
			
			for(int i=1;i<=N;i++)
			{
				if(k>=N-i && C-k>=i)
				{
					summ+=(binomial[k][N-i]/binomial[C][N])*binomial[C-k][i]*answer[k+i];
				}
			}
			double denom=1;
			if(k>=N)
				denom-=binomial[k][N]/binomial[C][N];
			answer[k]=summ/denom;
			//printf("%lf\n",answer[k]);
			
		}
		
		printf("Case #%d: %1.9f\n",t,answer[0]);
		
		
	}
	
}