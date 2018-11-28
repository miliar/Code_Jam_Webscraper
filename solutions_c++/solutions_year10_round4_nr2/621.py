#include <stdio.h>
#include <string.h>

int a[1300] , b[1300] , num[1300];
int m[530][530];

int main()
{
	int f[11] = {1 , 2 , 4 , 8 , 16 , 32 , 64 , 128 , 256 , 512 , 1024};
	int cas;
	int res , p;

	freopen("B-small-attempt1.in" , "r" , stdin);
	freopen("B-small-attempt1.out" , "w" , stdout);

	scanf("%d" , &cas);
	for (int t = 1; t <= cas; t ++)
	{
		scanf("%d", &p);
		for (int i = 0; i < f[p]; i ++)
			scanf("%d" , &a[i]);
		for (int i = 0; i < p; i ++)
			for (int j = 0; j < f[p-i-1]; j ++)
				scanf("%d" , &m[i][j]);

		for (int i = 0; i < f[p]; i ++) num[i] = p;
		memset(b , 0 , sizeof(b));
		res = 0;
		while (1)
		{
			int min = 30;
			int x = -1;
			for (int i = 0; i < f[p]; i ++)
				if (b[i] == 0 && a[i] < min)
				{
					x = i;
					min = a[i];
				}
			if (x == -1) break;
			int need = num[x] - a[x];
			
			if (need > 0)
			{
				int j = 0;
				for (int i = p-1; i >= 0; i --)
				{
					if (m[i][j] > 0)
					{
						m[i][j] = -1;
						need --;
						res ++;
						int k = i;
						int first = j, end = j;
						while (k>=0)
						{
							first = first * 2;
							end = end * 2 + 1;
							k --;
						}
						for (int z = first; z <= end; z ++)
							num[z] --;
					}
					j = x >> i;
					if (need == 0) break;
				}
			}
			for (int i = 0; i < f[p]; i ++)
				if (b[i] == 0 && num[i] <= a[i]) b[i] = 1;
		}
		printf("Case #%d: %d\n" , t , res);
	}

	return 0;
}