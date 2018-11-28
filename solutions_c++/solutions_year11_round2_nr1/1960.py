#include <iostream>
#include <vector>
#include <string>
#include <sstream> 
#include <cstdlib>


using namespace std;

int main()
{
	int T=0;
	cin>>T;

	for (int t=0;t<T;t++)
	{
		int N;
		cin>>N;

		string str[N]; 

		double rpi[N];
		double wp[N];
		double owp[N];
		double oowp[N];

		for (int n=0;n<N;n++) 
		{
			cin>>str[n];
		}

		for (int n=0;n<N;n++) 
		{
				int w=0, p=0;
				for (int j=0;j<N;j++) 
				{
					if (str[n][j]!='.') p++;
					if (str[n][j]=='1') w++;
				}
				wp[n] = (double)w/p;
		}
		
		for (int n=0;n<N;n++) 
		{
			double wpt[n];
			for (int i=0;i<N;i++) 
			{
					int w=0, p=0;
					for (int j=0;j<N;j++) 
					{
						if (j==n) continue;
						if (str[i][j]!='.') p++;
						if (str[i][j]=='1') w++;
					}
					wpt[i] = (double)w/p;
			}
	
			double swp=0;
			int cwp=0;
			for (int i=0;i<N;i++) {
				if (i==n || str[n][i]=='.') continue;
				swp+=wpt[i];
				cwp++;
			}
	
			owp[n]=swp/cwp;
		}

		for (int n=0;n<N;n++) 
		{	
			double sowp=0;
			int cowp=0;
			for (int i=0;i<N;i++)
			{
				if (i==n || str[n][i]=='.') continue;
				sowp+=owp[i];
				cowp++;

			}

			oowp[n]=sowp/cowp;
		}

		cout<<"Case #"<<t+1<<":"<<endl;
		for (int i=0;i<N;i++){cout.precision(12); cout<<0.25*wp[i]+0.5*owp[i] + 0.25*oowp[i]<<endl;}
	
	}//test case for ends

}
