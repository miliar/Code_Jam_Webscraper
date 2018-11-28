#pragma comment (linker, "/STACK:16000000")
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

int getmin(int a, int b)
{
	if (a == -1 || b == -1)
		return max(a, b);
	return min(a, b);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int testNum;
	scanf("%d", &testNum);
	int res[12][2000][12];
	for (int testCount = 0; testCount < testNum; testCount++)
	{
		int p;
		scanf("%d", &p);
		int n = 1 << p;
		int m[2000];
		for (int i = 0; i < n; i++)
			scanf("%d", &m[i]);
		memset(res, -1, sizeof(res));
		for (int i = 0; i < n; i++)
			for (int j = 0; j <= m[i]; j++)
				res[0][i][j] = 0;
		for (int i = 1; i <= p; i++)
			for (int j = 0; j < (1 << (p - i)); j++)
			{
				int cost;
				scanf("%d", &cost);
				int r = -1;
				for (int ii = p; ii >= 0; ii--)
				{
					if (res[i - 1][j * 2][ii] + 1 && res[i - 1][j * 2 + 1][ii] + 1)
						res[i][j][ii] = getmin(res[i][j][ii], res[i - 1][j * 2][ii] + res[i - 1][j * 2 + 1][ii] + cost);
					if (res[i - 1][j * 2][ii + 1] + 1 && res[i - 1][j * 2 + 1][ii + 1] + 1)
						res[i][j][ii] = getmin(res[i][j][ii], res[i - 1][j * 2][ii + 1] + res[i - 1][j * 2 + 1][ii + 1]);
					r = getmin(r, res[i][j][ii]);
					res[i][j][ii] = getmin(r, res[i][j][ii]);
				}
			}
		printf("Case #%d: %d\n", testCount + 1, res[p][0][0]);
	}
	return 0;
}