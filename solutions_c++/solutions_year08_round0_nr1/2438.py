# include <stdio.h>
# include <string.h>
# include <limits.h>
# define MAXS 128
# define MAXQ 1024
# define min(x, y) (x)<(y)?(x):(y)

char name[MAXS][MAXS];
int S, Q, N;
int q[MAXQ];
int c[MAXS][MAXQ];
int p[MAXS][MAXQ];

/*int calc(int si, int qi)
{
	
}*/

int main()
{
	int i, kase=1, k, ret, r, minval, j;
	char tmp[5000];

	freopen("saving.in", "r", stdin);
	freopen("saving.out", "w", stdout);

	//while(1)
	{
		gets(tmp); sscanf(tmp, "%d", &N);
		while(N--)
		{
			printf("Case #%d: ", kase++);
			
			gets(tmp); sscanf(tmp, "%d", &S);

			for(i = 0; i < S; i++)
			{
				gets(name[i]);
			}

			gets(tmp); sscanf(tmp, "%d", &Q);

			for(k = i = 0; i < Q; i++)
			{
				gets(tmp);
				for(j = 0; j < S; j++)
				{
					if(!strcmp(name[j], tmp))
					{
						q[k++] = j;
						break;
					}
				}
				if(j == S)
				{
					q[k++] = S+1;
				}
			}
			
			for(i = 0; i < S; i++)
			{
				p[i][Q] = INT_MAX;
				for(j = Q-1; j>=0; j--)
				{	
					if(q[j] == i)
					{
						p[i][j] = i;
					}
					else
					{
						p[i][j] = p[i][j+1];
					}
				}
			}

			for(i = 0; i <= S; i++)
			{
				for(j = 0; j <= Q; j++)
				{
					c[i][j] = INT_MAX;
				}
			}
			
			for(i = 0; i < S; i++)
			{
				if(q[Q-1] == i)
				{
					c[i][Q-1] = 1;
				}
				else
				{
					c[i][Q-1] = 0;
				}
			}

			/*ret = INT_MAX;
			for(i = 0; i < S; i++)
			{
				r = calc(i, 0);
				ret = min(ret, r);
			}*/

			for(j = Q-2; j>= 0; j--)
			{
				for(i = 0; i < S; i++)
				{
					if(q[j] != i)
					{
						c[i][j] = c[i][j+1];	
					}
					else
					{
						minval = INT_MAX;
						for(k = 0; k < S; k++)
						{
							if(k == i)continue;
							minval = min(minval, c[k][j+1]);
						}
						c[i][j] = minval + 1;
					}
				}
			}
			
			ret = INT_MAX;
			for(i = 0; i < S; i++)
			{
				ret = min(ret, c[i][0]);	
			}
			if(Q == 0)ret = 0;
			printf("%d\n", ret);
		}	
	}


	return 0;
}
