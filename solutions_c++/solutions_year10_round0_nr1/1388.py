#include <cstdio>

int main()
{
	freopen("p1.in", "r", stdin);
	freopen("p1.out", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int caseNum = 1; caseNum <= T; caseNum++)
	{
		long N, k;
		scanf("%ld%ld", &N, &k);
		k++;
		bool res = true;
		while (N > 0)
		{
			N--;
			if (k % 2 == 1)
			{
				res = false;
				break;
			}
			k /= 2;
		}
		printf("Case #%d: ", caseNum);
		if (res)
			printf("ON\n");
		else
			printf("OFF\n");
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
