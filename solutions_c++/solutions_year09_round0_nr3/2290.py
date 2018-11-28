#include <stdio.h>
#include <stdlib.h>

char b[1024] = " welcome to code jam";
int map[550][50];

int solve(char *a)
{
	int i,j;
	for (i=0; i<550; i++)
		map[i][0] = 1;
	for (j=1; j<50 ; j++)
		map[0][j] = 0;
	for (i=1; a[i]!=0; i++)
		for (j=1; b[j]!=0; j++)
			if (a[i]==b[j])
				map[i][j] = (map[i-1][j-1]+map[i-1][j])%10000;
		else
			map[i][j] = map[i-1][j];
#if DEBUG
	printf("%d, %d\n", i,j);
#endif
	return map[i-1][j-1];
}

int main() {
	int c,v;
	char s[1024];
	gets(s);
	sscanf(s, "%d", &c); 
	for (int i=0; i<c; i++)
	{
		gets(s+1);
		v=solve(s);
		printf("Case #%d: %04d\n", i+1, v);
	}
	return 0;
}