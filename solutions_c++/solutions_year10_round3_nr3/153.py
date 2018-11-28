#include <iostream>
using namespace std;
bool map[40][40];
bool visit[40][40];
int ans[100];
int main ()
{
	int T;
	int a;
	int t,all,allnum,i,j,ii,jj,m,n,mm,flag,k;
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		all=0;
		memset(visit,0,sizeof(visit));
		memset(ans,0,sizeof(ans));
		scanf("%d%d",&m,&n);
		for(i=0;i<m;i++)
		{
			scanf("%x",&a);
			for(j=n-1;j>=0;j--)
			{
				map[i][j]=a%2;
				a/=2;
			}
		}
		for(i=0;i<m;i++)
		{
			for(j=0;j<n;j++)
			{
				if(visit[i][j]==1)continue;
				mm=j+1;
				while(map[i][mm]!=map[i][mm-1]&&mm<n)mm++;
				m=mm-j;
				flag=0;
				for(k=mm;k>=1;k--)
				{
					for(ii=i+1;ii<i+mm;ii++)
					{
						for(jj=j;jj<j+mm;jj++)
						{
							if(map[ii][jj]==map[ii-1][jj])flag=1;
							if(jj>j&&map[ii][jj]==map[ii][jj-1])flag=1;
							if(flag==1)break;
						}
						if(flag)break;
					}
					if(flag==0)
					{
						for(ii=i+1;ii<i+mm;ii++)
						{
							for(jj=j;jj<j+mm;jj++)
							{
								visit[ii][jj]=1;
							}
						}
					}
					all+=mm*mm;
					ans[m]++;
				}
			}
		}
		allnum=0;
		for(i=1;i<=32;i++)if(ans[i]!=0)allnum++;
		printf("Case #%d: %d\n",t,allnum);
		for(i=1;i<=32;i++)
		{
			if(ans[i]!=0)
			{
				printf("%d %d\n",i,ans[i]);
			}
		}
	}
}