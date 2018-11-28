#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("answer.txt", "w", stdout);
	int tc;
	cin>>tc;
	for(int Case = 0; Case < tc; Case++)
	{
		int r, c;
		cin >> r >> c;
		vector<string> pic(r);
		for(int i = 0; i < r; ++i)
		{
			cin >> pic[i];
		}
		bool ok = true;
		for(int i = 0; i < r; ++i)
		{
			for(int j = 0; j < c; ++j)
			{
				if(pic[i][j] == '#')
				{
					if(i+1 < r && j+1 < c && pic[i+1][j] == '#' && pic[i][j+1] == '#' && pic[i+1][j+1] == '#')
					{
						pic[i][j] = '/';
						pic[i+1][j+1] = '/';
						pic[i+1][j] = '\\';
						pic[i][j+1] = '\\';
					}
					else
					{
						ok = false;
					}
				}
			}
		}

		cout << "Case #" << Case + 1 <<": " << endl;
		if(ok)
		{
			for(int i = 0; i < r; ++i)
			{
				cout << pic[i] << endl;
			}
		}
		else
			cout << "Impossible" << endl;
	}

	return 0;
}
