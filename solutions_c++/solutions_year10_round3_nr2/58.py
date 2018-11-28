#include <stdio.h>

int main()
{
	//freopen("B2.in", "r", stdin);
	//freopen("B2.out", "w", stdout);

	int nprob, l, p, c;
	scanf("%d", &nprob);
	for (int prob = 0; prob < nprob; prob ++)
	{
		scanf("%d%d%d", &l, &p, &c);
		int cnt = 0;
		while ((long long) l * c < p)
		{
			cnt ++;
			l *= c;
		}
		int ans = 0;
		while (cnt)
		{
			ans ++;
			cnt /= 2;
		}
		printf("Case #%d: %d\n", prob + 1, ans);
	}


	return 0;
}