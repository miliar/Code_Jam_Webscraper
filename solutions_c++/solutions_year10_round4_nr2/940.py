#include <cstdio>
#include <cstring>

int T;
int P;
int m[1 << 11];
int p[10][1 << 10];
int main()
{
	scanf("%d", &T);
	for(int t = 1; t <= T; t ++)
	{
		scanf("%d", &P);
		memset(m, 0, sizeof(m));
		for(int i = 0; i < (1 << P); i ++)
			scanf("%d", &m[i]);
		for(int i = 0; i < P; i ++)
			for(int j = 0; j < 1 << P - i - 1; j ++)
				scanf("%d", &p[i][j]);
		int res = 0;
		for(int i = 0; i < (1 << P); i ++)
		{
			int start = 1 << P;
			int add = 1 << P - 1;
			int level = 1;
			for(int j = start + (i >> level); add; start += add, add /= 2, level ++, j = start + (i >> level))
			{
//				fprintf(stderr, "%d\n", j);
				if( level > m[i] )
				{
					if(!m[j])	res ++;
					m[j] = 1;
				}
			}
		}
		printf("Case #%d: %d\n", t, res);
	}
}
