#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>

using namespace std;

const double Tau1 = (sqrt(5.0) + 1.0) * 0.5;
const double Tau2 = (sqrt(5.0) - 1.0) * 0.5;

int A1, A2, B1, B2;

long long Work()
{
	scanf("%d%d%d%d", &A1, &A2, &B1, &B2);
	long long Ans = 0;
	for (int i = A1; i <= A2; i ++)
	{
		int Min = B1;
		int Max = min(B2, (int) floor(i * Tau2 + 1e-8));
		if (Min <= Max)
			Ans += (long long) (Max - Min + 1);
		Min = max((int) ceil(i * Tau1 - 1e-8), B1);
		Max = B2;
		if (Min <= Max)
			Ans += (long long) (Max - Min + 1);
	}
	return Ans;
}

int main()
{
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	int Cases;
	scanf("%d", &Cases);
	for (int Case = 1; Case <= Cases; Case ++)
		printf("Case #%d: %I64d\n", Case, Work());
	return 0;
}
