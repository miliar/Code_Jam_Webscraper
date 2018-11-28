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

int n, m, a;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int testNum;
	scanf("%d", &testNum);
	for (int testInd = 0; testInd < testNum; testInd++)
	{
		scanf("%d%d%d", &n, &m, &a);
		for (int x1 = 1; x1 <= n; x1++)
		{
			int x2 = 0;
			if (a % x1 > 0)
				x2 = x1 - (a % x1);
			int y1 = 1;
			int y2 = (a + x2 * y1) / x1;
			if (y2 <= m)
			{
				printf("Case #%d: %d %d %d %d %d %d\n", testInd + 1, 0, 0, x1, y1, x2, y2);
				goto next;
			}
		}
		printf("Case #%d: IMPOSSIBLE\n", testInd + 1);
		next:;
	}
	return 0;
}
