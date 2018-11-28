#include <stdio.h>
#include <iostream>
#include <string.h>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
using namespace std;


int maze[33][33];
int ans[35];

int main()
{

	int ca, c;

	int r, k, n, d, m, l, t;
	int i, j;

	char s[100];

	freopen("c:\\C-small-attempt1.in", "r", stdin);
	freopen("c:\\C-small-attempt1.out", "w+", stdout);

	scanf("%d", &ca);
	for(c = 1; c <= ca; c++)
	{
		scanf("%d%d", &m, &n);

		memset(maze, -1, sizeof(maze));
		memset(ans, 0, sizeof(ans));
		for(i = 0;i < m; i++)
		{
			scanf("%s", &s);
			for(j = 0;j < n/4; j++)
			{
				int tmp;
				if(s[j]  >= '0' && s[j] <= '9')
					tmp = s[j] - '0';
				else tmp = s[j] - 'A' + 10;
				maze[i][j*4]   = (tmp&8)/8;
				maze[i][j*4+1] = (tmp&4)/4;
				maze[i][j*4+2] = (tmp&2)/2;
				maze[i][j*4+3] = tmp&1;
			}
		}

		/*
		for(i = 0;i< m; i++)
		{
			for(j = 0;j < n; j++)
			{
				printf("%d", maze[i][j]);
			}
			printf("\n");
		}*/

		int si = m > n ? n : m;
		int sum = m*n;
		int cc = 0;
		bool find;


		for(i = si; i >= 2; i--)
		{
			ans[i] = 0;
			for(j = 0;j < m; j++)
			{
				if(j + i - 1 >= m) continue;
				for(k = 0;k < n; k++)
				{
					if(k + i - 1 >= n) continue;
					find = true;
					for(l = j;l < j+i; l++)
					{
						for(t = k;t < k+i; t++)
						{
							if(maze[l][t] == -1)
							{
								find = false;
								goto ok;
							}

							if(t-1 >= k)
							{
								if((maze[l][t-1] && maze[l][t]) || ((!maze[l][t-1])&&(!maze[l][t])) )
								{
									find = false;
									goto ok;
								}
							}

							if(l-1 >= j)
							{
								if((maze[l-1][t] && maze[l][t]) || ((!maze[l-1][t])&&(!maze[l][t])) )
								{
									find = false;
									goto ok;
								}
							}


						}
					}
ok:                 if(find == true)
					{
						ans[i]++;
						for(l = j;l < j+i; l++)
						{
							for(t = k;t < k+i; t++)
							{
								maze[l][t] = -1;
							}
						}
					}
				}
			}


			if(ans[i] > 0) cc++;
			sum -= i*i*ans[i];
		}
	//	printf("%d\n", sum);
		if(sum > 0) cc++;
		ans[1] = sum;
		
		printf("Case #%d: %d\n", c, cc);
		for(i = si;i >= 1; i--)
		{
			if(ans[i] > 0) printf("%d %d\n", i, ans[i]);
		}

	}
	return 0;
}