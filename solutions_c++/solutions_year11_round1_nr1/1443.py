#include <cstdio>

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	int t;
	for (t = 1; t <= T; t++)
	{
		printf("Case #%d: ", t);
		int N, PD, PG;
		scanf("%d%d%d", &N, &PD, &PG);
		bool possible = 0;
		if ((PD < 100 && PG == 100) || (PD > 0 && PG == 0) ) possible = 0;
		else
		{
			int m = 100;
			int tmp;
			if (PD % 2 == 0)
			{
				m >>= 1;
				tmp = PD / 2;
				if (tmp % 2 == 0)
					m >>= 1;;
			}
			if (PD % 5 == 0)
			{
				m /= 5;
				tmp = PD / 5;
				if (tmp % 5 == 0)
					m /= 5;
			}
			if (m > N) possible = 0;
			else possible = 1;
		}
		if (possible) printf("Possible\n");
		else printf("Broken\n");
	}
	return 0;
}

