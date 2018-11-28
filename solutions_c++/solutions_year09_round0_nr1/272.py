

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char s[5001][16];
char str[1001];
int main()
{
	int n , l , d , cas,  i , j , len  , k , m , o;
	//freopen("E:\\A-small-attempt0.in" , "r"  ,stdin);
	//freopen("E:\\A-small-attempt0.out" , "w"  , stdout);
	scanf("%d %d %d" , &l , &d , &n);
	for(i = 0;i < d;i ++)
	{	
		scanf("%s" , s[i]);
	}
	for (k = 1;k <= n;k ++)
	{
		scanf("%s" , str);
		bool hash[16][26] = {0};
		j = 0;
		for (i = 0;i < l;i ++)
		{
			if (str[j] == '(')
			{
				j ++;
				while (str[j] != ')')
				{
					hash[i][str[j] - 'a'] = true;
					j ++;
				}
			}
			else
			{
				hash[i][str[j] - 'a'] = true;
				
			}
			j ++;
		}
		int ans = 0;
		for (i = 0;i < d;i ++)
		{
			for (j = 0;j < l;j ++)
			{
				if (hash[j][s[i][j] - 'a'] == 0)
					break;
			}
			if (j == l) ans ++;
		}
		printf("Case #%d: %d\n" , k , ans);

	}
	return 0;

}