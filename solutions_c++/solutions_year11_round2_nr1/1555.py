#include <iostream>
#include <stdio.h>

#define ct (int) 1e2

using namespace std;

double wp[ct], owp[ct], oowp[ct];
int t, n, cnt[ct];
char table[ct][ct];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> t;

	cout.precision(7);

	for (int i = 0; i < t; i++)
	{
		cin >> n;

		cerr << n << endl;

		for (int j = 0; j < n; j++)
			for (int k = 0; k < n; k++)
			{
				cin >> table[j][k];
			}		

		for (int j = 0; j < n; j++)
			wp[j] = owp[j] = oowp[j] = 0;
		for (int j = 0; j < n; j++)
			cnt[j] = 0;

		for (int j = 0; j < n; j++)
			for (int k = 0; k < n; k++)
				if (table[j][k] != '.')
					cnt[j]++;

		for (int j = 0; j < n; j++)
		{
			for (int k = 0; k < n; k++)
				if (table[j][k] != '.')
				{
					wp[j] += table[j][k] - '0';
				}  	
		  	
		}

		for (int j = 0; j < n; j++)
		{
			for (int k = 0; k < n; k++)
				if (table[j][k] != '.')
				{
					owp[j] += (wp[k] - table[k][j] + '0') / (cnt[k] - 1);
				}

			owp[j] /= cnt[j];

		  	//cerr << "owp #" << j << " = " << owp[j] << endl;
		}

		for (int j = 0; j < n; j++)
		{
			for (int k = 0; k < n; k++)
				if (table[j][k] != '.')
				{
					oowp[j] += owp[k];
				}

			oowp[j] /= cnt[j];	

			//cerr << "oowp #" << j << " = " << oowp[j] << endl;
		}

		cout << "Case #" << i + 1 << ":" << endl;
		for (int j = 0; j < n; j++)
			cout << fixed << 0.25 * (wp[j] / cnt[j]) + 0.5 * owp[j] + 0.25 * oowp[j] << endl;
			  
	}	

	return 0;
}