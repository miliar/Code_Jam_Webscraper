#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <cctype>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <bitset>
#include <iomanip>

using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int cntTest;
	cin >> cntTest;

	for (int test = 0; test < cntTest; ++test)
	{
		int n;
		cin >> n;

		vector <string> table(n);		
		getline(cin, table[0]);
		for (int i = 0; i < n; ++i)
			getline(cin, table[i]);

		vector <int> win(n), game(n);
		vector <double> owp(n), oowp(n), rank(n);

		for (int i = 0; i < n; ++i)
		{
			int cntWin = 0, cntGame = 0;
			for (int j = 0; j < n; ++j)
			{
				if (table[i][j] == '.')
					continue;

				++cntGame;
				if (table[i][j] == '1') ++cntWin;
			}

			win[i] = cntWin; game[i] = cntGame;
		}

		for (int i = 0; i < n; ++i)
		{
			int cntTeams = 0;
			double res = 0;

			for (int j = 0; j < n; ++j)
			{	
				if (i == j)
					continue;

				int cntWin = win[j], cntGame = game[j];
				if (table[j][i] != '.')
				{
					--cntGame;
					if (table[j][i] == '1') --cntWin;
					++cntTeams;

					res += (double)cntWin / cntGame;
				}				
			}

			owp[i] = res / cntTeams;
		}

		for (int i = 0; i < n; ++i)
		{
			int cntTeam = 0;
			double res = 0;

			for (int j = 0; j < n; ++j)
				if (table[i][j] != '.')
				{
					res += owp[j];
					++cntTeam;
				}

			oowp[i] = res / cntTeam;
		}

		for (int i = 0; i < n; ++i)
			rank[i] = (double)win[i] / game[i] * .25 + owp[i] * .5 + oowp[i] * .25;

		cout << "Case #" << test + 1 << ":" << endl;
		for (int i = 0; i < n; ++i)
			cout << fixed << setprecision(10) << rank[i] << endl;
	}

	return 0;
}