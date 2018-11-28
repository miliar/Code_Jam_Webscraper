#include <stdio.h>
#include <set>
using namespace std;

const int pow[10] = {1, 10, 100, 1000, 10000, 100000, 10000000};

int solve (int A, int B)
{
	set<int> visited;

	int result = 0;

	for (int i = A; i <= B; i++)
	{
		if (visited.find (i) != visited.end ())
		{
			continue;
		}

		int d[10], t = 0, tmp = i;
		while (tmp)
		{
			d[t ++] = tmp % 10;
			tmp /= 10;
		}

		tmp = i;

		int tot = 0;
		for (int j = 0; j < t; j++)
		{
			if (A <= tmp && tmp <= B && visited.find (tmp) == visited.end ())
			{
				tot ++;
				visited.insert (tmp);
				//printf ("%d ", tmp);
			}

			tmp = tmp / 10 + d[j] * pow[t - 1];
		}

		result += (tot * (tot - 1)) / 2;
	}

	return result;
}

int main(int argc, char *argv[])
{
	freopen ("C-small-attempt0.in", "r", stdin);
	freopen ("C-small.out", "w", stdout);

	int T, A, B;
	scanf ("%d", &T);
	for (int i = 1; i <= T; ++i)
	{
		scanf ("%d%d", &A, &B);
		printf ("Case #%d: %d\n", i, solve (A, B));
	}

	return 0;
}
