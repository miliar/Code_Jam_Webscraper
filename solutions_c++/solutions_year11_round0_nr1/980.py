#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

void Move(int &start, int finish, int cntStep)
{
	if ( abs(start - finish) <= cntStep )
	{
		start = finish;
		return;
	}

	start += (start < finish ? 1 : -1) * cntStep;
}

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

		vector <int> or, bl;
		or.push_back(1); bl.push_back(1);
		vector < pair <string, int> > seq;

		string color;
		int number;
		for (int i = 0; i < n; ++i)
		{
			cin >> color >> number;

			seq.push_back(make_pair(color, number));
			(color == "O" ? or : bl).push_back(number);
		}

		int indOr = 0, indBl = 0, posOr = 1, posBl = 1, res = 0;
		for (int i = 0; i < n; ++i)
		{
			if (seq[i].first == "O")
			{
				int curr = abs(posOr - seq[i].second) + 1;
				res += curr;
				posOr = seq[i].second;
				++indOr;

				if (indBl == (int)bl.size() - 1)
					continue;
				Move(posBl, bl[indBl + 1], curr);
			}
			else
			{
				int curr = abs(posBl - seq[i].second) + 1;
				res += curr;
				posBl = seq[i].second;
				++indBl;

				if (indOr == (int)or.size() - 1)
					continue;
				Move(posOr, or[indOr + 1], curr);
			}

		}

		cout << "Case #" << test + 1 << ": " << res << endl;
	}

	return 0;
}