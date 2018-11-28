#include<iostream>
#include<string>
using namespace std;

#define MAXN 101

int t,n;
string b[MAXN];
double wp[MAXN],owp[MAXN],oowp[MAXN],rpi[MAXN];

int main()
{
	//freopen("in.txt","r",stdin);
	//freopen("A-small-attempt0.in","r",stdin);
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>t;
	for(int ca=1;ca<=t;++ca)
	{
		printf("Case #%d: \n",ca);
		cin>>n;
		for(int i=0;i<n;++i)
		{
			cin>>b[i];
		}

		for(int i=0;i<n;++i)
		{
			int cnt=0;
			int w=0;
			for(int j=0;j<n;++j)
			{
				if(b[i][j]=='1')
				{
					cnt++;
					w++;
				}
				else if(b[i][j]=='0')
				{
					cnt++;
				}
			}
			wp[i]=(double)w/cnt;
		}

		for(int i=0;i<n;++i)
		{
			int cnt=0;
			double s=0;
			for(int j=0;j<n;++j)
			{
				if(b[i][j]!='.')
				{
					cnt++;
					int cnt0=0;
					int w0=0;
					for(int k=0;k<n;++k)
					{
						if(k==i)
						{
							continue;
						}
						if(b[j][k]=='1')
						{
							cnt0++;
							w0++;
						}
						else if(b[j][k]=='0')
						{
							cnt0++;
						}
					}
					s+=(double)w0/cnt0;
				}
			}
			owp[i]=s/cnt;
		}

		for(int i=0;i<n;++i)
		{
			int cnt=0;
			double s=0;
			for(int j=0;j<n;++j)
			{
				if(b[i][j]!='.')
				{
					s+=owp[j];
					cnt++;
				}
			}
			oowp[i]=s/cnt;
		}

		for(int i=0;i<n;++i)
		{
			rpi[i]=0.25*wp[i]+0.5*owp[i]+0.25*oowp[i];
		}

		for(int i=0;i<n;++i)
		{
			printf("%.7f\n",rpi[i]);
		}
	}
	return 0;
}
