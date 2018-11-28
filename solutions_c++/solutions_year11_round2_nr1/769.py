# include <iostream>
# include <fstream>
# include <string>
# include <vector>
# include <algorithm>
# include <cmath>
# include <iomanip>
using namespace std;

int main()
{
	ifstream cin("A.in");
	ofstream cout("A.out");
	int t;
	cin >> t;
	int casenum = 0;
	while(t - casenum)
	{
		int n;
		cin >> n;
		vector<string> vs(n);
		for(int i = 0; i < n; ++i)
			cin >> vs[i];
		vector<vector<double>> wp(n);
		vector<double> owp(n, 0.0);
		vector<double> oowp(n, 0.0);
		vector<int> games(n, 0);
		for(int i = 0; i < n; ++i)
		{
			int won = 0;
			for(int j = 0; j < n; ++j)
			{
				if(vs[i][j] == '1')
					++won;
				if(vs[i][j] != '.')
					++games[i];
			}
			for(int j = 0; j < n; ++j)
			{
				if(vs[i][j] == '1')
					wp[i].push_back(static_cast<double>(won - 1) / static_cast<double>(games[i] - 1));
				else if(vs[i][j] == '0')
					wp[i].push_back(static_cast<double>(won) / static_cast<double>(games[i] - 1));
				else if(vs[i][j] == '.')
					wp[i].push_back(static_cast<double>(won) / static_cast<double>(games[i]));
			}		
		}
		for(int i = 0; i < n; ++i)
		{
			for(int j = 0; j < n; ++j)
				if(vs[i][j] != '.')
					owp[i] += wp[j][i];
			owp[i] /= games[i];
		}
		for(int i = 0; i < n; ++i)
		{
			for(int j = 0; j < n; ++j)
				if(vs[i][j] != '.')
					oowp[i] += owp[j];
			oowp[i] /= games[i];
		}

		cout << "Case #" << casenum + 1 << ":" << endl;
		for(int i = 0; i < n; ++i)
			cout << setprecision(10) << setiosflags(ios::fixed | ios::showpoint) <<  0.25 * wp[i][i] + 0.5 * owp[i] + 0.25 * oowp[i] << endl;
		++casenum;
	}
	return 0;
}
