#include<stdio.h>
#include<algorithm>
using namespace std;

char s[600];
char l[] = "welcome to code jam";
int cnt[600][30];

int solve()
{
	int L = strlen(s);
	memset(cnt, 0, sizeof(cnt));
	for (int i = 0; i < L; i++)
	{
		for (int j = 0; j < 19; j++)
		{
			if (i > 0)
				cnt[i][j] = cnt[i-1][j];			
			if (s[i] != l[j])
				continue;
			if (j == 0)
				cnt[i][j] += 1;
			else
				cnt[i][j] += (i>=1) * cnt[i-1][j-1];
			cnt[i][j] %= 10000;
//			printf("%d %d -- %d\n", i, j, cnt[i][j]);
		}
	}
	return cnt[L-1][18];
}
	

int main()
{
	int tc;
	scanf("%d", &tc);
	gets(s);
	for (int i = 1; i <= tc; i++)
	{
		gets(s);
		printf("Case #%d: %04d\n", i, solve());
	}
	return 0;
}
 
