#include<stdio.h>

int csN, csK;
int N, C;
long long CchooseN;
double E[64];

long long choose(int n, int k)
{
	long long s;
	int i;
	for(s = 1, i = 0; i < k; ++i)
		s = (s*(n-i)) / (i+1);
	return s;
}

int main()
{
	int i, j;
	double ex, prob;
	scanf("%d", &csN);
	for(csK = 1; csK <= csN; ++csK)
	{
		scanf("%d %d", &C, &N);
		CchooseN = choose(C, N);
		E[C] = 0;
		for(i = C-1; i >= 0; --i)
		{
			E[i] = 1;
			for(j = 1; j <= N && i+j <= C; ++j)
				E[i] += (E[i+j] * choose(C-i, j) * choose(i, N-j)) / CchooseN;
			if(i >= N) E[i] = (E[i]*CchooseN) / (CchooseN-choose(i, N));
		}
		printf("Case #%d: %.7lf\n", csK, E[0]);
	}
}
