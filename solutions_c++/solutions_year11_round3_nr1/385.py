#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <deque>
#include <map>
#include <cmath>
#include <set>
#include <stack>
#include <sstream>

using namespace std;

string toString(int val)
{
    ostringstream oss;
    oss << val;
    return oss.str();
}

int fromString(const std::string& s) 
{
  istringstream iss(s);
  int res;
  iss >> res;
  return res;
}

int main() 
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t)
	{
		cout << "Case #" << t + 1 << ":" << endl;
		int R, C;
		cin >> R >> C;
		vector <string> table(R);
		for (int i = 0; i < R; ++i)
		{
			cin >> table[i];
		}
		for (int i = 0; i < R - 1; ++i)
		{
			for (int j = 0; j < C - 1; ++j)
			{
				if ((table[i][j] == '#') && (table[i][j + 1] == '#') && (table[i + 1][j] == '#') && (table[i + 1][j + 1] == '#'))
				{
					table[i][j] = table[i + 1][j + 1] = '/';
					table[i + 1][j] = table[i][j + 1] = '\\';
				}
			}
		}
		bool good = true;
		for (int i = 0; i < R; ++i)
		{
			for (int j = 0; j < C; ++j)
			{
				if (table[i][j] == '#')
				{
					good = false;
				}
			}
		}
		if (good)
		{
			for (int i = 0; i < R; ++i)
			{
				cout << table[i] << endl;
			}
		}
		else
		{
			cout << "Impossible" << endl;
		}
	}
	return 0;
}







