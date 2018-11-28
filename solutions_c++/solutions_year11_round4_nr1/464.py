#include <cstdio>
#include <algorithm>
using namespace std;

int X, S, R, N;
double t;
double L[109]; //length for each speed w_i

int main()
{
	int T;
	scanf("%d", &T);
	for (int Ti = 1; Ti <= T; Ti++)
	{
		//init
		for (int i = 0; i <= 100; i++)
			L[i] = 0;
		
		//input
		scanf("%d %d %d %lf %d", &X, &S, &R, &t, &N);
		L[0] = X;
		for (int i = 0; i < N; i++)
		{
			int b, e, w;
			scanf("%d %d %d", &b, &e, &w);
			L[w] += e - b;
			L[0] -= e - b;
		}
		
		//greedy
		double time = 0;
		for (int i = 0; i <= 100; i++)
			if (L[i] > 0)
			{
				//run the whole time
				if ((t > 0) && (L[i] <= t * (i + R)))
				{
					t -= 1.0 * L[i] / (i + R);
					time += 1.0 * L[i] / (i + R);
				}
				//run + walk
				else
				{
					if (t > 0)
					{
						//run
						L[i] -= t * (i + R);
						time += t;
						t = 0;
					}
					
					//walk
					time += 1.0 * L[i] / (i + S);
				}
			}

		//output
		printf("Case #%d: %.10f\n", Ti, time);
	}
	return 0;
}