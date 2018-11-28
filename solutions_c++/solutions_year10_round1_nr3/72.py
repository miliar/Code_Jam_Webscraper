#include<cstdio>

int A1,A2,B1,B2;
bool ok(int A, int B)
{
	if (A < B)
	{
		int tmp = A; A = B; B = tmp;
	}
	if (B == A) return false;
	if (A / B >= 2) return true;
	return !ok(A - B, B);

}

long long solve(int A, int B)
{
	if (A == 0 || B == 0) return 0;
	long long cnt;
	cnt = 1;
	long long prev, last;
	prev = last = 1;
	for (int i = 2; i <= A; ++i)
	{
		if (ok(i, prev))
		{
			prev += 1; last += 2;
		}
		else last += 1;
		if (prev > B) return cnt;
		if (last >= B) cnt += B - prev + 1; else cnt += last - prev + 1;
	}
	return cnt;
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("output.txt","w", stdout);
	int cases;
	scanf("%d", &cases);
	for (int ca = 1; ca <= cases; ++ca)
	{
		scanf("%d%d%d%d",&A1,&A2, &B1,&B2);
		long long ans = solve(A2,B2) - solve(A1-1,B2) - solve(A2, B1 - 1) + solve(A1 - 1, B1 - 1);
		ans = (long long)(A2 - A1 + 1) * (long long)(B2 - B1 + 1) - ans;
		printf("Case #%d: %lld\n", ca, ans);
	}
	fclose(stdin);
	fclose(stdout);
}
