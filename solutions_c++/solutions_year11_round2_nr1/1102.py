#include <iostream>
using namespace std;
char match[101][101];
double wp[101];
double owp[101];
double oowp[101];
double awp[101];
int main()
{
	int t,n;
	cin>>t;
	for (int i=1;i<=t;i++)
	{
		memset(match,0,sizeof(match));
		memset(wp,0,sizeof(wp));
		memset(owp,0,sizeof(owp));
		memset(oowp,0,sizeof(oowp));
		memset(awp,0,sizeof(awp));
		cin>>n;
		for (int j=0;j<n;j++)
			cin>>match[j];
		for (int j=0;j<n;j++)
		{
			int cnt=0;
			int wincnt=0;
			for (int k=0;k<n;k++)
			{
				if (match[j][k]=='.')
					continue;
				if (match[j][k]=='1')
					wincnt++;
				cnt++;
			}
			wp[j]=1.0*wincnt/cnt;
		}
		for (int j=0;j<n;j++)
		{
			memset(awp,0,sizeof(awp));
			for(int l=0;l<n;l++)
			{
				int cnt=0;
				int wincnt=0;
				for (int k=0;k<n;k++)
				{
					if (k==j) continue;
					if (match[l][k]=='.')
						continue;
					if (match[l][k]=='1')
						wincnt++;
					cnt++;
				}
				awp[l]=1.0*wincnt/cnt;
			}

			double sum=0;
			int cnt=0;
			for (int k=0;k<n;k++)
			{
				if (match[j][k]=='.')
					continue;
				sum+=awp[k];
				cnt++;
			}
			owp[j]=sum/cnt;
		}
		for (int j=0;j<n;j++)
		{
			double sum=0;
			int cnt=0;
			for (int k=0;k<n;k++)
			{
				if (match[j][k]=='.')
					continue;
				sum+=owp[k];
				cnt++;
			}
			oowp[j]=sum/cnt;
		}
		cout<<"Case #"<<i<<":"<<endl;
		for (int j=0;j<n;j++)
		{
			double res=0.25 * wp[j] + 0.50 * owp[j] + 0.25 * oowp[j];
			printf("%.12lf\n",res);
		}
	}
	return 0;
}