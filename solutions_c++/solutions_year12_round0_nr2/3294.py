#include <cstdio>
#include <algorithm>

using namespace std;
int Sum[128], Count[32];
int T, I, J, K, t, i, j, z, V;

void read()
{
	scanf("%d%d%d", &I, &J, &K);
	for (i = 1; i <= I; ++i)
	{
		scanf("%d", &Sum[i]);
	}
}

inline bool canSurprise(int & sum)
{
	return 2 <= sum && sum <= 28;
}

inline bool canContribute(int & sum, int & threshold, bool surprise)
{
	return surprise? sum >= threshold * 3 - 4: sum >= threshold * 3 - 2;
}

void solve()
{
	for (z = V = 0; z <= 30; ++z)
	{
		Count[z] = 0;
	}

	for (i = 1; i <= I; ++i)
	{
		++Count[Sum[i]];
	}

	for (z = 30, j = 0; z >= K; --z)
	{
		while (Count[z] > 0)
		{
			if (canContribute(z, K, false))
			{
				++V;
				--Count[z];
			}
			else
			{
				break;
			}
		}

		while (Count[z] > 0 && j < J)
		{
			if (canContribute(z, K, true))
			{
				++V;
				--Count[z];
				++j;
			}
			else
			{
				break;
			}
		}
	}
}

void write()
{
	printf("Case #%d: %d\n", t, V);
}

int main()
{
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	scanf("%d", &T);
	for (t = 1; t <= T; ++t)
	{
		read();
		solve();
		write();
	}
	return 0;
}