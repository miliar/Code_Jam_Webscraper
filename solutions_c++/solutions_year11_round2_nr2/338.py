#include <cstdio>
#include <algorithm>
using namespace std;

const long long infinity = 1000000000000000LL;

int main()
{
	int T;
	scanf("%d", &T);
	for (int Ti = 1; Ti <= T; Ti++)
	{
		//input
		int C;
		long long D;
		scanf("%d %lld", &C, &D);
    D *= 2;
		
		long long P[C];
		int V[C];
		for (int i = 0; i < C; i++)
		{
			scanf("%lld %d", &P[i], &V[i]);
			P[i] *= 2;
		}
		
		//binary search the time
		long long a = 0;
		long long b = infinity;
		
		//b = 12;
		
		do
		{
			long long t = (a + b) / 2;
			
			//check
			bool ok = true;
			long long last = -infinity;
			for (int i = 0; i < C; i++)
			{
				if ((last + D * V[i] > P[i] + t) || (D * (V[i] - 1) > 2 * t))
				{
					ok = false;
					//printf("i = %d %d %d\n", i, last + D * V[i] > P[i] + t, D * V[i] > 2 * t);
					break;
				}
				last = max(last + D * V[i], P[i] - t + D * (V[i] - 1));
				//printf("last = %lld\n", last);
			}
			
			//printf("<%lld ; %lld> %lld -> %d\n", a, b, t, ok);
			
			if (ok)
				b = t - 1;
			else
				a = t + 1;
		}
		while (a <= b);
			
		//output
		printf("Case #%d: %f\n", Ti, 0.5 * a);
	}
	return 0;
}