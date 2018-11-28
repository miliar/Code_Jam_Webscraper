#include <cstdio>

const int N = 1001;
int r, k, n;
__int64 g[2*N];
__int64 s[2*N];
int next[N];

__int64 sum(int l, int r)
{
	if (r <= l)
		r += n;
	return s[r] - s[l];
}

void ScanAndInit(int testId)
{
	scanf("%d%d%d", &r, &k, &n);
	for (int i3 = 0; i3 < n; i3++)
		scanf("%I64d", &g[i3]);

	for (int i1 = n; i1 < 2*n; i1++)
		g[i1] = g[i1-n];
	for (int i2 = 1; i2 < 2*n; i2++)
		s[i2] = s[i2-1] + g[i2-1];
	for (int i = 0; i < n; i++)
	{
		for (int j = i+1; j <= i+n; j++)
			if (s[j]-s[i] <= k)
				next[i] = (j) % n;
	}
/*	printf("DEBUG INFO (test#%d)\n", testId);
	printf("g-array:\n");
	for (int i5 = 0; i5 < n; i5++)
		printf("%I64d ", g[i5]);
	printf("\ns-array:\n");
	for (int i4 = 0; i4 < 2*n; i4++)
		printf("%I64d ", s[i4]);
	printf("\nnext-array:\n");
	for (int i6 = 0; i6 < 2*n; i6++)
		printf("%d ", next[i6]);
	printf("\n");*/
}

void Solve(int testId)
{	
	ScanAndInit(testId);
//	printf("Case #%d solve.\n", testId);
	__int64 res = 0;
	int cur = 0;
	for (int i = 0; i < r; i++)
	{		
		int n = next[cur];
		__int64 ss = sum(cur, n);
//		printf("\tcur:%d next:%d s:%I64d\n",cur, n, ss);
		res += ss;		
		cur = n;
	}
	printf("Case #%d: %I64d\n", testId, res);
}

void Solve()
{
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
		Solve(i);
}

void OpenFiles()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
}

int main()
{
	OpenFiles();
	Solve();
	return 0;
}
/*
3
4 6 4
1 4 2 1
100 10 1
1
5 5 10
2 4 2 3 4 2 1 2 1 3

Case #1: 21
Case #2: 100
Case #3: 20
 */