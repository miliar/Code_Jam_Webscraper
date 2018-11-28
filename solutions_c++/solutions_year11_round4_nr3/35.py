#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
using namespace std;

int			yes	[1000000 + 100];

long long		n;

void init()
{
	cin >> n;
}

void solve()
{
	memset(yes, 1, sizeof(yes));
	int top = int( sqrt(n) + 1 );
	long long ans = 1;

	for (long long i = 2; i <= top; i ++)
	{
		if (yes[i])
		{
			long long k = (long long)i * i;
			while (k <= top)
			{
				yes[k] = 0;
				k += i;
			}

			k = n;
			long long cc = 0;
			while (k >= i)
				k /= i, cc ++;
			if (cc >= 1) ans += cc - 1;
		}
	}

	if (n == 1) ans = 0;
	printf("%d\n",(int)ans);
}

int main()
{
//	freopen("C-small-attempt1.in", "r", stdin);
//	freopen("C-small2.out", "w", stdout);

	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

//	freopen("in.txt", "r", stdin);

	long long T;
	cin >> T;

	for (long long t = 1; t <= T; t ++)
	{
		init();
		printf("Case #%d: ", (int)t);
		solve();
	}

	return 0;
}
