
	#include <cstdlib>
	#include <cstdio>

	using namespace std;

	int N, n, k;

	int work()
	{
		scanf("%d%d", &n, &k);
		int m = (1 << n);
		n = m;
		if ((k % n) == n - 1)
			printf("ON\n");
		else
			printf("OFF\n");
	}

	int main()
	{
		freopen("A-large.in", "r", stdin);
		freopen("A.out", "w", stdout);
		scanf("%d", &N);
		for (int i = 1; i <= N; i ++)
		{
			printf("Case #%d: ", i);
			work();
		}
		return 0;
	}
