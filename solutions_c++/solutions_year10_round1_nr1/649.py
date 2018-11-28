#include<cstdio>

int main()
{
	int T, cas;
	scanf("%d", &T);
	for(cas = 1; cas <=T; cas ++)
	{
		int n, k;
		int i, j, ii, jj;
		int d[4][2] = {{1,-1}, {1,1}, {0,1}, {1,0}};
		char rec[50][51], tmp[50][51];
		scanf("%d %d", &n, &k);
		for(i = 0; i < n; i ++)
		{
			scanf("%s", rec[i]);
			tmp[i][n] = '\0';
		}
		for(i = 0; i < n; i ++)
		{
			for(j = 0; j < n; j ++)
			{
				tmp[i][j] = rec[n-1-j][i];
			}
		}
		/*putchar('\n');
		for(i = 0; i < n; i++)
		{
			puts(tmp[i]);
		}*/
		for(j = 0; j < n; j ++)
		{
			for(i = 0; i < n; i ++)
			if(tmp[i][j] == '.')
			{
				for(ii = i; ii >= 1; ii --)
				{
					tmp[ii][j] = tmp[ii-1][j];
					tmp[ii-1][j] = '.';
				}
			}
		}
		/*putchar('\n');
		for(i = 0; i < n; i++)
		{
			puts(tmp[i]);
		}*/
		int res = 0;
		for(i = 0; i < n; i ++)
		{
			for(j = 0; j < n; j ++)
			if(tmp[i][j] != '.')
			{
				for(jj = 0; jj < 4; jj ++)
				{
					for(ii = 0; ii < k; ii ++)
					{
						int nexti, nextj;
						nexti = i + d[jj][0]*ii;
						nextj = j + d[jj][1]*ii;
						if(nexti < n && nexti >= 0
						&& nextj < n && nextj >= 0
						&& tmp[nexti][nextj] == tmp[i][j])
						{
						}
						else {
							break;
						}
					}
					if(ii == k){
						if(tmp[i][j] == 'R')
						{
							res |= 1;
						}
						else {
							res |= 2;
						}
						break;
					}
				}
			}
		}
		if(res == 0)printf("Case #%d: Neither\n", cas);
		if(res == 1)printf("Case #%d: Red\n", cas);
		if(res == 2)printf("Case #%d: Blue\n", cas);
		if(res == 3)printf("Case #%d: Both\n", cas);
	}
	return 0;
}
