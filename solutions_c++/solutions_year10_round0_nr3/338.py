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

const int maxn = 10000;

int r, k, n;
int g[maxn];
int64 sum;

int next[maxn];
int64 d[maxn];

void calc(int ind, int64 x)
{
	d[ind] = 0;
	int cur = ind;
	while (x >= g[cur])
	{
		x -= g[cur];
		d[ind] += g[cur];
		cur = (cur + 1) % n;
		if (cur == ind) break;
	}
	next[ind] = cur;
}

void Solve()
{
	cin >> r >> k >> n;
	sum = 0;
	for (int i = 0; i < n; i++)
	{
		cin >> g[i];
		sum += g[i];
	}
	for (int i = 0; i < n; i++)
		calc(i, k);
	int64 res = 0;
	int cur = 0;
	for (int i = 0; i < r; i++)
	{
		res += d[cur];
		cur = next[cur];
	}
	cout << res << "\n";
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
