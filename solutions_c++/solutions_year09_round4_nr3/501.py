#include <fstream>
#include <iomanip>
#include <algorithm>
#include <numeric>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <utility>
#include <cmath>
#include <functional>
#include <stack>
#include <set>

using namespace std;

int c[100];
int r;
int n, k;
int a[100][100];

void Go(int i)
{
	if (i == n)
	{
		int maxc = 0;
		for (int j = 0; j < n; ++j)
			maxc = max(maxc, c[j]);
		if (maxc < r) r = maxc; 
		return;
 	}
	int colors[17] = {0};
	for (int j = 0; j < i; ++j)
	{
		if (a[i][j] == 1) colors[c[j]] = 1; 
	}
	int newc = 0;
	while (colors[newc] == 1) ++newc;
	if (newc >= r) return;
	c[i] = newc;
	Go(i+1);
	++newc;
	while (colors[newc] == 1) ++newc;
	if (newc >= r) return;
	c[i] = newc;
	Go(i+1);
}

int main()
{
	ifstream ifs("c.in");
	ofstream ofs("c.out");
	int t;
	ifs >> t;
	for (int test = 0; test < t; ++test)
	{
		memset(c, -1, sizeof(c));
		memset(a, 0, sizeof(a));
		ifs >> n >> k;
		vector<vector<int> > v(n, vector<int>(k, 0));
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < k; ++j)
			{
				ifs >> v[i][j];
			}
		for (int i= 0; i < n; ++i)
			for (int j = 0; j < n; ++j)
			{
				for (int l = 0; l < k; ++l)
				{
					if (v[i][l] == v[j][l]) a[i][j] = 1;
					if (l > 0)
					{
						if (v[i][l-1] > v[j][l-1] && v[i][l] < v[j][l]) a[i][j] = 1;
						if (v[i][l-1] < v[j][l-1] && v[i][l] > v[j][l]) a[i][j] = 1;
					}
				}
			}
		int cnt = 0;
		r = n;
		//for (int j = 0; j < k; ++j)
		//{
		//	int maxn = 0;
		//	for (int i = 0; i < n; ++i)
		//	{
		//		maxn = max(maxn, v[i][j]);
		//	}
		//	for (int i = 0; i < n; ++i)
		//		if (c[i] == -1 && v[i][j] == maxn)
		//		{
		//			c[i] = cnt;
		//			++cnt;
		//		}
		//}
		Go(0);
		ofs << "Case #" << test+1 << ": " << r+1 << endl;
	}
	return 0;
}
