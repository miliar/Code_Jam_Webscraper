#include <iostream>
#include <cstdio>
#include <cstring>

int main()
{
	char flag[26];
	int t;
	char g[101];
	flag[0] = 'y';
	flag[1] = 'h';
	flag[2] = 'e';
	flag[3] = 's';
	flag[4] = 'o';
	flag[5] = 'c';
	flag[6] = 'v';
	flag[7] = 'x';
	flag[8] = 'd';
	flag[9] = 'u';
	flag[10] = 'i';
	flag[11] = 'g';
	flag[12] = 'l';
	flag[13] = 'b';
	flag[14] = 'k';
	flag[15] = 'r';
	flag[16] = 'z';
	flag[17] = 't';
	flag[18] = 'n';
	flag[19] = 'w';
	flag[20] = 'j';
	flag[21] = 'p';
	flag[22] = 'f';
	flag[23] = 'm';
	flag[24] = 'a';
	flag[25] = 'q';
	freopen("A.in","r",stdin);	
	freopen("A.out","w",stdout);
	scanf("%d\n",&t);
	for (int i = 0; i < t; i++)
	{
		printf("Case #%d: ",i + 1);
		gets(g);
		for (int j = 0; j < strlen(g); j++)
			if (g[j] == ' ')
				printf(" ");
			else
				printf("%c",flag[g[j]-'a']);
		puts("");
		
	}
	return 0;
}
