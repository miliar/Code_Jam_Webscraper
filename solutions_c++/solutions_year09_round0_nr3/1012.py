#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <string>

#define pb push_back
#define mp make_pair
#define sz(v) ((int)(v).size())
#define all(v) (v).begin(),(v).end()

using namespace std;

typedef pair<int, int> ii;
typedef long long int64;
typedef vector<int> vi;

const int mod = 10000;

char s1[10000];
char s2[1000] = "welcome to code jam";

int d[1000][100];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	gets(s1);
	int nc;
	sscanf(s1, "%d", &nc);
	for (int it = 0; it < nc; it++)
	{
		gets(s1);
		memset(d, 0, sizeof(d));
		int n = strlen(s1), m = strlen(s2);
		for (int i = 0; i <= n; i++)
			d[i][0] = 1;
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= m; j++)
			{
				d[i][j] = d[i - 1][j];
				if (s1[i - 1] == s2[j - 1])
					d[i][j] += d[i - 1][j - 1];
				d[i][j] %= mod;
			}
		printf("Case #%d: %.4d\n", it + 1, d[n][m]);
	}
	return 0;
}
