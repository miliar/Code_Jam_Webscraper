#include <cstdio>
#include <iostream>

using namespace std;

int main()
{
	int T, i, j, n, d[1024], t = 1, cnt, K, now;
	//freopen("C-small-attempt0.in","r",stdin);
	//freopen("C.out","w", stdout);
	scanf("%d", &T);
	int k[5008];
	bool flag[5008];
	while (T --)
	{
		scanf("%d", &K);
		scanf("%d", &n);
		for (i = 0; i < n; i ++)
			scanf("%d", &d[i]);
		memset(flag, 0, sizeof(flag));
		now = 0;
		for (i = 1; i <= K; i ++)
		{
			cnt = 0;
			while (1)
			{
				
				if (flag[now] == 0)
					cnt ++;
				
				if (cnt == i)
				{
					k[now] = i;
					flag[now] = 1;
					now = now + 1;
					if (now >= K)
						now -= K;
					break;
				}
				now = now + 1;
				if (now >= K)
					now -= K;
				
			}
		}
		printf("Case #%d:", t ++);
		for (i = 0; i < n; i ++)
			printf(" %d", k[d[i]-1]);
		printf("\n");
	}
	return 0;
}