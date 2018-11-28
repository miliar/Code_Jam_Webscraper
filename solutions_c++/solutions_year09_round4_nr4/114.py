#include <cstdio>
#include <cmath>

int Tests, Cases;
int N;
double X[10], Y[10], R[10];
double Ans, Tmp;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d", &Tests);
	for (int Cases = 1; Cases <= Tests; ++ Cases)
	{
		scanf("%d", &N);
		for (int i = 0; i < N; ++ i)
			scanf("%lf %lf %lf", &X[i], &Y[i], &R[i]);
		if (N == 1)
		{
			printf("Case #%d: %.6lf\n", Cases, R[0]);
			continue;
		}
		if (N == 2)
		{
			Ans = R[0] > R[1] ? R[0] : R[1];
		printf("Case #%d: %.6lf\n", Cases, Ans);
			continue;
		}
		Ans = 1E10;
		for (int i = 0; i < N; ++ i)
			for (int j = i + 1; j < N; ++ j)
			{
				int k = 0;
				for (int k = 0; k < N; ++ k)
					if (k != i && k != j) break;
				Tmp = sqrt((X[i] - X[j]) * (X[i] - X[j]) + (Y[i] - Y[j]) * (Y[i] - Y[j])) + R[i] + R[j];
				if (2 * R[k] > Tmp) Tmp = 2 * R[k];
				if (Ans > Tmp) Ans = Tmp;
			}
		printf("Case #%d: %.6lf\n", Cases, Ans / 2);
	}
}
