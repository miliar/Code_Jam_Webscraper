#include <math.h>
#include <stdio.h>
#include <algorithm>

using namespace std;

long long sqr(int x) 
{
	return (long long)x * x;
}

int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);


    int testcases;
	scanf("%d", &testcases);

	for (int cases = 1; cases <= testcases; cases++)
	{
		int N;

		scanf("%d", &N);
		int x, vx, y, vy, z, vz;

		x = 0; vx = 0;
		y = 0; vy = 0;
		z = 0; vz = 0;

		for (int i = 0; i < N; i++)
		{
			int tmp;
		    scanf("%d", &tmp);
			x += tmp;

			scanf("%d", &tmp);
			y += tmp;

			scanf("%d", &tmp);
			z += tmp;

			scanf("%d", &tmp);
			vx += tmp;

			scanf("%d", &tmp);
			vy += tmp;

			scanf("%d", &tmp);
			vz += tmp;
		}

		long long a = sqr(vx) + sqr(vy) + sqr(vz);
		long long b = (long long)2 * x * vx + (long long)2 * y * vy + (long long)2 * z * vz;
		long long c = sqr(x) + sqr(y) + sqr(z);

		double t, d ,tmp;

		if (a == 0) 
		{
			t = 0;
			d = sqrt((double)c) / N;
		}
		else 
		{
			t = -b / ((double)2 * a);
			if (t < 0) t = 0;

            tmp = a * t * t + b * t + c;
		
			if (tmp >= 0)
			{
				d = sqrt(tmp) / N;
			}
			else 
			{
				tmp = sqr(b) - 4 * a * c;
                t = (-b - tmp) / (2 * a);
				if (t < 0) t = 0;
            
				tmp = a * t * t + b * t + c;
				if (tmp < 0) tmp = 0;
			    d = sqrt(tmp) / N;
			}
		}

		printf("Case #%d: %.8lf %.8lf\n", cases, d, t);
	}

	return 0;
}
