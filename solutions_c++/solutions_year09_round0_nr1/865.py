#include <stdio.h>
#include <string.h>

int flag[20][200];
char tab[10000];
struct Q
{
	char str[20];
	int flag;
}q[5500];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("1.out","w", stdout);
	int i,j,k;
	int L,D,N;
	scanf("%d%d%d", &L, &D, &N);
	for( i = 0; i < D; i ++ )
	{
		scanf("%s", q[i].str);
		q[i].flag = 0;
	}
	for( i = 0; i < N; i ++ )
	{
		for( j = 0; j < D; j ++ )
		{
			q[j].flag = 0;
		}
		scanf("%s", tab);
		memset( flag, 0, sizeof(flag));
		int count = 0;
		int f = 0;
		for( j = 0;  tab[j]; j ++ )
		{
			if( tab[j] == ')' )
			{
				f = 0;
				count ++;
			}
			else if( tab[j] == '(' )
			{
				f = 1;
			}
			else
			{
				flag[count][tab[j]] = 1;
				if( f == 0 )
				{
					count ++;
				}
			}
		}
		for( j = 0; j < L; j ++ )
		{
			for( k = 0; k < D; k ++ )
			{
				if( q[k].flag == 1 )
				{
					continue;
				}
				if( flag[j][ q[k].str[j] ] == 0 )
				{
					q[k].flag = 1;
				}
			}
		}
		int ans = 0;
		for( j = 0; j < D; j ++ )
		{
			if( q[j].flag == 0 )
				ans ++;
		}
		printf("Case #%d: %d\n", i+1, ans);
	}
	return 0;
}