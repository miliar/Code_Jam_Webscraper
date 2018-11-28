#include<stdio.h>
#include<string.h>
int sum[505][505];
int sumy[505][505];
char a[505][505];
char b[505][505];
bool yesx[505][505];
bool yesy[505][505];
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.out","w",stdout);

	int tt;
	scanf("%d",&tt);
	for(int t=1;t<=tt;t++)
	{
		int r,c,d;
		scanf("%d %d %d",&r,&c,&d);
		for(int i=0;i<c;i++) sum[0][i]=0;
		for(int i=0;i<r;i++)
		{
			scanf("%s",a[i]);
			for(int j=0;j<c;j++)
			{
				a[i][j]-='0';
				sum[i+1][j]=sum[i][j]+a[i][j];
			}
		}
		for(int i=0;i<r;i++) sumy[0][i]=0;
		for(int i=0;i<c;i++)
		{
			for(int j=0;j<r;j++)
			{
				b[i][j]=a[j][i];
				sumy[i+1][j]=sumy[i][j]+b[i][j];
			}
		}
				
		int k=r;
		if(k>c) k=c;
		bool yes=0;
		for(;k>=3;k--)
		{
//			printf("!%d\n",k);
			memset(yesx,0,sizeof(yesx));
			memset(yesy,0,sizeof(yesy));
			for(int i=0;i+k<=r;i++)
			{
				int ii=i+k;
				int dx=i*2+1;
				
				int mass=0;
				int mx=0;
				
				{
					mass+=(sum[i+k-1][0]-sum[i+1][0]);
					for(int j=1;j<k-1;j++)
						mass+=(sum[i+k][j]-sum[i][j]);
					mass+=(sum[i+k-1][k-1]-sum[i+1][k-1]);
					
					mx+=(sum[i+k-1][0]-sum[i+1][0])*1;
					for(int j=1;j<k-1;j++)
						mx+=(sum[i+k][j]-sum[i][j])*(j*2+1);
					mx+=(sum[i+k-1][k-1]-sum[i+1][k-1])*((k-1)*2+1);
				}
				
				for(int j=0;j+k<=c;j++)
				{
					int jj=j+k;
					int dy=j*2+k;
					
//					printf("(%d,%d,%d) ",mass,dy*mass,mx);
					if(dy*mass==mx) yesx[i][j]=1;
					
					mass-=(sum[i+k-1][j]-sum[i+1][j]);
					mass+=(sum[i+k-1][j+k]-sum[i+1][j+k]);
					mass-=a[i][j+1];
					mass-=a[i+k-1][j+1];
					mass+=a[i][j+k-1];
					mass+=a[i+k-1][j+k-1];

					mx-=(sum[i+k-1][j]-sum[i+1][j])*(j*2+1);
					mx+=(sum[i+k-1][j+k]-sum[i+1][j+k])*((j+k)*2+1);
					mx-=a[i][j+1]*((j+1)*2+1);
					mx-=a[i+k-1][j+1]*((j+1)*2+1);
					mx+=a[i][j+k-1]*((j+k-1)*2+1);
					mx+=a[i+k-1][j+k-1]*((j+k-1)*2+1);
				}
//				printf("\n");
			}
//			printf("\n");
			
			for(int i=0;i+k<=c;i++)
			{
				int ii=i+k;
				int dx=i*2+1;
				
				int mass=0;
				int mx=0;
				
				{
					mass+=(sumy[i+k-1][0]-sumy[i+1][0]);
					for(int j=1;j<k-1;j++)
						mass+=(sumy[i+k][j]-sumy[i][j]);
					mass+=(sumy[i+k-1][k-1]-sumy[i+1][k-1]);
					
					mx+=(sumy[i+k-1][0]-sumy[i+1][0])*1;
					for(int j=1;j<k-1;j++)
						mx+=(sumy[i+k][j]-sumy[i][j])*(j*2+1);
					mx+=(sumy[i+k-1][k-1]-sumy[i+1][k-1])*((k-1)*2+1);
				}
				
				for(int j=0;j+k<=r;j++)
				{
					int jj=j+k;
					int dy=j*2+k;
					
//					printf("(%d,%d,%d) ",mass,dy*mass,mx);
					if(dy*mass==mx) yesy[j][i]=1;
					
					mass-=(sumy[i+k-1][j]-sumy[i+1][j]);
					mass+=(sumy[i+k-1][j+k]-sumy[i+1][j+k]);
					mass-=b[i][j+1];
					mass-=b[i+k-1][j+1];
					mass+=b[i][j+k-1];
					mass+=b[i+k-1][j+k-1];

					mx-=(sumy[i+k-1][j]-sumy[i+1][j])*(j*2+1);
					mx+=(sumy[i+k-1][j+k]-sumy[i+1][j+k])*((j+k)*2+1);
					mx-=b[i][j+1]*((j+1)*2+1);
					mx-=b[i+k-1][j+1]*((j+1)*2+1);
					mx+=b[i][j+k-1]*((j+k-1)*2+1);
					mx+=b[i+k-1][j+k-1]*((j+k-1)*2+1);
				}
//				printf("\n");
			}
//			printf("\n");
			
			for(int i=0;i<r;i++)
			{
				for(int j=0;j<c;j++)
				{
//					printf("(%d,%d) ",yesx[i][j],yesy[i][j]);
					if(yesx[i][j]==1 && yesy[i][j]==1)
					{
						yes=1;
						break;
					}
				}
//				printf("\n");
				if(yes==1) break;
			}
//			printf("\n\n");
			if(yes==1) break;
		}
		
		printf("Case #%d: ",t);
		if(k<=2) printf("IMPOSSIBLE\n");
		else printf("%d\n",k);
	}

	return 0;
}
