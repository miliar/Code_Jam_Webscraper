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

const int MAX_N = 100;
const int MAX_LEN = 128;
const int MAX_M = 1000;
const int INF = 100000;

int n, m;
int f[MAX_M][MAX_N];
char name[MAX_N][MAX_LEN];
char query[MAX_M][MAX_LEN];
char buffer[MAX_LEN];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int testNum;
	scanf("%d", &testNum);
	for (int testInd = 0; testInd < testNum; testInd++)
	{
		scanf("%d", &n);
		gets(buffer);
		for (int i = 0; i < n; i++)
			gets(name[i]);
		scanf("%d", &m);
		gets(buffer);
		for (int i = 0; i < m; i++)
			gets(query[i]);
		for (int i = 0; i < m; i++)
			for (int j = 0; j < n; j++)
				if (strcmp(name[j], query[i]) == 0)
					f[i][j] = INF;
				else if (i == 0)
					f[i][j] = 0;
				else
				{
					f[i][j] = INF;
					for (int k = 0; k < n; k++)
						f[i][j] = min(f[i][j], f[i - 1][k] + (j != k));
				}
		printf("Case #%d: %d\n", testInd + 1, *min_element(f[m - 1], f[m - 1] + n));
	}
	return 0;
}
