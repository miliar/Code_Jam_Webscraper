#include<iostream>
#include<cmath>
#include<string>
using namespace std;

char mp[105][105];
double wp[105],owp[105],oowp[105];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
//	freopen("1.txt","r",stdin);
	int T,n;
	cin>>T;
	for(int cas=1;cas<=T;cas++)
	{
		cin>>n;
		for(int i=1;i<=n;i++)for(int j=1;j<=n;j++)
			cin>>mp[i][j];

		for(int k=1;k<=n;k++)
		{
			int one = 0;
			int zero = 0;
			for(int j=1;j<=n;j++)
			{
				if(mp[k][j]=='1') one++;
				else if(mp[k][j]=='0') zero++;
			}
			wp[k]=1.0*one/(one+zero);
		}
		
		for(int k=1;k<=n;k++)
		{
			owp[k]=0;
			int num = 0;
			for(int i=1;i<=n;i++)
			{
				if(mp[k][i]!='.')
				{
					num++;
					int one = 0;
					int zero = 0;
					for(int j=1;j<=n;j++)
					{
						if(j!=k&&mp[i][j]=='1') one++;
						if(j!=k&&mp[i][j]=='0') zero++;
					}
					owp[k]+=1.0*one/(one+zero);
				}
			}
			owp[k]/=num;
		}

		for(int i=1;i<=n;i++)
		{
			oowp[i]=0;
			int num = 0;
			for(int j=1;j<=n;j++)
			{
				if(mp[i][j]!='.')
				{
					num++;
					oowp[i]+=owp[j];
				}
			}
			oowp[i]/=num;
		}
		
		cout<<"Case #"<<cas<<":\n";
		for(int i=1;i<=n;i++)
		{
			cout<<0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]<<'\n';
		}
	}
	return 0;
}