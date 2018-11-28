#include <cassert>
#include <cstdio>
#include <ctime>
#include <cstdlib>
#include <climits>
#include <cstddef>
#include <cctype>
#include <cmath>
#include <cstring>
#include <fstream>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <iterator>
#include <numeric>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <vector>
#include <bitset>
#include <list>
#include <string>
#include <functional>
#include <utility>
using namespace std;
typedef long long llint;
int const N = 10000;
int n;
int d[N + 1], l[N + 1];
int u[N + 1];
bool readin()
{
	if (scanf("%d", &n) == EOF)
	{
		return false;
	}
	for (int i = 0; i < n; ++i)
	{
		scanf("%d%d", &d[i], &l[i]);
	}
	scanf("%d", &d[n]);
	l[n] = INT_MAX;
	return true;
}
bool solve()
{
	memset(u, -1, sizeof(u));
	u[0] = d[0];
	for (int i = 0; i < n; ++i)
	{
		if (u[i] == -1)
		{
			continue;
		}
		int t = lower_bound(d, d + (n + 1), d[i] + u[i] + 1) - d;
		for (int j = i + 1; j < t; ++j)
		{
			u[j] = max(u[j], min(l[j], d[j] - d[i]));
		}
	}
	return u[n] != -1;
}
int main()
{
	int tc;
	scanf("%d", &tc);
	for (int cc = 1; cc <= tc; ++cc)
	{
		readin();
		printf("Case #%d: %s\n", cc, solve() ? "YES" : "NO");
	}
	return 0;
}

