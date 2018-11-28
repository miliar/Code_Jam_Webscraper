#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

#define EPS 1e-4

double dis(int x1, int y1, int x2, int y2)
{
	return sqrt(double((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)));
}

double area(int x1, int y1, int x2, int y2, int x3, int y3)
{
	double a = dis(x1, y1, x2, y2);
	double b = dis(x1, y1, x3, y3);
	double c = dis(x3, y3, x2, y2);
	if (a + b > c && a + c > b && b + c > a)
	{
		double p = (a + b + c) / 2;
		return sqrt(p * (p - a) * (p - b) * (p - c));
	}
	else
		return 0.;
}

int main()
{
	int T, t;
	int N, M, A;
	int x1, y1, x2, y2, x3, y3;
	scanf("%d", &T);
	for (t = 1; t <= T; t++)
	{
		scanf("%d %d %d", &N, &M, &A);
		if (N * M < A) goto imp;
				for (x2 = 0; x2 <= N; x2++)
					for (y2 = 0; y2 <= M; y2++)
						for (x3 = x2; x3 <= N; x3++)
							for (y3 = y2; y3 <= M; y3++)
							{
								double a1 = area(0, 0, x2, y2, x3, y3);
								double a2 = area(N, 0, x2, y2, x3, y3);
								double a3 = area(0, M, x2, y2, x3, y3);
								double a4 = area(N, M, x2, y2, x3, y3);
								if (fabs(a1 * 2 - A) < EPS)
								{
									printf("Case #%d: %d %d %d %d %d %d\n", t, 0, 0, x2, y2, x3, y3);
									goto next;
								}
								else if (fabs(a2 * 2 - A) < EPS)
								{
									printf("Case #%d: %d %d %d %d %d %d\n", t, N, 0, x2, y2, x3, y3);
									goto next;
								}
								else if (fabs(a3 * 2 - A) < EPS)
								{
									printf("Case #%d: %d %d %d %d %d %d\n", t, 0, M, x2, y2, x3, y3);
									goto next;
								}
								else if (fabs(a4 * 2 - A) < EPS)
								{
									printf("Case #%d: %d %d %d %d %d %d\n", t, N, M, x2, y2, x3, y3);
									goto next;
								}
							}
imp:
		printf("Case #%d: IMPOSSIBLE\n", t);
next:;
	}
	return 0;
}