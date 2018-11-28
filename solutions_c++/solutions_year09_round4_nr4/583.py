#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>

using namespace std;

int pl[3][100];

double r(int a, int b, int r)
{
	double dx = pl[0][a]-pl[0][b];
	dx *= dx;
	double dy = pl[1][a]-pl[1][b];
	dy *= dy;
	double d = (sqrt(dx+dy)+pl[2][a]+pl[2][b])/2.0;
	return max(d,(double)pl[2][r]);
}
int main()
{
	freopen("D-small-attempt1.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int C;
	scanf("%d", &C);
	for (int cc=1; cc<=C; cc++)
	{
		int N;
		scanf("%d", &N);
		for (int i=0; i<N; i++)
		{
			scanf("%d%d%d", &pl[0][i], &pl[1][i], &pl[2][i]);
		}

		double res = 10000000;

		if (N == 3)
		{
			res = min(res, r(0,1,2));
			res = min(res, r(0,2,1));
			res = min(res, r(1,2,0));
		}
		if (N == 1)
			res = pl[2][0];
		if (N == 2)
			res = max(pl[2][0], pl[2][1]);

		printf("Case #%d: %lf\n", cc, res);
	}


	return 0;
}