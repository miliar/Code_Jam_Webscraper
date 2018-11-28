#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char s[30];
int hash[10];
int main()
{
	int i , j , t , cas = 1;
	freopen("F:\\B-large.in" , "r" , stdin);
	freopen("F:\\B-large.out" , "w" , stdout);
	scanf("%d" , &t);
	while (t --)
	{
		memset(hash , 0 , sizeof(hash));
		scanf("%s" , s);
		int l = strlen(s);
		for (i = l - 2;i >= 0;i --)
		{
			if (s[i] < s[i + 1]) break;
		}
		printf("Case #%d: " , cas ++);
		if (i < 0)
		{
			for (i = 0;i < l;i ++)
				hash[s[i] - '0'] ++;
			for (i = 1;i < 10;i ++)
				if (hash[i] != 0)
				{
					printf("%d0" , i);
					hash[i] --;
					break;
				}
			for (i = 0;i < 10;i ++)
			{
				while (hash[i] --)
					printf("%d" , i);
			}
			printf("\n");
			continue;
		}
		else
		{
			for (j = 0;j < i; j ++)
				printf("%c" , s[j]);
			int tmp = i;
			for (;s[i];i ++)
			{
				hash[s[i] - '0'] ++;
			}
			for (i = s[tmp] - '0' + 1;i < 10;i ++)
			{
				if (hash[i] != 0)
				{
					printf("%d" , i);
					hash[i] --;
					break;
				}
			}
			for (i = 0;i < 10;i ++)
			{
				while (hash[i] --)
					printf("%d" , i);
			}
			printf("\n");
		}
	}
	return 0;
}