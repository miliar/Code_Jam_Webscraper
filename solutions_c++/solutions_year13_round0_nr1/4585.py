#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

typedef unsigned long long uint64;

int main()
{
	ios_base::sync_with_stdio(0);
	int test_cases;
	cin >> test_cases;
	for (int test_num = 1; test_num <= test_cases; ++test_num) {
		cout << "Case #" << test_num << ": ";
		vector<vector<char> > v(4, vector<char>(4));
		int n = 4;
		for (auto &i : v)
			for (auto &j : i)
				cin >> j;
		vector<char> users = {'X', 'O'};
		bool done = 0;
		for (auto &u : users) {
			bool gwin = 0;
			for (auto &i : v) {
				bool win = 1;
				for (auto &j : i)
					if (!(j == u || j == 'T'))
						win = 0;
				if (win)
					gwin = 1;
			}
			for (int j = 0; j < n; ++j) {
				bool win = 1;
				for (int i = 0; i < n; ++i)
					if (!(v[i][j] == u || v[i][j] == 'T'))
						win = 0;
				if (win)
					gwin = 1;
			}
			{
				bool win = 1;
				for (int i = 0; i < n; ++i)
					if (!(v[i][i] == u || v[i][i] == 'T'))
						win = 0;
				if (win)
					gwin = 1;
			}
			{
				bool win = 1;
				for (int i = 0; i < n; ++i)
					if (!(v[i][n - i - 1] == u || v[i][n - i - 1] == 'T'))
						win = 0;
				if (win)
					gwin = 1;
			}

			if (gwin) {
				done = 1;
				cout << u << " won" << endl;
				break;
			}
		}
		if (done)
			continue;
		bool not_compl = 0;
		for (auto &i : v)
			for (auto &j : i)
				if (j == '.')
					not_compl = 1;
		if (not_compl)
			cout << "Game has not completed" << endl;
		else
			cout << "Draw" << endl;
	}
	return 0;
}