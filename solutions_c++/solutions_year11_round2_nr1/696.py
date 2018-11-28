#include<iostream>
#include<fstream>
#include<string>
#include<ctime>
using namespace std;
char mat[111][111];
double wp[111],owp[111],oowp[111];
double win_sum[111],sum[111];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t,i,j,k,m=1,n;cin>>t;
	while(t--)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++) scanf("%s",&mat[i]);
		memset(owp,0,sizeof(owp));
		memset(win_sum,0,sizeof(win_sum));
		memset(sum,0,sizeof(sum));
		memset(win_sum,0,sizeof(win_sum));
		memset(oowp,0,sizeof(oowp));
		for(i=0;i<n;i++)
		{
			for(j=0;j<n;j++)
				if(mat[i][j]!='.')
				{
					if(mat[i][j]=='1') win_sum[i]+=1;
					sum[i]+=1;
				}
			wp[i]=win_sum[i]/sum[i];
		}
		for(i=0;i<n;i++)
		{
			for(j=0;j<n;j++)
				if(mat[i][j]!='.')
				{
					if(mat[i][j]=='0') owp[i]+=(win_sum[j]-1)/(sum[j]-1);
					else owp[i]+=(win_sum[j])/(sum[j]-1);
				}
			owp[i]/=sum[i];
		}
		for(i=0;i<n;i++)
		{
			for(j=0;j<n;j++)
				if(mat[i][j]!='.')
					oowp[i]+=owp[j];
			oowp[i]/=sum[i];
		}
		printf("Case #%d:\n",m++);
		for(i=0;i<n;i++)
		{
			//printf("%.6lf\n",owp[i]);
			printf("%.6lf\n",0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
		}
	}
}