#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

bool check(int *Y, int A)
{
	for(int i = 0; i < A; i++)
		for(int j = i + 1; j < Y[i]; j++)
			if(Y[j] > Y[i])
				return false;
	return true;
}

void test(int *X, int *Y, int A)
{
	for(int i = 0; i < A; i++)
	{
		int best = 0;
		double best_value = 0;
		for(int j = i + 1; j <= A; j++)
		{
			double value = (X[j] - X[i]) / (double)(j - i);
			if(value > best_value)
				best = j, best_value = value;
		}
		
		if(best != Y[i])
			printf("(%d: %d, %d) ", i, best, Y[i]);
	}
	//puts("");
}

int main()
{
	int N, MAX = 10000000;
	
	scanf("%d\n", &N);
	for(int t = 0; t < N; t++)
	{
		int A;
		scanf("%d\n", &A), A--;
		
		int *Y = new int[A], *X = new int[A + 1], *Z = new int[A + 1];
		for(int i = 0; i < A; i++)
			scanf("%d\n", &Y[i]), Y[i]--;
		
		if(check(Y, A))
		{
			X[A] = MAX, Z[A] = -1;
			for(int i = A - 1; i >= 0; i--)
				Z[i] = Z[Y[i]] + 1, X[i] = X[Y[i]] - 1 - Z[i] * (Y[i] - i);
			
			printf("Case #%d: ", t + 1);
			for(int i = 0; i <= A; i++)
				printf("%d ", X[i]);
			puts("");
			test(X, Y, A);
		}
		else
			printf("Case #%d: Impossible\n", t + 1);
		
		delete[] X, delete[] Y;
	}
	
	return 0;
}
