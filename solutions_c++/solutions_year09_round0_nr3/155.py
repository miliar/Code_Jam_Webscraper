#include <string>
#include <vector>
#include <map>
#include <list>
#include <set>
#include <queue>
#include <iostream>
#include <sstream>
#include <stack>
#include <deque>
#include <cmath>
#include <memory.h>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <utility>

using namespace std;

#define INF (2000000000)

const int nmax = 700;
const int mmax = 20;
const int modulo = 10000;

int a[nmax][mmax];

string pattern = "welcome to code jam";
int x = (int)pattern.size();

string s;

void solve(int t)
{
	int i, n = (int)s.size();
	int j, k;
	a[0][0] = 1;
	for(i = 0; i < n; ++i)
	{
		for(j = 0; j < x; ++j)
		{
			if (s[i] == pattern[j])
			{
				for(k = 0; k <= i; ++k)
				{
					a[i + 1][j + 1] += a[k][j];
					a[i + 1][j + 1] %= modulo;
				}
			}
		}
	}
	int ans = 0;
	for(i = 0; i < n; ++i)
	{
		ans += a[i + 1][x];
		ans %= modulo;
	}
	printf("Case #%d: %04d\n", t, ans);
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int i, n;
	scanf("%d", &n);
	getline(cin, s);
	for(i = 0; i < n; ++i)
	{
		memset(a, 0, sizeof(a));
		getline(cin, s);
		solve(i + 1);
	}
	return 0;
}