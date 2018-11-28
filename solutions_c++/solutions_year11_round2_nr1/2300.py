#include<iostream>
#include<string>
int matryx[101][101];
long double owp[101];
long double oowp[101];
long double wp[101];
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.out","w",stdout);
	int i,j;
	int t,n,kil;
	cin>>t;
	string temp;
	for(int k=0;k<t;k++)
	{
		printf("Case #%d:\n",k+1);
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			cin>>temp;
			for(j=0;j<n;j++)
			{
				if(temp[j]=='1')
					matryx[i][j]=1;
				if(temp[j]=='0')
					matryx[i][j]=0;
				if(temp[j]=='.')
					matryx[i][j]=-1;
			}
		}
		for(i=0;i<n;i++)
		{
			wp[i]=0;
			kil=0;

			for(j=0;j<n;j++)
			{
				if(matryx[i][j]==1)
				{
					wp[i]++;
					kil++;
				}
				if(matryx[i][j]==0)
				{
					kil++;
				}
			}
			wp[i]/=kil;
		}
		long double o=0;
		int i1,kil1=0;
		for(i1=0;i1<n;i1++)
		{
			owp[i1]=0;
			kil1=0;
			for(i=0;i<n;i++)
			{
				o=0;
				kil=0;
				if(matryx[i1][i]!=-1)
				{
					kil=0;
					kil1++;
					for(j=0;j<n;j++)
					{
						if(j!=i1)
						{
							if(matryx[i][j]==1)
							{
								o++;
								kil++;
							}
							if(matryx[i][j]==0)
							{
								kil++;
							}
						}
					}
					
				}
				if(kil!=0)
					o/=(long double)kil;
				owp[i1]+=o;

			}
			owp[i1]/=(long double)kil1;

		}
		for(i=0;i<n;i++)
		{
			oowp[i]=0;
			kil=0;
			for(j=0;j<n;j++)
			{
				if(matryx[i][j]!=-1)
				{
					kil++;
					oowp[i]+=owp[j];
				}
			}
			oowp[i]/=(long double)kil;
		}
		for(i=0;i<n;i++)
		{
			long double rpi=0.25*wp[i]+0.5*owp[i]+0.25*oowp[i];
			printf("%.10llf\n",rpi);
			//cout<<rpi<<endl;
		}
	}
}