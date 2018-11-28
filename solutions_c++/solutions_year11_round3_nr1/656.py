#include<stdio.h>
#include<cstring>
#define MAX 60
char a[MAX][MAX];
int main()
{
	memset(a, 0, sizeof(a));
	int t;
	int tp = 0;
	int i, j;
	int n, m;
	scanf("%d", &t);
	while(t--)
	{
		tp++;
		scanf("%d%d", &m, &n);
		for(i=0; i<m; ++i)
		{
			getchar();
			for(j=0; j<n; ++j)
			{
				scanf("%c", &a[i][j]);
			}
		}

		int imp = 0;
		for(i=0; i<m; ++i)
		{
			for(j=0; j<n; ++j)
			{
				if(a[i][j] == '#')
				{
					if(a[i][j+1] == '#' && a[i+1][j] == '#' && a[i+1][j+1] == '#')
					{
						a[i][j] = '/';
						a[i+1][j] = 'i'; 
						a[i][j+1] = 'i';
						a[i+1][j+1] = '/';
					}
					else
					{
						imp = 1;
						break;
					}
				}
			}
			if(imp == 1)
				break;
		
		}
		printf("Case #%d:\n", tp);
		if(imp == 1)
			printf("Impossible\n");
		else
		{
			for(i=0; i<m; i++)
			{
				for(j=0; j<n; ++j)
				{
					if(a[i][j] == 'i')
						printf("\\");
					else
					{
						printf("%c", a[i][j]);
					}
				}
				printf("\n");
			}
		}
	}
	return 0;
}


