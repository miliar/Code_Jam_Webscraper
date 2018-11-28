#include <iostream>
#include <algorithm>


const double eps = 1e-8;


using namespace std;


int speed[1000146];


bool doubleEqual(double a, double b)
{
	return fabs(a - b) < eps;
}


bool doubleMore(double a, double b)
{
	return a > b && !doubleEqual(a, b);
}


int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d", &T);
	for(int _ = 0; _ < T; _++)
	{
		fprintf(stderr, "%d\n", _);
		int x, s, r, n;
		double t;
		scanf("%d%d%d%lf%d", &x, &s, &r, &t, &n);
		for(int i = 0; i < x; i++)
			speed[i] = s;
		for(int i = 0; i < n; i++)
		{
			int b, e, w;
			scanf("%d%d%d", &b, &e, &w);
			for(int j = b; j < e; j++)
				speed[j] = w + s;
		}
		sort(speed, speed + x);
		double ans = 0;
		for(int i = 0; i < x; i++)
		{
			double curTime = 1. / (double)speed[i];
			if(doubleEqual(t, 0))
				ans += curTime;
			else
			{
				double newSpeed = speed[i] - s + r;
				double newTime = 1. / newSpeed;
				if(doubleMore(t, newTime))
				{
					t -= newTime;
					ans += newTime;
				}
				else
				{
					double possibleDist = t * newSpeed;
					ans += t + (1. - possibleDist) / (double)speed[i];
					t = 0;
				}
			}
		}
		printf("Case #%d: %.9lf\n", _ + 1, ans);
	}
}