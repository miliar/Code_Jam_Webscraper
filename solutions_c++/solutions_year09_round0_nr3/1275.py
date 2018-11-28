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

int N,n,m;
char s1[1000];
char s2[1000] = "welcome to code jam";
int a[1000][1000];


int main()
{
	freopen((FILENAME + ".in").c_str(), "r", stdin);
	freopen((FILENAME + ".out").c_str(), "w", stdout);

	scanf("%d", &N);
	gets(s1);
	for (int I=1; I<=N; ++I)
	{
		gets(s1);
		n = (int)strlen(s1);
		m = (int)strlen(s2);
		memset(a, 0, sizeof a);

		for (int i=0; i<=n; ++i)
			a[i][0] = 1;
		for (int i=1; i<=n; ++i)
			for (int j=1; j<=m; ++j)
			{
				a[i][j] = a[i-1][j];
				if (s1[i-1] == s2[j-1])
					a[i][j] = (a[i][j] + a[i-1][j-1]) % 10000;
			}

		printf("Case #%d: %04d\n", I, a[n][m]);
	}

	return 0;
} 