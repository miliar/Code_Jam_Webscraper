#include<cstdio>
#include<algorithm>
using namespace std;

#define INPUT "B-large.in"
#define OUTPUT "B-large.out"
#define CMAX 1001
#define NMAX 1000001
#define ll long long
int A[NMAX];

void solve()
{
	int D[CMAX], n, l, c, i, k = 0;
	ll t, sum = 0;

	scanf("%d%lld%d%d", &l, &t, &n, &c);
	for(i = 0; i < c; ++i)
		scanf("%d", D + i);

	for(i = 0; i < n; ++i)
		sum += D[i % c];
	sum *= 2;

	ll s = 0;
	for(i = 0; i < n; ++i)
	{
		s += D[i % c];
		if(s > t / 2)
			break;
	}

	if(i == n)
	{
		printf("%lld\n", sum);
		return;
	}

	A[k++] = s - t / 2;
	for(++i; i < n; ++i)
		A[k++] = D[i % c];
	sort(A, A + k);
	for(i = k - 1; i >= k - l && i >= 0; --i)
		sum -= A[i];

	printf("%lld\n", sum);
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
