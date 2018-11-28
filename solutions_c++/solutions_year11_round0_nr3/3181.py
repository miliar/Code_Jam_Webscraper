#include<stdio.h>

long long int sol;

int maxtwo(int x, int y)
{
	if(x>y)
		return x;
	return y;
}

int max(int x, int y, int z)
{
	return maxtwo(maxtwo(x,y), z);
}

void back(int A[], int n, long long int left, long long int right, int nl, int nr, int sl, int sr)
{
	if(n == 0)
	{
		if((nl != 0) && (nr != 0))
		{
			if(sl == sr)
			sol = max(sol, left, right);
		}
	}
	else
	{
		back(A, n-1, left+A[n], right, nl+1, nr, sl^A[n], sr);
		back(A, n-1, left, right+A[n], nl, nr+1, sl, sr^A[n]);
	}
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d", &T);
	for(int cases = 1; cases <= T; cases++)
	{
		sol = 0;
		int A[1001];
		int N;
		scanf("%d", &N);
		for(int i = 1; i <= N; i++)
		{
			scanf("%d", &A[i]);
		}
		back(A, N, 0, 0, 0, 0, 0, 0);
		if(sol)
			printf("Case #%d: %lld\n", cases, sol);
		else
			printf("Case #%d: NO\n", cases);
	}
	return 0;
}