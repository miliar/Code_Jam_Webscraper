#include <iostream>
#include <cmath>

using namespace std;

int C;
int N;
int X[64];
int Y[64];
int R[64];

double eval(int x1, int y1, int r1, int x2, int y2, int r2)
{
	return (hypot(x1 - x2 + 0.0, y1 - y2 + 0.0) + r1 + r2) / 2.0;
}

double minRadius()
{
	if (N == 1)
		return R[0];
	else if (N == 2)
		return max(R[0], R[1]);
	else 
		return min(min(max(eval(X[0], Y[0], R[0], X[1], Y[1], R[1]), R[2] + 0.0), max(eval(X[0], Y[0], R[0], X[2], Y[2], R[2]), R[1] + 0.0)), max(eval(X[2], Y[2], R[2], X[1], Y[1], R[1]), R[0] + 0.0));
}

int main()
{
	scanf("%d", &C);
	for (int ncase = 1; ncase <= C; ++ncase) {
		scanf("%d", &N);
		for (int i = 0; i < N; ++i)
			scanf("%d %d %d", &X[i], &Y[i], &R[i]);
		printf("Case #%d: %.7f\n", ncase, minRadius());
	}
	return 0;
}
