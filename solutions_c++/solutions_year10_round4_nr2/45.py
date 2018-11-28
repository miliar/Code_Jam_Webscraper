#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <cstring>
#include <cstdio>
#include <cassert>
#include <queue>
#include <bitset>
//#include <cmath>
#include <sstream>
#include <string>
#include <vector>

#define pb push_back
#define sz(v) ((int)(v).size())
#define all(v) (v).begin(),(v).end()

using namespace std;

typedef pair<int, int> ii;
typedef long long int64;
typedef vector<int> vi;

template<class T> T abs(T x) {return x > 0 ? x : (-x); }
template<class T> T sqr(T x) {return x * x; }

const int inf = 1000000000;

int m[1000000];
vi pr[20];
vi mx[20];

vi d[20][20];
int n;

int go(int cur, int l, int v)
{
	if (l == n)
	{
		if (cur > m[v]) return inf;
		return 0;
	}
	int& res = d[cur][l][v];
	if (res != -1) return res;
	//if (cur > mx[l][v]) return res = inf;
	res = pr[l][v] + go(cur, l + 1, 2 * v) + go(cur, l + 1, 2 * v + 1);
	res = min(res, go(cur + 1, l + 1, 2 * v) + go(cur + 1, l + 1, 2 * v + 1));
	res = min(res, inf);
	return res;
}

void Solve()
{
	cin >> n;
	for (int i = 0; i < (1 << n); i++)
		cin >> m[i];
	for (int i = n - 1; i >= 0; i--)
	{
		int s = 1 << i;
		pr[i] = vi(s);
		for (int j = 0; j < s; j++)
			cin >> pr[i][j];
		mx[i] = vi(s, 0);
		for (int j = 0; j <= n; j++)
			d[j][i] = vi(s, -1);
	}
	for (int i = 0; i < (1 << n); i++)
	{
		int x = m[i], y = i, z = n;
		while (z)
		{
			y /= 2, z--;
			mx[z][y] = max(mx[z][y], x);
		}
	}
	cout << go(0, 0, 0) << "\n";
}

int main()
{
	int nc;
	cin >> nc;
	for (int it = 0; it < nc; it++)
	{
		printf("Case #%d: ", it + 1);
		Solve();
	}
	return 0;
}
