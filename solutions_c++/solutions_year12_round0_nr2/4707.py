#include <cstdio>
using namespace std;

int surp(int x)
{
	if (x == 0) return 0;
	if (x > 25) return 10;
	return (x + 4)/3;
}

int notsurp(int x)
{
	return (x + 2)/3;
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int nn;
	scanf ("%d\n", &nn);
	for (int ii = 1; ii <= nn; ++ii)
	{
		int n, s, p, a, k = 0;
		scanf ("%d%d%d", &n, &s, &p);
		for (int i = 0; i < n; ++i)
		{
			scanf ("%d", &a);
			if (notsurp(a) >= p) ++k;
			else
				if (s > 0 && surp(a) >= p)
				{
					++k;
					--s;
				}
		}
		printf ("Case #%d: %d\n", ii, k);
	}
}
