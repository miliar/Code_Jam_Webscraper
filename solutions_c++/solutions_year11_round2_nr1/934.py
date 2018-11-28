#include <iostream>
#include <iomanip>
#include <fstream>
using namespace std;

string s[101];

int win[101], lose[101];
double wp[101], owp[101], oowp[101];
int cnt;

int main ()
{
	freopen("A-large.in", "r", stdin);
	freopen("a.txt", "w", stdout);
	int T;
	cin>>T;
	int n;
	for(int t=1; t<=T; ++t)
	{
		cin>>n;
		for(int i=0; i<n; ++i)
		{
			win[i]=0; lose[i]=0;
			cin>>s[i];
			for(int j=0; j<n; ++j)
			{
				if (s[i][j]=='1') ++win[i];
				else if (s[i][j]=='0') ++lose[i];
			}	
			wp[i]=win[i];
			wp[i]/=(win[i]+lose[i]);
		}
		for(int i=0; i<n; ++i)
		{
			cnt=0;
			owp[i]=0;
			for(int j=0; j<n; ++j)
			{
				if (s[i][j]=='0')
				{
					++cnt;
					owp[i]+= double(win[j]-1)/(lose[j]+win[j]-1);		
				}
				else if (s[i][j]=='1')
				{
					++cnt;
					owp[i]+=double(win[j])/(lose[j]+win[j]-1);	
				}
			}	
			owp[i]/=cnt;
		}
		for(int i=0; i<n; ++i)
		{
			cnt=0;
			oowp[i]=0;
			for(int j=0; j<n; ++j)
			{
				if (s[i][j]!='.')
				{
					++cnt;
					oowp[i]+=owp[j];		
				}
			}	
			oowp[i]/=cnt;
		}		
		cout<<"Case #"<<t<<": "<<endl;
		for(int i=0; i<n; ++i)
		{
			cout<<fixed<<setprecision(10)<<0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]<<endl; 
		}
	}
}
