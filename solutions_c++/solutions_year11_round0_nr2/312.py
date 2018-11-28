#define _CRT_SECURE_NO_DEPRECATE
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
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>

using namespace std;

#define CL(x) memset(x, 0, sizeof(x))

#define FOR(i, n) for (int i = 0; i < (int)(n); i++)

typedef long long LL;
typedef vector<int> vi;
typedef vector<string> VS;

void ASS(bool b)
{
	if (!b)
	{
		++*(int*)0;
	}
}

const int CHAR_CNT = 32;
char a[CHAR_CNT][CHAR_CNT];
char b[CHAR_CNT][CHAR_CNT];
int cnt[CHAR_CNT];

bool Ok(string s)
{
	FOR(i, s.size())
		if (s[i] < 'A' || s[i] > 'Z')
			return 0;
	return 1;
}

void Solve()
{
	CL(a);
	CL(b);
	CL(cnt);

	int t;
	cin >> t;
	string s;
	FOR(i, t)
	{
		cin >> s;
		ASS(Ok(s));
		int x = s[0] - 'A' + 1;
		int y = s[1] - 'A' + 1;
		a[x][y] = a[y][x] = s[2] - 'A' + 1;
	}
	cin >> t;
	FOR(i, t)
	{
		cin >> s;
		ASS(Ok(s));
		int x = s[0] - 'A' + 1;
		int y = s[1] - 'A' + 1;
		b[x][y] = b[y][x] = 1;
	}
	cin >> t;
	cin >> s;
	ASS(t == s.size());
	vector<char> ans;
	FOR(i, s.size())
	{
		s[i] = s[i] - 'A' + 1;
		ans.push_back(s[i]);
		cnt[ans.back()]++;
		while (ans.size() >= 2 && a[ans[ans.size() - 1]][ans[ans.size() - 2]])
		{
			char c = a[ans[ans.size() - 1]][ans[ans.size() - 2]];
			cnt[ans.back()]--;
			ans.pop_back();
			cnt[ans.back()]--;
			ans.pop_back();
			ans.push_back(c);
			cnt[ans.back()]++;
		}
		if (ans.size())
		{
			bool bad = 0;
			FOR(j, CHAR_CNT)
				if (b[ans.back()][j] && cnt[j])
					bad = 1;
			if (bad)
			{
				ans.clear();
				CL(cnt);
			}
		}
	}
	if (ans.size())
	{
		printf("[");
		FOR(i, ans.size())
		{
			if (i)
				printf(", ");
			char s[4];
			s[0] = ans[i] - 1 + 'A';
			s[1] = 0;
			printf("%s", s);
		}
		printf("]\n");
	}
	else
	{
		printf("[]\n");
	}
}

int main()
{
	freopen("c:\\my\\in.txt", "r", stdin);
	freopen("c:\\my\\out.txt", "w", stdout);
	int t;
	cin >> t;
	FOR(i, t)
	{
		printf("Case #%d: ", i + 1);
		Solve();
	}

	return 0;
}