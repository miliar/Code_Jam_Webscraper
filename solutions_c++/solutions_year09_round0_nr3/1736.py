#include <stdio.h>
#include <string.h>

#define ni(x) scanf("%d", &x)
#define ns(x) scanf("%s", x)
#define ndirs 4
#define valid(r,c) (r>=0 && r<row && c>=0 && c<col)

char line[512];
char text[] = "welcome to code jam";
int ltext = strlen(text);

int dp[512][24];

int main()
{
	int kisses;
	ni(kisses);
	gets(line);

	for(int ks = 1; ks <= kisses; ++ks)
	{
		gets(line);
		//puts(line);
		dp[0][0] = (line[0] == text[0]) ? 1 : 0;
		int p;
		for(p = 1; line[p]; ++p)
		{

			for(int q=0;q<ltext;q++) // enumerate state
			{
				int laststatecount = q ? dp[p-1][q-1] : 1;
				dp[p][q] = dp[p-1][q] + laststatecount * (line[p] == text[q]);
				//printf("%d ", dp[p][q]);
				dp[p][q] %= 10000;
				
			}
			//puts("");
		}
		printf("Case #%d: %04d\n", ks, dp[p-1][ltext-1]);
	}
}
