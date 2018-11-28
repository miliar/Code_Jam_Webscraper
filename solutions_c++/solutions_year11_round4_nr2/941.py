#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;

#define eps (1e-5)

char in[510][510];

long long n, m;
long long a[510][510];

void read()
{
	long long D;
	scanf("%lld%lld%lld", &n, &m, &D);
	for (long long i = 0; i < n; ++i)
		scanf("%s", in[i]);
	memset(a, 0, sizeof(a));
	for (long long i = 0; i < n; ++i)
		for (long long j = 0; j < m; ++j)
			a[i + 1][j + 1] = D + in[i][j] - '0';
}

int main()
{
	freopen("C:\\Users\\hayk\\Documents\\GCJ\\B-small-attempt2.in", "r", stdin);
//	freopen("C:\\Users\\hayk\\Documents\\GCJ\\sample.in", "r", stdin);
	freopen("C:\\Users\\hayk\\Documents\\GCJ\\B-small-attempt2.out", "w", stdout);
//	freopen("C:\\Users\\hayk\\Documents\\GCJ\\C-large.in", "r", stdin);
//	freopne("C:\\Users\\hayk\\Documents\\GCJ\\C-large.out", "w", stdout);

	long long T, nt, i, j, k, p, q;
	scanf("%lld", &T);
	for (nt = 1; nt <= T; ++nt)
	{
		read();
		for (k = min(n, m); k >= 3; --k)
		{
			for (i = 1; i + k - 1 <= n; ++i)
				for (j = 1; j + k - 1 <= m; ++j)
				{
					double cx = 0, cy = 0, mass = 0;
					for (p = i; p <= i + k - 1; ++p)
						for (q = j; q <= j + k - 1; ++q)
							if (!(p == i && q == j ||
								p == i && q == j + k - 1 ||
								p == i + k - 1 && q == j ||
								p == i + k - 1 && q == j + k - 1))
						{
							cx += p * a[p][q];
							cy += q * a[p][q];
							mass += a[p][q];
						}
					cx /= mass;
					cy /= mass;

					if (fabs(cx - i - (k - 1)/2.0) < eps &&
						fabs(cy - j - (k - 1)/2.0) < eps)
					{
						goto there;
					}
				}
		}
there:
		printf("Case #%lld: ", nt);
		if (k >= 3)
			printf("%lld\n", k);
		else
			printf("IMPOSSIBLE\n");
	}
	return 0;
}
