#include <iostream>
using namespace std;

const int MAXN = 1000 + 10;

int g[MAXN], p[MAXN], s[MAXN];
int R, k, N;

int main(int argc, char *argv[])
{
	freopen ("C-large.in", "r", stdin);
	freopen ("ou.txt", "w", stdout);

	int T;
	scanf ("%d", &T);
	for (int test = 1; test <= T; ++test)
	{
		printf ("Case #%d: ", test);
		scanf ("%d%d%d", &R, &k, &N);

		long long sum = 0;
		for (int i = 0; i < N; ++i)
		{
			scanf ("%d", g + i);
			sum += (long long)g[i];
		}

		if (sum <= k)
		{
			printf ("%I64d\n", sum * R);
			continue;
		}

		for (int i = 0; i < N; ++i)
		{
			sum = 0;
			for (int j = i; ; j = (j + 1) % N)
			{
				sum += g[j];
				if (sum > k)
				{
					p[i] = j;
					s[i] = sum - g[j];
					break;
				}
			}
			//printf ("%d ", p[i]);
		}
		//printf ("\n");

		long long answer = 0;

		for (int i = 1, cur = 0; i <= R; i++, cur = p[cur])
		{
			answer += s[cur];
		}

		printf ("%I64d\n", answer);
	}
	
	return 0;
}
