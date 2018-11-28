#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std; 
__int64 gcd(__int64 a, __int64 b)
{
	if (b)
		return gcd(b, a % b);
	return a;
}
int main()
{
	int T, tcnt = 0;
	freopen("A-large.in", "r", stdin);
	freopen("a.txt", "w", stdout);
	scanf("%d", &T);
	while (T--)
	{
		__int64 N, PD, PG;
		scanf("%I64d%I64d%I64d", &N, &PD, &PG);
		if (PD != 100 && PG == 100 || PD != 0 && PG == 0)
		{
			printf("Case #%d: Broken\n", ++tcnt);
		}
		else
		{
			__int64 g = gcd(PD, 100);
			g = 100 / g;
			if (g > N)
			{
				//printf("%d %d %d %d ", N, PD, PG, g);
				printf("Case #%d: Broken\n", ++tcnt);
				
			}
			else
			{
				//printf("%d %d %d ", N, PD, PG);
				printf("Case #%d: Possible\n", ++tcnt);
			}
		}
	}
	return 0;
}
