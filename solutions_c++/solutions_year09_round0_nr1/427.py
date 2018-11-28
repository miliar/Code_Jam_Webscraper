#include <cstdio>
#include <cstring>
#include <math.h>
#include <algorithm>
#include <string>
#include <vector>
#include <cctype>
#include <bitset>
#include <sstream>
#include <set>
#include <map>

using namespace std;
template <class T> T sqr(T a) { return a * a; }
#define memfill(a, b) memset(a, b, sizeof(a))
#define pb push_back
#define vi vector<int>
#define vii vector<vector<int> >
#define vs vector<string>
#define pii pair<int, int>
#define dist(a, b) sqrt(sqr(a.x - b.x) + sqr(a.y - b.y))
#define bound(x, y, n, m) x >= 0 && y >= 0 && x < n && y < m

int l, d;
vs words;

int solve(string s, string w)
{
	int cur = 0;
	for (int i = 0; i < l; i++)
	{
		int fail = 1;
		if (s[cur] == '(')
		{
			cur++;
			while (s[cur] != ')')
			{
				if (s[cur] == w[i])
					fail = 0;
				cur++;
			}
			cur++;
		}
		else
		{
			fail = s[cur] != w[i];
			cur++;
		}
		if (fail)
			return 0;
	}
	return 1;
}

int solve(string s)
{
	int res = 0;
	for (int i = 0; i < d; i++)
		res += solve(s, words[i]);
	return res;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int testNum;
	scanf("%d%d%d", &l, &d, &testNum);
	char s[1000];
	for (int i = 0; i < d; i++)
	{
		scanf("%s", s);
		string sss = s;
		words.pb(sss);
	}
	for (int testCount = 0; testCount < testNum; testCount++)
	{
		scanf("%s", s);
		string sss = s;
		printf("Case #%d: %d\n", testCount + 1, solve(sss));
	}
	return 0;
}