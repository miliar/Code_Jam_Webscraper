#include <stdio.h>
#include <memory.h>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;
int T;
char s[1000];
char * phrase = "welcome to code jam";
int mas[2][20];
int MOD = 10000;

int main()
{
	freopen("output.txt", "w", stdout);
	scanf("%d", &T);gets(s);
	for (int t = 0; t < T; t++)
	{
		gets(s);
		for (int i = 0; i < 20; i++)
		{
			mas[0][i] = 0;
			mas[1][i] = 0;
		}
		mas[0][0] = 1;
		for (int i = 0; s[i]; i++)
		{
			for (int j = 0; j < 20; j++)
			{
				mas[(i+1)%2][j] = mas[i%2][j];
				if (j > 0 && phrase[j-1] == s[i])
					mas[(i+1)%2][j] = (mas[(i+1)%2][j] + mas[i%2][j-1])%MOD;
			}
			int zz = 0;
		}
		int res = mas[strlen(s)%2][19];
		printf("Case #%d: ", t+1);
		int mm[4];
		for (int i = 0; i < 4; i++)
		{
			mm[i] = res % 10;
			res /= 10;
		}
		for (int i = 3; i >= 0; i--)
			printf("%d", mm[i]);
		printf("\n");

	}

	fclose(stdout);
	return 0;
}