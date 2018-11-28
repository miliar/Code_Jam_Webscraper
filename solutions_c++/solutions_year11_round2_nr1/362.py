#include <iostream>
#include <iomanip>

#include <string>
#include <vector>
#include <utility>
#include <algorithm>
#include <complex>
#include <cmath>
#include <map>
#include <numeric>
#include <set>
#include <iterator>
#include <bitset>

using namespace std;

//ostream_iterator<int> spout(cout, " ");

typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<double> vd;

int N;
vs tbl;

vi wins, games;
vd owp, oowp;

void parseCase(istream &inp)
{
	inp >> N;

	tbl.clear();

	for (int j = 0; j < N; ++j)
	{
		string l;
		inp >> l;
		tbl.push_back(l);
	}
}

void answer()
{
	games.clear();
	games.resize(N);
	wins.clear();
	wins.resize(N);

	for (int j = 0; j < N; ++j)
	for (int k = 0; k < N; ++k)
	{
		if (tbl[j][k] == '.') continue;

		if (tbl[j][k] == '1') ++wins[j];
		++games[j];
	}

	owp.clear();
	owp.resize(N);

	for (int j = 0; j < N; ++j)
	{
		for (int k = 0; k < N; ++k)
		{
			switch(tbl[j][k])
			{
				case '.':
					break;
				case '1':
					owp[j] += double(wins[k]) / (games[k]-1);
					break;
				case '0':
					owp[j] += double(wins[k]-1) / (games[k]-1);
					break;
			}
		}
		owp[j] /= games[j];
	}

	oowp.clear();
	oowp.resize(N);

	for (int j = 0; j < N; ++j)
	{
		for (int k = 0; k < N; ++k)
		{
			if (tbl[j][k] == '.') continue;

			oowp[j] += owp[k];
		}
		oowp[j] /= games[j];
	}

	for (int j = 0; j < N; ++j)
		cout << 0.25 * (double(wins[j]) / games[j]) + 0.5 * owp[j] + 0.25 * oowp[j] << endl;
	
}

#ifndef ANS_NOMAIN
int main()
{
	cout.precision(10);
	cout << fixed;

	int T;
	cin >> T;
	for (int caseNum = 1; caseNum <= T; ++caseNum)
	{
		parseCase(cin);
		cout << "Case #" << caseNum << ": " << endl;
		answer();
	}

	return 0;
}
#endif
