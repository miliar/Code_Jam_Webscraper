#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std; 
int P[210], V[210];
int main()
{
	int T, tcnt = 0;
	freopen("B-small-attempt3.in", "r", stdin);
	freopen("b.txt", "w", stdout);
	scanf("%d", &T);
	while (T--)
	{
		int C, D;
		scanf("%d%d", &C, &D);
		double totV = 0;
		for (int i = 0; i < C; i++)
		{
			scanf("%d%d", &P[i], &V[i]);
			totV += V[i];
		}
		if (C == 1 && V[0] == 1)
		{
			
		}
		double l = 0, r = 1e10;
		//if (r < totV * D)
		r = totV * D + 10;
		//r = 1;
		while (fabs(l - r) > 1e-12)
		{
			double mid = (l + r) / 2;
			int flag = 0;
			double left = P[0] - mid, right = P[C - 1] + mid;
			int i, j;
			for (i = 0, j = C - 1; i < j; i++, j--)
			{
				if (P[i] - mid > left)
					left = P[i] - mid;
				if (P[j] + mid < right)
					right = P[j] + mid;
				left += D * (V[i] - 1);
				right -= D * (V[j] - 1);
				if (fabs(left - P[i]) > mid || fabs(right - P[j]) > mid || left + D > right)
				{
					flag = 1;
					break;
				}
				left += D;
				right -= D;
			}
			if (i == j && (right - left < D * (V[i] - 1) || 2 * mid < D * (V[i] - 1)))
				flag = 1;
			if (flag == 1)
				l = mid;
			else
				r = mid;
		}
		printf("Case #%d: %.10lf\n", ++tcnt, l);
	}
	return 0;
}
