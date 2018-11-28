#include <map>
#include <string>
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;


void main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int cases;
	cin >> cases;
	for (int casen = 1; casen <= cases; casen++)
	{
		int n;
		cin >> n;
		vector < vector <int> > v(n);
		for (int i = 0; i < n; ++i)
		{
			v[i].resize(n);
			for (int j = 0; j < n; ++j)
			{
				char r;
				cin >> r;
				if (r == '.')
					v[i][j] = -1;
				else if (r == '0')
					v[i][j] = 0;
				else 
					v[i][j] = 1;
			}
		}
		cout << "Case #" << casen << ":" << endl;
		vector<double> wp(n);
		vector<double> owp(n);
		vector<double> oowp(n);
		for (int c = 0; c < n; ++c)
		{
			//cout << 0.25*wp[j] + 0.5*owp[j] + 0.25*oowp[j] << endl;
			vector<double> localwp(n);
			for (int i = 0; i < n; ++i)
			{
				double cwp = 0;
				double fullwp = 0;
				int games = 0;
				int fullgames = 0;
				for (int j = 0; j < n; ++j)
				{
					if (v[i][j] == 1)
					{
						fullwp += 1;
						fullgames++;
						if (j != c)
						{
							cwp += 1;
							games++;
						}
					}
					else if (v[i][j] == 0)
					{
						fullgames++;
						if (j != c)
							games++;
					}
				}
				cwp /= games;
				localwp[i] = cwp;
				fullwp /= fullgames;
				wp[i] = fullwp;
			}
			double cowp = 0;
			int games = 0;
			for (int j = 0; j < n; ++j)
			{
				if (j != c && v[c][j] == 1 || v[c][j] == 0)
				{
					cowp += localwp[j];
					games++;
				}
			}
			cowp /= games;
			owp[c] = cowp;
		}
		for (int i = 0; i < n; ++i)
		{
			double coowp = 0;
			int games = 0;
			for (int j = 0; j < n; ++j)
			{
				if (v[i][j] == 1 || v[i][j] == 0)
				{
					coowp += owp[j];
					games++;
				}
			}
			coowp /= games;
			oowp[i] = coowp;
		}
		for (int i = 0; i < n; ++i)
			cout << 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i] << endl;
	}
}