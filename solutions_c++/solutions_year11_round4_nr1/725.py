#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int MaxN = 1000 + 10;

int Length, NormalV, RunV, RunTime, N;
int L[MaxN], W[MaxN];

struct TInterval
{
	int Len, W;
};

TInterval F[MaxN];

bool operator < (const TInterval& A, const TInterval& B)
{
	return A.W < B.W;
}

double Work()
{
	scanf("%d%d%d%d%d", &Length, &NormalV, &RunV, &RunTime, &N);
	double Ans = 0;
	for (int i = 0; i < N; i ++)
	{
		int A, B, C;
		scanf("%d%d%d", &A, &B, &C);
		F[i].Len = B - A;
		F[i].W = C;
		Length -= F[i].Len;
		Ans += F[i].Len / (double) (NormalV + F[i].W);
	}
	F[N].Len = Length;
	F[N].W = 0;
	Ans += F[N].Len / (double) (NormalV + F[N].W);

	sort(F, F + N + 1);
	double RunT = RunTime;
	for (int i = 0; i <= N; i ++)
	{
		double NT = F[i].Len / (double) (NormalV + F[i].W);
		double RT = F[i].Len / (double) (RunV + F[i].W);
		if (RT <= RunT)
		{
			RunT -= RT;
			Ans = Ans - NT + RT;
		}
		else
		{
			double Len = RunT + (F[i].Len - RunT * (RunV + F[i].W)) / (double) (NormalV + F[i].W);
			RunT = 0;
			Ans = Ans - NT + Len;
		}
	}
	return Ans;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int Cases;
	scanf("%d", &Cases);
	for (int i = 1; i <= Cases; i ++)
		printf("Case #%d: %.8lf\n", i, Work());
	return 0;
}