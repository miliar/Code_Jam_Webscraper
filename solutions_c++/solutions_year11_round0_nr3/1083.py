#include<cstdio>
#include<algorithm>

int main()
{
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		int N;
		scanf("%d", &N);
		int sum = 0;
		int xsum = 0;
		int m = int(1e7);
		for (int i = 0; i < N; i++)
		{
			int c;
			scanf("%d", &c);
			sum += c;
			xsum ^= c;
			m = std::min(m, c);
		}
		if (xsum)
			printf("Case #%d: NO\n", t);
		else
			printf("Case #%d: %d\n", t, sum - m);
	}
	return 0;
}
