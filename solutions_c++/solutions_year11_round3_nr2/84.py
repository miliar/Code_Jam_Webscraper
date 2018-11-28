#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std; 
__int64 A[1001000];
__int64 TA[1000100];
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("BLarge.txt","w",stdout);
	int T, tcnt = 0;
	__int64 L, t, N, C;
	scanf("%d", &T);
	while (T--)
	{
		scanf("%I64d%I64d%I64d%I64d", &L, &t, &N, &C);
		for(int i = 0; i < C; i++)
			scanf("%d", &A[i]);
		for (int i = C; i < N; i++)
			A[i] = A[i - C];
		__int64 ans = 0;
		for (int i = 0; i < N; i++)
		{
			ans += A[i];
		}
		__int64 tot = 0;
		int i;
		__int64 left;
		for (i = 0; i < N; i++)
		{
			tot += A[i];
			if (tot * 2 > t)
			{
				left = tot * 2 - t;
				break;
			}
		}
		int tn = 1;
		TA[0] = left;
		for (i++; i < N; i++)
			TA[tn++] = A[i] * 2;
		sort(TA, TA + tn);
		__int64 totBoost = 0;
		for (int i = 0; i < L && i < tn; i++)
		{
			totBoost += TA[tn - i - 1];
		}
		printf("Case #%d: %I64d\n", ++tcnt, ans * 2 - totBoost / 2);
	}	
	return 0;
}
