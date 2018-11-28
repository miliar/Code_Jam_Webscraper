#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:65000000")
#include <cstdio>
#include <algorithm>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include <set>
#include <cmath>

using namespace std;
const string FILENAME = "gcj";

int l,d,n,cnt;
char s[1000000];
char words[11000][300];
bool pattern[300][256];

int main()
{
	freopen((FILENAME + ".in").c_str(), "r", stdin);
	freopen((FILENAME + ".out").c_str(), "w", stdout);

	scanf("%d%d%d", &l, &d, &n);
	gets(s);
	for (int i=0; i<d; ++i)
		gets(words[i]);

	for (int I=1; I<=n; ++I)
	{
		gets(s);
		memset(pattern, false, sizeof pattern);
		for (int i=0, j=0; s[i]!=0 && j<l; ++j)
			if (s[i] == '(')
			{
				++i;
				while (s[i] != 0 && s[i] != ')')
					pattern[j][s[i++]] = true;
				++i;
			}
			else
				pattern[j][s[i++]] = true;

		cnt = d;
		for (int i=0; i<d; ++i)
			for (int j=0; j<l; ++j)
				if (!pattern[j][words[i][j]])
				{
					--cnt;
					break;
				}

		printf("Case #%d: %d\n", I, cnt);
	}

	return 0;
} 