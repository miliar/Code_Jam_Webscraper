#include<cstdio>
using namespace std;

#define INPUT "C-small.in"
#define OUTPUT "C-small.out"
#define NMAX 102

void solve()
{
	int A[NMAX], n, l, h;

	scanf("%d%d%d", &n, &l, &h);
	for(int i = 0; i < n; ++i)
		scanf("%d", A + i);

	for(int f = l; f <= h; ++f)
	{
		int i;
		for(i = 0; i < n; ++i)
			if(f % A[i] != 0 && A[i] % f != 0)
				break;
		if(i == n)
		{
			printf("%d\n", f);
			return;
		}
	}

	printf("NO\n");
}

int main()
{
	int nt;

	freopen(INPUT, "r", stdin);
	freopen(OUTPUT, "w", stdout);

	scanf("%d", &nt);
	for(int t = 1; t <= nt; ++t)
	{
		printf("Case #%d: ", t);
		solve();
	}

	return 0;
}
