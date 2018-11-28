#include <cstdio>
#include <iostream>

using namespace std;

int main()
{
	int N;
	
	scanf("%d\n", &N);
	for(int t = 0; t < N; t++)
	{
		int A, B;
		scanf("%d %d\n", &A, &B);
		
		double *P = new double[A], *X = new double[A + 1], E0 = B + 2;
		for(int i = 0; i < A; i++)
			scanf("%lf ", &P[i]);
		
		X[0] = 1;
		for(int i = 0; i < A; i++)
			X[i + 1] = X[i] * P[i];
		for(int i = 0; i <= A; i++)
		{
			double E = X[A - i] * (i + B - A + i + 1) + (1 - X[A - i]) * (i + B - A + i + 1 + B + 1);
			if(E < E0)
				E0 = E;
		}
		
		printf("Case #%d: %.6lf\n", t + 1, E0);
		delete[] P;
		delete[] X;
	}
	
	return 0;
}
