#include "stdio.h"

char s[3][128] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi",
	"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
	"de kr kd eoya kw aej tysr re ujdr lkgc jv"};
char t[3][128] = {"our language is impossible to understand",
	"there are twenty six factorial possibilities",
	"so it is okay if you want to just give up"};
char m[128];
char str[16384];

int main()
{
	int nu = 0;
	char u[128] = {0};
	for(int i = 0; i < 3; i ++)
		for(int j = 0; s[i][j]; j ++)
		{
			m[s[i][j]] = t[i][j];
			if(!u[t[i][j]])
			{
				u[t[i][j]] = 1;
				nu ++;
			}
		}
/*	printf("%d\n", nu);
	for(char c = 'a'; c <= 'z'; c ++)
		if(!m[c])
		{
			printf("%c!!\n", c);
		}
*/	m['z'] = 'q';
	m['q'] = 'z';
	int N, c ;
	scanf("%d", &N);
	gets(str);
	for(int T = 1; T <= N; T ++)
	{
		gets(str);
		for(char *p = str; *p; p ++)
			*p = m[*p];
		printf("Case #%d: ", T);
		puts(str);
	}
	return 0;
}
