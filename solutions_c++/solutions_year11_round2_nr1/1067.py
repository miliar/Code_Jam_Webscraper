#include<iostream>
#include<cmath>

using namespace std;

int main()
{
	long T;
	cin >> T;

	for(int t = 0; t < T; t++)
	{
		long N;
		cin >> N;

		double wp[N];
		int wins[N];
		int losses[N];
		int won[N][N];
		int lost[N][N];

		for(int n = 0; n < N; n++)
		{
			losses[n] = wins[n] = 0;
			for(int m = 0; m < N; m++)
			{
				char c;
				cin >> c;
				won[n][m] = lost[n][m] = 0;
				if(c == '0')
				{
					losses[n]++;
					lost[n][m] = 1;
				}
				if(c == '1')
				{
					wins[n]++;
					won[n][m] = 1;
				}

				wp[n] = (double)wins[n]/(wins[n] + losses[n]);
			}
		}
	
		double owp[N];
		for(int n  = 0; n < N; n++)
		{
			owp[n] = 0;
			for(int m = 0; m < N; m++)
				owp[n] += abs((double)won[n][m] + lost[n][m])*(wins[m] - won[m][n])/(wins[m] + losses[m] - won[m][n] - lost[m][n]);	
			owp[n] = owp[n]/((wins[n] + losses[n]));
		}

		double oowp[N];
		for(int n  = 0; n < N; n++)
		{
			oowp[n] = 0;	
			for(int m = 0; m < N; m++)
				oowp[n] += abs((double)won[n][m] + lost[n][m])*owp[m];	

			oowp[n] = oowp[n]/(wins[n] + losses[n]);
		}

		double rpi[N];
		cout << "Case #" << (t+1) << ":" << endl;

		for(int n  = 0; n < N; n++)
		{
			rpi[N] = 0.25*wp[n] + 0.5*owp[n] + 0.25*oowp[n];
			cout << rpi[N] << endl;
		}

	}
}
