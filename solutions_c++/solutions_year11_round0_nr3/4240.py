#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;

const int MAXN = 1005, INFTY = 0x3F3F3F3F;

int T, N, num [MAXN];

int main ()
{
	scanf ("%d", &T);

	for (int i = 0, x, total, small; i < T; i++)
	{
		scanf ("%d", &N);
		x = total = 0; small = INFTY;

		for (int j = 0; j < N; j++)
		{
			scanf ("%d", num + j);

			x ^= num [j]; 
			total += num [j];
			small = min (small, num [j]);
		}

		printf ("Case #%d: ", i + 1);

		if (x != 0)
			printf ("NO\n");
		else
			printf ("%d\n", total - small);
	}

	return 0;
}
