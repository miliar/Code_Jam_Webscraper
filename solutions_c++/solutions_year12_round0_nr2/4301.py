// Google Code Jam 2012
// Qualification Round
// Program B. Dancing With the Googlers
#include <cstdio>
#include <cstring>

int main()
{
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; i++)
	{
		int N, S, P;
		int normal = 0;
		int surprise = 0;
		scanf("%d %d %d", &N, &S, &P);
		for (int j = 0; j < N; j++)
		{
			int t;
			scanf("%d", &t);
			if (t >= 3*P-2)
				normal++;
			else if (t >= 3*P-4 && P > 1)
				surprise++;
		}
		int ans = normal;
		if (surprise >= S) ans += S;
		else ans += surprise;
		printf("Case #%d: %d\n", i, ans);
	}
	return 0;
}
