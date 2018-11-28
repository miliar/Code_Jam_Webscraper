#include <vector>
#include <list>
#include <algorithm>
#include <cmath>
#include <functional>
#include <cstdlib>
#include <iostream>

using namespace std;

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int cases;
	scanf("%d", &cases);

	int R, k, N;
	int p, g, f;
	int sum;
	int groups[1000];

	for (int i = 1; i <= cases; i++)
	{
		scanf ("%d %d %d", &R, &k, &N);

		for (int j = 0; j < N; j++)
		{
			scanf("%d", &groups[j]);
		}

		sum = 0;
		p = 0;

		for (int x = 0; x < R; x++)
		{
			g = 0;
			f = -1;
			while (groups[p] + g <= k && p != f)
			{
				if (f == -1) f = p;

				g += groups[p];

				p++;
				if (p >= N) p = 0;
			}

			sum += g;
		}

		cout << "Case #" << i << ": " << sum << endl;
	}

	return 0;
}