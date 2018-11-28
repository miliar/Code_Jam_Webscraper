#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
using namespace std;

#define for_each(it, v) for (typeof((v).begin()) it = (v).begin(); it != (v).end(); ++it)

const char* PATTERN = "welcome to code jam";
const int MAX_M = 20;
const int MAX_N = 501;

int testNum;
int n, m;
int f[MAX_N][MAX_M];
char buf[MAX_N];
int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C.out", "w", stdout);
	gets(buf);
	sscanf(buf, "%d", &testNum);
	m = strlen(PATTERN);
	for (int k = 0; k < testNum; k++)
	{
		gets(buf);
		n = strlen(buf);
		memset(f, 0, sizeof(f));
		for (int i = 0; i <= n; i++)
		{
			f[i][0] = 1;
			for (int j = 1; j <= m; j++)
				if (i > 0)
				{
					f[i][j] = f[i - 1][j];
					if (buf[i - 1] == PATTERN[j - 1])
						f[i][j] = (f[i][j] + f[i - 1][j - 1]) % 10000;
				}
		}
		printf("Case #%d: %.4d\n", k + 1, f[n][m] % 10000);
	}
	return 0;
}
