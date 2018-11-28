#include<iostream>
#include<string>
#include<fstream>
#include<vector>
#include<cstdio>
using namespace std;


int main()
{

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t;
	cin >> t;

	for(int tt = 1; tt <= t; tt++)
	{
		int n;
		cin >> n;


		vector<string> g(n);
		for(int i = 0; i < n; i++)
			cin >> g[i];
		vector<double> wp(n);
		vector<double> sum(n), cnt(n);
		for(int i = 0; i < n; i++)
		{
			for(int j = 0; j < n; j++)
			{
				if(g[i][j] == '1')
					sum[i] += 1.0;
				if(g[i][j] != '.')
					cnt[i] += 1.0;
			}
			wp[i] = sum[i] / cnt[i];
		}

		vector<double> owp(n);
		for(int i = 0; i < n; i++)
		{
			double s = 0.0, c = 0.0;
			for(int j = 0; j < n; j++)
			{
				if(g[i][j] != '.') //j is opponent of i
				{
					s += (sum[j] - (1 - g[i][j] + '0')) / (cnt[j] - 1.0);
					c += 1.0;
				}
			}
			owp[i] = s / c;
		}

		vector<double> oowp(n);
		for(int i = 0; i < n; i++)
		{
			double s = 0.0;
			double c = 0.0;
			for(int j = 0; j < n; j++)
			{
				if(g[i][j] != '.')
				{
					s += owp[j];
					c += 1.0;
				}
			}
			oowp[i] = s / c;
		}


		cout << "Case #" << tt <<":" << endl;
		for(int i = 0; i < n; i++)
			printf("%0.9lf\n", 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i]);
	}

	return 0;
}