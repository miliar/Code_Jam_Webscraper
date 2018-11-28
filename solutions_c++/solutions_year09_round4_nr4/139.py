#include <iostream>
#include <cmath>

using namespace std;

const int MaxN = 5;

int N, TCase;
double Ans, X[MaxN], Y[MaxN], R[MaxN];

double work(int x)
{
	int a = 0, b = 0;
	if (x == 1) a = 2, b = 3;
	else if (x == 2) a = 1, b = 3;
	else a = 1, b = 2;
	double Res = (sqrt((X[a] - X[b]) * (X[a] - X[b]) + (Y[a] - Y[b]) * (Y[a] - Y[b])) + R[a] + R[b]) / 2;
	Res = max(Res, R[x]);
	return Res;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &TCase);
	for (int Case = 1; Case <= TCase; ++Case)
	{
		scanf("%d", &N);
		for (int i = 1; i <= N; i++)
			scanf("%lf%lf%lf", &X[i], &Y[i], &R[i]);
		Ans = 1e10;
		if (N == 3)
			for (int i = 1; i <= N; i++)
				Ans = min(Ans, work(i));
		if (N == 1) Ans = R[1];
		if (N == 2) Ans = max(R[1], R[2]);
		
		printf("Case #%d: %.8lf\n", Case, Ans);
	}
	return 0;
}
