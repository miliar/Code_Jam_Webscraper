# include <iostream>
using namespace std;

int z[11];
int need[100];

__int64 gcd(__int64 x, __int64 y)
{
	if (y == 0) return 0;
	if (x % y == 0) return y;
	else return gcd(y, x % y);
}

__int64 lcm(__int64 x, __int64 y)
{
	return x * y / gcd(x, y);
}

int main()
{
	int C, N, i, j, game, all;
	__int64 k, m;

//	freopen("b-small.in", "rt", stdin);
//	freopen("b-small.out", "wt", stdout);
	
	cin >> C;
	for (game = 1; game <= C; game++)
	{
		cin >> N;
		for (i = 0; i < N; i++)		
			cin >> z[i];

		all = 0;
		for (i = 0; i < N - 1; i++)
		{
			for (j = i + 1; j < N; j++)
				need[all++] = abs(z[i] - z[j]);
		}
		k = need[0];
		for (i = 1; i < all; i++)
			if (need[i]) k = gcd(k, need[i]);
		m = 0;
		for (i = 0; i < N; i++)
		{
			if (z[i] % k)
			{
				if (m == 0) m = 1;
				m = lcm(m, k - (z[i] % k));
			}
		}

		cout << "Case #" << game << ": ";
		printf("%I64d\n", m);
	}
	
	return 0;
}