#include<cstdio>

using namespace std;

int mas[51][51];
int res[51][51];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	int i, j, k;
	for(i = 0; i<T; i++)
	{
		int R, C;
		int count_blue = 0;
		scanf("%d%d", &R, &C);
		char c;
		getchar();
		for(k = 0; k<R; k++)
		{
			for(j = 0; j<C; j++)
			{
				c = getchar();
				if(c == '.')
				{
					mas[k][j] = 0;
					res[k][j] = 0;
				}
				if(c == '#')
				{
					mas[k][j] = 1;
					count_blue++;
				}
			}
			getchar();
		}
		printf("Case #%d:\n", i+1);
		if(count_blue%4!=0)
		{
			printf("Impossible\n");
			continue;
		}
		bool right = true;
		for(k = 0; k<R; k++)
		{
			for(j = 0; j<C; j++)
			{
				if(mas[k][j] == 1)
				{
					if(k+1<R && mas[k+1][j] == 1)
					{
						if(j+1<C && mas[k][j] == 1)
						{
							if(mas[k+1][j+1] == 1)
							{
								res[k+1][j+1] = 5;
								res[k][j+1] = 3;
								res[k+1][j] = 4;
								res[k][j] = 2;
								mas[k+1][j+1] = 0;
								mas[k][j+1] = 0;
								mas[k+1][j] = 0;
								mas[k][j] = 0;
							}
							else
							{
								right = false;
								break;
							}
						}
						else
						{
							right = false;
							break;
						}
					}
					else
					{
						right = false;
						break;
					}
				}
			}
			if(right == false)
				break;
		}
		if(right == false)
		{
			printf("Impossible\n");
			continue;
		}
		for(k = 0; k<R; k++)
		{
			for(j = 0; j<C; j++)
			{
				if(res[k][j] == 0)
					putchar('.');
				if(res[k][j] == 2)
					putchar('/');
				if(res[k][j] == 3)
					putchar('\\');
				if(res[k][j] == 4)
					putchar('\\');
				if(res[k][j] == 5)
					putchar('/');
			}
			puts("");
		}
	}
	return 0;
}