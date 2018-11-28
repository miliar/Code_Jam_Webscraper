#include <cstdio>
#include <cstring>

int mic[2][25];
char *theword = "Awelcome to code jam";

int main()
{
	int testIndex, testCount;
	scanf("%d\n", &testCount);
	for(testIndex = 1; testIndex <= testCount; testIndex++)
	{
		char str[510];
		gets(str);
		int len = strlen(str);
		int thewordlen = strlen(theword);
		for(int i = 0; i < 25; i++)mic[1][i] = mic[0][i] = 0;
		mic[0][0] = 1;
		for(int i = 0; i < len; i++)
		{
			//printf("\n%c ", str[i]);
			for(int j = 0; j <= thewordlen; j++)
			{
				mic[(i+1)%2][j] = mic[i%2][j];
				if(str[i] == theword[j])
					mic[(i+1)%2][j] += mic[i%2][j-1];
				mic[(i+1)%2][j] %= 10000;
				//printf("%d ", mic[(i+1)%2][j]);
			}
		}
		printf("Case #%d: %04d\n", testIndex, mic[len%2][thewordlen-1]);
	}
	return 0;
}
