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
const string FILENAME = "awe";
const int BIG = 99999;

char a[510];
char b[] = "welcome to code jam";
int alen, blen;

int tab[510][20];

int getCount(int i, int j)
{
	int &res = tab[i][j];
	if (res != -1)
		return res;
	if (i == alen || j == blen)
	{
		res = j == blen ? 1 : 0;
	}
	else
	{
		res = getCount(i + 1, j);
		if (a[i] == b[j])
		{
			res += getCount(i + 1, j + 1);
			if (res >= 10000)
				res -= 10000;
		}
	}
	return res;
}

int main()
{
	freopen((FILENAME + ".in").c_str(), "r", stdin);
	freopen((FILENAME + ".out").c_str(), "w", stdout);
	int N;
	scanf("%d\n", &N);
	for (int tc = 0; tc < N; ++tc)
	{
		gets(a);
		memset(tab, -1, sizeof tab);
		alen = (int)strlen(a);
		blen = (int)strlen(b);
		printf("Case #%d: %04d\n", tc + 1, getCount(0, 0));
	}

	return 0;
}