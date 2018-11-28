#include <iostream>
#include <cmath>
#include <deque>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <bitset>

using namespace std;

int		N, M, A;

int	main()
{
	int nCase;
	scanf("%d", &nCase);
	for (int nowCase = 1; nowCase <= nCase; ++nowCase)
	{
		scanf("%d%d%d", &N, &M, &A);
		
		int x1, y1, x2, y2;
		if (N * M < A)
			printf("Case #%d: IMPOSSIBLE\n", nowCase);
		else
		{
			x1 = N;
			y2 = (A - 1) / N + 1;
			x2 = x1 * y2 - A;
			y1 = 1;
			printf("Case #%d: %d %d %d %d %d %d\n", nowCase, 0, 0, x1, y1, x2, y2);
		}
	}
	return 0;
}
