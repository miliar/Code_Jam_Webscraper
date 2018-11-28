#include <iostream>
using namespace std;

#include <fstream>
using std::ifstream;
using std::ofstream;

int main()
{
	ifstream indata;
	ofstream outdata;
	int t;
	indata.open("A-large.in");
	outdata.open("A.txt");
	indata>>t;
	for(int i = 1; i <= t; i++)
	{
		
		int n;
		indata>>n;
		int a[n][n];
		double ng[n], ngw[n], wp[n], owp[n], oowp[n], rpi[n];
		for(int j = 0; j < n; j++)
		{
			ng[j] = 0;
			ngw[j] = 0;
			for(int k = 0; k < n; k++)
			{
				char c;
				indata>>c;
				if(c == '0')
				{
					ng[j] = ng[j] + 1;
					a[j][k] = 0;
				}
				else if(c == '1')
				{
					ng[j] = ng[j] + 1;
					ngw[j] = ngw[j] + 1;
					a[j][k] = 1;
				}
				else
					a[j][k] = -1;
			}	

			wp[j] = (ngw[j]/ng[j]);
		}

		for(int j = 0; j < n; j++)
		{
			owp[j] = 0;
			for(int k = 0; k < n; k++)
			{
				if(a[j][k] != -1)
				{
					if(a[j][k] == 1)
						owp[j] = owp[j] + ((ngw[k])/(ng[k] - 1));
					else if(a[j][k] == 0)
						owp[j] = owp[j] + ((ngw[k] - 1)/(ng[k] - 1));
				}
			}	

			owp[j] = (owp[j]/ng[j]);
		}

		for(int j = 0; j < n; j++)
		{
			oowp[j] = 0;
			for(int k = 0; k < n; k++)
			{
				if(a[k][j] != -1)
					oowp[j] = oowp[j] + owp[k];
			}	

			oowp[j] = (oowp[j]/ng[j]);
		}

		outdata<<"Case #"<<i<<": \n";
		for(int j = 0; j < n; j++)
		{
			rpi[j] = (0.25 * wp[j]) + (0.50 * owp[j]) + (0.25 * oowp[j]);
			outdata<<rpi[j]<<"\n";
		}

	}
	indata.close();
	outdata.close(); 
}
