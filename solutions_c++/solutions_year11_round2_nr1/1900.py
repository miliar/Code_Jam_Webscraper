#include <iostream>
#include <numeric>
#include <string>
#include <vector>

using namespace std;

int main(int argc, char** argv)
{
	int N;
	cin >> N;
	for (int i = 0; i < N; ++i)
	{
		int m;
		cin >> m;
		vector <string> table(m);
		for (int j = 0; j < m; ++j)
			cin >> table[j];

		cout << "Case #" << (i + 1) << ": " << endl;
		vector <double> wp(m), owp(m), oowp(m);
		vector <int> win(m), game(m);
		for (int j = 0; j < table.size(); ++j)
		{
			int wins = 0, games = 0;
			for (int k = 0; k < table[j].size(); ++k)
			{
				wins += (table[j][k] == '1');
				games += (table[j][k] != '.');
			}
			wp[j] = double(wins) / games;
			win[j] = wins;
			game[j] = games;
		}
		for (int j = 0; j < table.size(); ++j)
		{
			double t = 0;
			int opponents = 0;
			for (int k = 0; k < win.size(); ++k)
			{
				if (k == j || table[k][j] == '.')
					continue;
				++opponents;
				t += double(win[k] - (table[k][j] == '1')) / (game[k] - 1);
			}
			t /= opponents;
			owp[j] = t;
		}
		for (int j = 0; j < table.size(); ++j)
		{
			int opponents = 0;
			for (int k = 0; k < table.size(); ++k)
			{
				if (table[j][k] == '.')
					continue;
				oowp[j] += owp[k];
				++opponents;
			}
			oowp[j] /= opponents;
			cout << (0.25 * wp[j] + 0.5 * owp[j] + 0.25 * oowp[j]) << endl;
		}
	}
	return 0;
}
