#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>
#include <set>
#include <stack>
#include <string.h>
#include <algorithm>
#define FOREACH(it, C) for(typeof((C).begin()) it = (C).begin(); it != (C).end(); ++it)
using namespace std;
const int INF = 1000000100, N = 110;
typedef long long int LL;
int t, n, ans, r;
string chuj;
vector<string> d;
bool same(int x1, int y1, int x2, int y2)
{
	if(x1 < 0 || x1 >= d.size() || y1 < 0 || y1 >= d[x1].size() || d[x1][y1] == ' ')
		return true;
	if(x2 < 0 || x2 >= d.size() || y2 < 0 || y2 >= d[x2].size() || d[x2][y2] == ' ')
		return true;
	return (d[x1][y1] == d[x2][y2]);
}
bool check(int x, int y)
{
	for(int i = 0; i <= 2 * n; ++i)
		for(int j = 0; j <= 2 * n; ++j)
			if(!same(x - i, y - j, x + i, y - j) || !same(x - i, y + j, x + i, y + j) || !same(x - i, y - j, x - i, y + j) || !same(x + i, y - j, x + i, y + j))
				return false;
	return true;
}
int main()
{
	cin >> t;
	for(int testCase = 1; testCase <= t; ++testCase)
	{
		ans = INF;
		cin >> n;
		getline(cin, chuj);
		d.resize(2 * n - 1);
		for(int i = 0; i < 2 * n - 1; ++i)
			getline(cin, d[i]);
		for(int i = -1; i <= 2 * n - 1; ++i)
			for(int j = -1; j <= 2 * n - 1; ++j)
				if(check(i, j))
				{
					r = abs(i - n + 1) + abs(j - n + 1) + n;
			//		cout << i << " " << j << " " << r << endl;
					ans = min(ans, r * r - n * n);
				}
		cout << "Case #" << testCase << ": " << ans << endl;
	}
}
/*
2
2
 1
2 3
 4
*/
