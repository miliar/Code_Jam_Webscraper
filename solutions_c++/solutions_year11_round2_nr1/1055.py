#include <iostream>
#include <cstdio>
#include <iomanip>

using namespace std;

const int MAXN = 100 + 10;

int n;
double op[MAXN], wp[MAXN], owp[MAXN], oowp[MAXN], rpi[MAXN];
char m[MAXN][MAXN];

double c_wp(int d, int r)
{
	double s = 0;
	for(int i=1; i<=n; i++)
		if(i != r && m[d][i] != '.')
			s += (m[d][i] == '1');
	return s/(op[d] - !!r);
}

int main()
{
	cout << fixed << setprecision(7);

	int t;
	cin >> t;
	for(int T=1; T<=t; T++)
	{
		cin >> n;
		for(int i=1; i<=n; i++)
		{
			op[i] = 0;
			for(int j=1; j<=n; j++)
			{
				cin >> m[i][j];
				op[i] += (m[i][j] != '.');
			}
		}

		for(int i=1; i<=n; i++)
			wp[i] = c_wp(i, 0);
		for(int i=1; i<=n; i++)
		{
			double &o = owp[i] = 0;
			for(int j=1; j<=n; j++)
				if(m[i][j] != '.')
					o += c_wp(j, i);
			o /= op[i];
		}
		for(int i=1; i<=n; i++)
		{
			double &o = oowp[i] = 0;
			for(int j=1; j<=n; j++)
				if(m[i][j] != '.')
					o += owp[j];
			o /= op[i];
		}
		for(int i=1; i<=n; i++)
			rpi[i] = 0.25*wp[i] + 0.50*owp[i] + 0.25*oowp[i];

		cout << "Case #" << T << ":" << endl;
		for(int i=1; i<=n; i++)
			cout << rpi[i] << endl;
	}
	return 0;
}

