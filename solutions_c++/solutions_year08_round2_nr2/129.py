#pragma warning( disable : 4786 )

#include <map>
#include <queue>
#include <stack>
#include <set>
#include <list>
#include <string>
#include <cmath>
#include <iostream>
#include <sstream>
#include <utility>
#include <limits>
#include <numeric>
#include <iomanip>
#include <algorithm>
#include <fstream>

using namespace std;

vector<vector<int> > a;
vector<int> was;
int n;

void dfs(int v)
{
	was[v] = 1;
	for (int i = 0; i < n; ++i)
		if (a[v][i] == 1 && was[i] == 0)
			dfs(i);
}

int main()
{
	ifstream ifs("b.in");
	ofstream ofs("b.out");
	
	int t;
	ifs >> t;
	for (int l = 0; l < t; ++l)
	{
		int res = 0;
		a.assign(1000, vector<int>(1000, 0));
		int A, B, p;
		ifs >> A >> B >> p;
		map<int, int> m;
		n = 0;
		for (int i = A; i <= B; ++i)
		{
			int k = i;
			int j = 2;
			vector<int> tmp;
			while (k > 1)
			{
				if (k % j == 0)
				{
					while (k % j == 0) k /= j;
					if (j >= p)
					{
						if (m.count(j) == 0)
						{
							m[j] = n;
							++n;
						}
						tmp.push_back(j);
					}
				}
				++j;
			}
			if (tmp.empty())
			{
				++res;
			}
			for (int j = 0; j < tmp.size(); ++j)
				for (int k = j+1; k < tmp.size(); ++k)
				{
					a[m[tmp[j]]][m[tmp[k]]] = 1;
					a[m[tmp[k]]][m[tmp[j]]] = 1;
				}
		}
		was.assign(n, 0);
		for (int i = 0; i < n; ++i)
			if (was[i] == 0)
			{
				dfs(i);
				++res;
			}
		ofs << "Case #" << l+1 << ": " << res << endl;
	}
	return 0;
}
