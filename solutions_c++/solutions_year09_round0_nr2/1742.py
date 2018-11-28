#include <algorithm>
#include <cassert>
#include <iostream>
#include <set>
#include <string>
#include <vector>

using namespace std;


int h, w;
int att[128][128];
char res[128][128];
char curLetter;


char FillFlow(int i, int j)
{
	if (res[i][j] != 0)
	{
		return res[i][j];
	}

	int vals[] =
		{
			i > 0 ? att[i - 1][j] : 0x7FFFFFFF,
			j > 0 ? att[i][j - 1] : 0x7FFFFFFF,
			j < w - 1 ? att[i][j + 1] : 0x7FFFFFFF,
			i < h - 1 ? att[i + 1][j] : 0x7FFFFFFF
		};

	int minIndex = min_element(vals, vals + sizeof(vals)/sizeof(vals[0])) - vals;

	if (vals[minIndex] >= att[i][j])
	{	// It is a sink
		return res[i][j] = curLetter++;
	}

	switch (minIndex)
	{
	case 0: return res[i][j] = FillFlow(i - 1, j); break;
	case 1: return res[i][j] = FillFlow(i, j - 1); break;
	case 2: return res[i][j] = FillFlow(i, j + 1); break;
	case 3: return res[i][j] = FillFlow(i + 1, j); break;
	default: throw runtime_error("Impossible situation");
	}
}


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int testn;
	cin >> testn;

	for (int testi = 0; testi < testn; ++testi)
	{
		cin >> h >> w;

		for (int i = 0; i < h; ++i)
		{
			for (int j = 0; j < w; ++j)
			{
				cin >> att[i][j];
			}
		}

		curLetter = 'a';

		for (int i = 0; i < h; ++i)
		{
			fill_n(res[i], w, 0);
		}

		char prevResChar = 'a' - 1;

		for (int i = 0; i < h; ++i)
		{
			for (int j = 0; j < w; ++j)
			{
				if (res[i][j] == 0)
				{
					char resChar = FillFlow(i, j);
					assert(resChar <= prevResChar + 1);
					prevResChar = resChar;
				}
			}
		}

		cout << "Case #" << testi + 1 << ':' << endl;

		for (int i = 0; i < h; ++i)
		{
			for (int j = 0; j < w; ++j)
			{
				cout << res[i][j];

				if (j < w - 1)
				{
					cout << ' ';
				}
			}

			cout << endl;
		}
	}

	return 0;
}