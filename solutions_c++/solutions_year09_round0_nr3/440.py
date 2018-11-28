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

char s[900];
char t[40];
int a[900][40];

int solve()
{
	int sl = strlen(s);
	int tl = strlen(t);
	for (int i = 0; i <= sl; i++)
	{
		for (int j = 0; j <= tl; j++)
		{
			if (j == 0)
				a[i][j] = 1;
			else if (i == 0)
				a[i][j] = 0;
			else
				a[i][j] = (a[i - 1][j] + a[i - 1][j - 1] * (s[i - 1] == t[j - 1])) % 10000;
			//printf("%d ", a[i][j]);
		}
		//printf("\n");
	}
	return a[sl][tl];
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int testNum;
	scanf("%d", &testNum);
	gets(s);
	strcpy(t, "welcome to code jam");
	for (int testCount = 0; testCount < testNum; testCount++)
	{
		gets(s);
		char ss[9];
		int rres = solve() + 10000;
		sprintf(ss, "%d", rres);
		printf("Case #%d: %s\n", testCount + 1, ss + 1);
	}
	return 0;
}