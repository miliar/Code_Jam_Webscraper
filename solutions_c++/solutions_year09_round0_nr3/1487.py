#include <cstdio>
#include<stdlib.h>
#include<cmath>
#include<algorithm>
#include<string.h>
using namespace std;

#define DEBUG 0

int N;
char s1[1000], s2[] = "welcome to code jam\0";
int ans[100][1000];

void solve(void)
{
	for(int i = 0; i < strlen(s2); i++)
		ans[i][0] = 0;

	if(s1[0] == 'w') ans[0][0] = 1;

	for(int i = 1; i < strlen(s1); i++)
	{
		if(s1[i] == 'w') 
			ans[0][i] = ans[0][i - 1] + 1;
		else 
			ans[0][i] = ans[0][i - 1];
	}

	for(int i = 1; i < strlen(s2); i++)
		for(int j = 1; j < strlen(s1); j++)
		{
			if(s2[i] == s1[j]) 
				ans[i][j] = (ans[i - 1][j] + ans[i][j - 1]) % 10000;
			else 
				ans[i][j] = ans[i][j - 1];
		}
}


int main()
{
	freopen("C-large.in","r",stdin);

#if !DEBUG
	freopen ("C-large.out","w",stdout);
#endif

	scanf("%d\n", &N);

	for(int i = 1;i <= N; i++)
	{
		//scanf("%s\n", s1);
		gets(s1);

		solve();

		printf("Case #%d: %04d\n", i, ans[strlen(s2) - 1][strlen(s1) - 1]);

	
	}
	

#if !DEBUG
	fclose (stdout);
#endif

	return 0;
}
