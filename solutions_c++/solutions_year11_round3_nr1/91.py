#include<stdio.h>
int main()
{
	int T, caseNum;
	scanf("%d",&T);
	for(caseNum = 1; caseNum <= T; ++caseNum)
	{
		printf("Case #%d:\n", caseNum);

		int w, h;
		const int N = 53;
		char str[N][N]={0};
		int i,j;
		scanf("%d%d",&h,&w);
		for(i=1;i<=h;++i)scanf("%s",str[i]+1);

		for(i=1;i<=h;++i)for(j=1;j<=w;++j)
		{
			if(str[i][j] == '#')
			{
				if(str[i+1][j+1]=='#' &&
					str[i+1][j] == '#' && 
					str[i][j+1] == '#')
				{
					str[i][j] = str[i+1][j+1] = '/';
					str[i+1][j] = str[i][j+1] = '\\';
				}
				else goto E;
			}
		}
		

		for(i=1;i<=h;++i)
		{
			for(j=1;j<=w;++j)
			{
				putchar(str[i][j]);
			}
			putchar('\n');
		}

		continue;
E:;
		puts("Impossible");
		continue;
	}
	return 0;
}
/*
*/