#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char exist[27];
int len[27];
int pos[27][20];
char word[27];
int table[550][20];

int main()
{
	int i, aa, nn, l, j, t, k, ans;
	char buffer[1000];
	memset(exist,0,sizeof(exist));
	memset(len,0,sizeof(len));
	strcpy(word,"welcome to code jam");
	
	exist['w'-'a'] = 1;
	
	for ( i = 1; i < 19; i++ )
	{
		t = word[i]-'a';
		if ( word[i] == ' ' ) t = 26;
		exist[t] = 1;
		pos[t][len[t]++] = i;
	}
	
	gets(buffer);
	nn = atoi(buffer);
	for ( aa = 1; aa <= nn; ++aa )
	{
		memset(table,0,sizeof(table));
		gets(buffer);
		l = strlen(buffer);
		for ( i = 0; i < l; i++ )
		{
			t = buffer[i] -'a';
			if ( buffer[i] == ' ' ) t = 26;
			if ( !exist[t] ) continue;
			if (buffer[i] == 'w')
			{
				table[i][0] = 1;
			}
			for ( j = 0; j < i; j++ )
			{
				for ( k = 0; k < len[t]; k++ )
				{
					table[i][pos[t][k]] += table[j][pos[t][k]-1];
					table[i][pos[t][k]] %= 10000;
				}
			}
		}
		
		ans = 0;
		for ( i = 0; i < l; i++ )
		{
			ans = (ans + table[i][18]) % 10000;
		}
		
		printf("Case #%d: %04d\n",aa,ans);
	}
	
	return 0;
}

