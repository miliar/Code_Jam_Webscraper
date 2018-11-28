#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <map>
#include <cstdio>
#include <set>
#include <stack>
#include <vector>
#include <algorithm>
#include <cmath>
#include <memory>
#include <queue>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)n; i++)
#define forv(i, v) forn(i, v.size())
#define all(v) v.begin(), v.end()

typedef long double ld;
typedef long long int64;
typedef pair<ld, ld> pt;

#define X first
#define Y second
#define pb push_back
#define mp make_pair
#define y1 PALEVO

string tmp = "welcome to code jam";

int ans[20];

int main()
{
	
	int t;
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	scanf("%d\n", &t);
	for (int test = 0; test < t; test++)
	{
		string s;
		getline(cin, s);
		memset(ans, 0, sizeof ans);
		ans[0] = 1;
		for (int i = 0; i < (int)s.size(); i++)
		{
			for (int j = 18; j >= 0; --j)
			{
				if (s[i] == tmp[j])
				{
					ans[j + 1] = (ans[j + 1] + ans[j]) % 10000;
				}
			}
		}
		printf("Case #%d: %04d\n", test + 1, ans[19]);
	}
	return 0;
}

