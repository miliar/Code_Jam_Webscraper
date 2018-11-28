#define _CRT_SECURE_NO_DEPRECATE
#define _USE_MATH_DEFINES

#include <cstdlib>
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <string>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <queue>

using namespace std;

typedef long long int64;
typedef pair<int,int> pii;
typedef vector<int> vi;

int nt;
int n, m;
string d[1 << 7];
string e[1 << 7];
int good[1 << 7];

inline int check(string &s1, string &s2)
{
	if ((int)s1.length() != (int)s2.length()) return 0;
	int l = (int)s1.length();
	for (int i = 0; i < l; ++i)
	{
		if (s1[i] == '_') continue;
		if (s1[i] != s2[i]) return 0;
	}
	return 1;
}

inline int play(int x, int y)
{
	string s = e[y];
	
	int l = (int)d[x].length();

	int vars = 0;
	for (int i = 0; i < n; ++i)
	{
		good[i] = 0;
		if ((int)d[i].length() == l)
		{
			good[i] = 1;
			++vars;
		}
	}

	if (vars == 1) return 0;

	int res = 0;
	for (int j = 0; j < 26; ++j)
	{
		int was = 0;
		for (int i = 0; i < n; ++i)
		{
			if (!good[i]) continue;
			if (d[i].find(s[j]) == -1) continue;
			was = 1;
			break;
		}

		if (!was) continue;

		int curX = 0;
		for (int i = 0; i < l; ++i)
		{
			if (d[x][i] == s[j]) curX += (1 << i); 
		}

		if (curX == 0) ++res;

		vars = 0;
		for (int i = 0; i < n; ++i)
		{
			if (!good[i]) continue;
			
			int curI = 0;
			for (int t = 0; t < l; ++t)
			{
				if (d[i][t] == s[j]) curI += (1 << t); 
			}

			if (curX == curI)
				++vars;
			else
				good[i] = 0;
		}

		if (vars == 1) return res;
	}

	return res;
}

inline void solve()
{
	cin >> n >> m;
	for (int i = 0; i < n; ++i)
		cin >> d[i];
	for (int i = 0; i < m; ++i)
		cin >> e[i];

	for (int j = 0; j < m; ++j)
	{
		int best = -1;
		int g = -1;
		for (int i = 0; i < n; ++i)
		{
			int cur = play(i, j);
			if (cur > best)
			{
				best = cur;
				g = i;
			}
		}
		if (j) cout << " ";
		cout << d[g];
	}
}

int main()
{
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);

	cin >> nt;
	for (int tn = 1; tn <= nt; ++tn)
	{
		cout << "Case #" << tn << ": ";
		solve();
		cout << endl;
	}

	return 0;
}