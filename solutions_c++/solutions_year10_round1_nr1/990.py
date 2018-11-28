#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

void
rotate (
	vector< string > &table
) {
	if (table.empty()
	||  table.size() != table[0].size())
	{
		return;
	}

	vector< string > tmp(table);

	int matrix[2][2] = { { 0, -1 }, { 1, 0 } };

	for (unsigned int i = 0; i < table.size(); i++)
	{
		for (unsigned int j = 0; j < table.size(); j++)
		{
			int k = i * matrix[0][0] + j * matrix[0][1] + table.size() - 1,
			    l = i * matrix[1][0] + j * matrix[1][1];
			//cerr << "(" << k << ", " << l << ") <- (" << i << ", " << j << ")" << endl;
			table[i][j] = tmp[k][l];
		}
	}
}

void
fall (
	vector< string > &table
) {
	if (table.empty()
	||  table.size() != table[0].size())
	{
		return;
	}

	vector< string > tmp(table);

	const unsigned int offset = table.size() - 1;

	for (unsigned int i = 0; i < table.size(); i++)
	{
		unsigned int current = 0;
		for (unsigned int j = 0; j < table.size(); j++)
		{
			table[offset - j][offset - i] = '.';

			if (tmp[offset - j][offset - i] == '.')
			{
				continue;
			}

			table[offset - current++][offset - i] = tmp[offset - j][offset - i];
		}
	}
}

void
check (
	const vector< string > &table,
	int K
) {
	bool flags[2];

	vector< vector< int > > tmp1(2, vector< int >(4, 0));
	vector< vector< vector< int > > > tmp2(table.size(), tmp1);
	vector< vector< vector< vector< int > > > > dp(table.size(), tmp2);

	for (unsigned int i = 0; i < table.size(); i++)
	{
		for (unsigned int j = 0; j < table.size(); j++)
		{
			unsigned int rob;

			switch (table[i][j])
			{
			case 'R':
				rob = 0;
				break;
			case 'B':
				rob = 1;
				break;
			default:
			case '.':
				continue;
			}

			dp[i][j][rob][0] = 1;
			dp[i][j][rob][1] = 1;
			dp[i][j][rob][2] = 1;
			dp[i][j][rob][3] = 1;

			if (i > 0)
			{
				dp[i][j][rob][0] += dp[i-1][j][rob][0];
			}
			if (j > 0)
			{
				dp[i][j][rob][1] += dp[i][j-1][rob][1];
			}
			if (i > 0 && j > 0)
			{
				dp[i][j][rob][2] += dp[i-1][j-1][rob][2];
			}
			if (i > 0 && j < table.size() - 1)
			{
				dp[i][j][rob][3] += dp[i-1][j+1][rob][3];
			}

			if (dp[i][j][rob][0] >= K
			||  dp[i][j][rob][1] >= K
			||  dp[i][j][rob][2] >= K
			||  dp[i][j][rob][3] >= K
			) {
				flags[rob] = true;
			}
		}
	}

	if (flags[0] && flags[1])
	{
		cout << "Both";
	}
	else if (flags[0] && !flags[1])
	{
		cout << "Red";
	}
	else if (!flags[0] && flags[1])
	{
		cout << "Blue";
	}
	else if (!flags[0] && !flags[1])
	{
		cout << "Neither";
	}
	else
	{
		cerr << "ERROR!" << endl;
	}
}

int
main (
	int argc,
	char **argv
) {
	if (argc < 2)
	{
		cerr << "no input data specified." << endl;
		return -1;
	}

	fstream fin(argv[1], ios::in);

	int T;
	fin >> T;

	for (int t = 0; t < T; t++)
	{
		long N, K;
		fin >> N >> K;

		cerr << "N: " << N << ", K: " << K << endl;

		vector< string > table;
		string buffer;
		for (long n = 0; n < N; n++)
		{
			fin >> buffer;
			table.push_back(buffer);
		}

		cerr << "origin:" << endl;
		for (vector< string >::const_iterator it = table.begin();
			it != table.end();
			it++)
		{
			cerr << *it << endl;
		}
		cerr << endl;

		rotate(table);

		cerr << "rotated:" << endl;
		for (vector< string >::const_iterator it = table.begin();
			it != table.end();
			it++)
		{
			cerr << *it << endl;
		}
		cerr << endl;

		fall(table);

		cerr << "falled:" << endl;
		for (vector< string >::const_iterator it = table.begin();
			it != table.end();
			it++)
		{
			cerr << *it << endl;
		}
		cerr << endl;

		cout << "Case #" << (t + 1) << ": ";
		check(table, K);
		cout << endl;

		cerr << endl;
	}

	fin.close();

	return 0;
}
