# include <cstdio>
using namespace std;
int n;
char data[105][105];
double wp[105],owp[105],oowp[105];
int win[105],total[105];
int main()
{
	int test;
	scanf("%d",&test);
	for(int t=1;t<=test;t++)
	{
		scanf("%d",&n);
		for(int i=0;i<n;i++)
		{
			total[i]=0,win[i]=0;
			 scanf("%s",data[i]);
			for(int j=0;j<n;j++)
				  total[i]+=(data[i][j]!='.'),win[i]+=(data[i][j]=='1');
			wp[i]=(double)win[i]/total[i];
			owp[i]=oowp[i]=0;
		}
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<n;j++)
				if(data[i][j]=='1')
					owp[i]+=(win[j])/(total[j]-1.0);
				else if(data[i][j]=='0')
					owp[i]+=(win[j]-1.0)/(total[j]-1.0);
			owp[i]/=total[i];
		}
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<n;j++)
				oowp[i]+=(data[i][j]!='.'?owp[j]:0);
			oowp[i]/=total[i];
		}
		printf("Case #%d:\n",t);
		for(int i=0;i<n;i++)
			printf("%.10lf\n",0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
		
	}
	return 0;
}