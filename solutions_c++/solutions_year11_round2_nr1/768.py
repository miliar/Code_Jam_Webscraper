#include <iostream>
#include <string>
#include <vector>
#include <cstring>

using namespace std;

double wp[102];
double owp[102];
double oowp[102];
double rpi[102];
double w[102];
double t[102];

int main()
{
	int T;
	cin >> T;
	for(int i=1;i<=T;i++)
	{
		int N;
		cin >> N;
		vector<string> vs;
		string s;
		memset(wp,0,sizeof(wp));
		memset(owp,0,sizeof(owp));
		memset(rpi,0,sizeof(rpi));
		memset(oowp,0,sizeof(oowp));
		memset(w,0,sizeof(w));
		memset(t,0,sizeof(t));
		for(int j=0;j<N;j++)
		{
			cin >> s;
			vs.push_back(s);
		}
		for(int j=0;j<N;j++)
		{
			for(int k=0;k<N;k++)
			{
				if(vs[j][k] == '0')
				{
					t[j]++;
				}
				if(vs[j][k] == '1')
				{
					t[j]++;
					w[j]++;
				}
			
			}
			wp[j] = 1.0*w[j]/t[j];
		}

		for(int j=0;j<N;j++)
		{

			for(int k=0;k<N;k++)
			{
				if(vs[j][k] == '0')
				{
					owp[j] += 1.0*(w[k]-1)/(t[k]-1);
				}
				if(vs[j][k] == '1')
				{
					owp[j] += 1.0*(w[k])/(t[k]-1);
				}
			}
			owp[j] /= t[j]; 
		}
		for(int j=0;j<N;j++)
		{
			for(int k=0;k<N;k++)
			{
				if(isdigit(vs[j][k]))
				{
					oowp[j] += owp[k];
				}	
			}
			oowp[j] /= t[j];
		}
		
		for(int j=0;j<N;j++)
		{
			rpi[j] = 0.25*wp[j]+0.5*owp[j]+0.25*oowp[j];
		}
		cout << "Case #" << i << ": " << endl;
		for(int j=0;j<N;j++)
		{
			cout << rpi[j] << endl;
		}
 	}
}
