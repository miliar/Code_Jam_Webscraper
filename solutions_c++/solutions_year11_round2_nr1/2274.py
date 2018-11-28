#include<iostream>
#include<string>
#include<iomanip>
using namespace std;
int main()
{
	int tc,tbc;
	cin>>tc;
	tbc = tc;
	cout<<setprecision(12);
	while(tc--)
	{
		int n;
		cin>>n;
		string arr[n];
		double wp[n],owp[n],oowp[n];
		
		//reset
		for(int i=0;i<n;i++)
		{
			wp[i]=0;
			owp[i]=0;
			oowp[i]=0;
		}
	
		for(int i=0;i<n;i++)cin>>arr[i];

		//wp
		for(int i=0;i<n;i++)
		{
			int w=0,l=0;
			for(int j=0;j<n;j++)
			{
				if(arr[i][j]=='1')w++;
				else if(arr[i][j]=='0')l++;
			}
			wp[i] = (double)w/((double)w+(double)l);
		}

		//owp
		for(int i=0;i<n;i++)
		{
			int opp=0;
			for(int j=0;j<n;j++)
			{
				if(arr[i][j]!='.')
				{
					opp++;
					int w=0,l=0;
					for(int k=0;k<n;k++)
					{
						if(k!=i)
						{
							if(arr[j][k]=='1')w++;
							else if(arr[j][k]=='0')l++;		
						}
					}
					owp[i] += (double)w/((double)w+(double)l);
				}
			}
			owp[i] /= (double)opp;
		}

		//oowp
		for(int i=0;i<n;i++)
		{
			int opp=0;
			for(int j=0;j<n;j++)
			{
				if(arr[i][j]!='.')
				{
					opp++;
					oowp[i] += owp[j];
				}
			}
			oowp[i] /= (double)opp;
		}
		
		cout<<"Case #"<<tbc-tc<<":"<<endl;
		//Calculation
		for(int i=0;i<n;i++)
		{
			cout<<(0.25*wp[i]+0.5*owp[i]+0.25*oowp[i])<<endl;
		}
	}
	return 0;
}
