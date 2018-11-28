#include<stdio.h>
#include<string.h>
#include<iostream>
#include<stdlib.h>


#define SZ 505
#define SZ2 21

using namespace std;

int memo[SZ][SZ2];
char line[SZ];


int main()
{
//	freopen("C-small-attempt0.in", "rt", stdin);
//	freopen("C-small.out", "wt", stdout);

	freopen("C-large.in", "rt", stdin);
	freopen("C-large.out", "wt", stdout);

	string s = "welcome to code jam";
	int kase, n, i, j;
	scanf("%d", &n);
	gets(line);
	for(kase = 1; kase <= n; kase++)
	{
		gets(line);
		int len = strlen(line);
		for(i = 0; i < len; i++)
		{
			memo[i][0] = 1;
		}
		for(i = 1; i <= len; i++)
		{
			for(j = 1; j <= s.length(); j++)
			{
				if(line[i - 1] == s[j - 1])
				{
					memo[i][j] = (memo[i-1][j-1] + memo[i - 1][j]) % 10000;
				}
				else
				{
					memo[i][j] = memo[i - 1][j];
				}
			}
		}
		printf("Case #%d: %04d\n",kase, memo[len][s.length()]);
	}
	return 0;
}
