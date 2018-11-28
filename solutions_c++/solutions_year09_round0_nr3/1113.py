#include <iostream>
#include <fstream>
#include <cstdio>
#include <set>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <string>

using namespace std;

string s;

void Load()
{
	s = "";
	char c = getchar();
	while (! ((c == 10) || (c == EOF)))
	{
		s += c;
		c = getchar();
	}
}

const int MOD = 10000;
int res[510][510];
string t;

void Solve()
{
	t = "welcome to code jam";
	memset(res, 0, sizeof(res));
	res[0][0] = 1;
	int i, j;
	for (i = 0; i <= s.length(); i++)
	{
		for (j = 0; j <= t.length(); j++)
		{
			if (i != s.length())
			{
				res[i + 1][j] += res[i][j];
				res[i + 1][j] %= MOD;
			}
			if (j != t.length() && i != s.length())
			{
				if (s[i] == t[j])
				{
					res[i + 1][j + 1] += res[i][j];
					res[i + 1][j + 1] %= MOD;
				}
			}
		}
	}
	int q = res[s.length()][t.length()];
	if (q < 10) printf("0");
	if (q < 100) printf("0");
	if (q < 1000) printf("0");
	printf("%d", q);
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int nt, it;
	scanf("%d", &nt);
	char c = getchar();
	while (c != 10) c = getchar();
	for (it = 0; it < nt; it++)
	{
		printf("Case #%d: ", it + 1);
		Load();
		Solve();
		printf("\n");
	}
	return 0;
}