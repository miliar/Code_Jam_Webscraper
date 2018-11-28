#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <iostream>
#include <string>
#include <set>
#include <queue>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)n; ++i)

const int INF = 1000000000;


const char str[] = "welcome to code jam";
string s;

int d[1000][50];
int n, m;

int get(int pos, int cur)
{
	if (pos == n && cur == m)
		return 1;
	if (pos == n)
		return 0;

	if (d[pos][cur] != -1)
		return d[pos][cur];

	int ans = get(pos + 1, cur);
	if (cur < m && s[pos] == str[cur])
		ans += get(pos + 1, cur + 1);
	ans %= 10000;
	return d[pos][cur] = ans;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tests;
	scanf("%d\n", &tests);
	forn(test, tests)
	{
		memset(d, 255, sizeof(d));
		getline(cin, s);	
		n = (int)s.length();
		m = (int)strlen(str);
		printf("Case #%d: %4.4d\n", test + 1, get(0, 0));
	}
	

	return 0;
}

