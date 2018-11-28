#include <stdio.h>
#include <string.h>
#define g 1000

int ar,ca,ne;
int ma[g],ic;
int bi[g], pi[g];

int main ()
{
	freopen ("clarge.in", "r", stdin);
	freopen ("clarge.out", "w", stdout);

	scanf ("%d", &ic);
	for (int i = 0; i < ic; i ++)
	{
		scanf ("%d%d%d", &ar, &ca, &ne);
		for (int i = 0; i < ne; i ++)
			scanf ("%d", ma + i);
		for (int i = 0; i < ne; i ++)
		{
			bi[i] = 0;
			pi[i] = i;
			while (bi[i] + ma[pi[i]] <= ca)
			{
				bi[i] += ma[pi[i]];
				pi[i] = (pi[i] + 1) % ne;
				if (pi[i] == i)
					break;
			}
		}
		long long ans = 0;

		int pos = 0;
		for (int i = 0; i < ar; i ++)
		{
//			printf ("%d\n", bi[pos]);
			ans += bi[pos];
			pos = pi[pos];
		}

		printf ("Case #%d: %I64d\n", i + 1, ans);
	}

	return 0;
}