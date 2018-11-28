#include <iostream>
#include <cstdio>
#include <string>

#define MAX_C 500 

int map[20][MAX_C+1];
char target[20] = "welcome to code jam";

int main()
{
	int i, j, k;
	int n, N;
	int lent, leni;
	char input[MAX_C+1];

	lent = strlen(target);

	scanf("%d\n", &N);

	for(n=1;n<=N;n++)
	{
		memset(map, 0, sizeof(map));
		gets(input);
		leni = strlen(input);

		if( input[0] == target[0] )
			map[0][0] = 1;

		for(i=1;i<leni;i++)
		{
			if( input[i]==target[0] )
				map[0][i] = (map[0][i-1] + 1) % 10000;
			else
				map[0][i] = map[0][i-1];
		}
		for(i=1;i<lent;i++)
		{
			for(j=i;j<leni;j++)
			{
				if( target[i]==input[j] )
					map[i][j] = (map[i-1][j-1] + map[i][j-1]) % 10000;
				else
					map[i][j] = map[i][j-1];
			}
		}
		printf("Case #%d: %04d\n", n, map[lent-1][leni-1]);
	}

	return 0;
}
