#include <stdio.h>
#include <string.h>

int a[105];
int r[50][50];
int f[50][50];
char s[1000];

int main ()
{
	//freopen("B-large (1).in", "r", stdin);
	//freopen("B-large (1).out", "w", stdout);
	int ca;
	scanf("%d", &ca);
	int c, d, n;
	int kase = 0;
	while (ca--)
	{
		memset(f, -1, sizeof(f));
		memset(r, 0, sizeof(r));
		scanf("%d", &c);		
		for (int i = 0; i < c; i++)
		{
			scanf("%s", s);
			int x = s[0] - 'A';
			int y = s[1] - 'A';
			int z = s[2] - 'A';
			f[x][y] = f[y][x] = z; 
		}
		scanf("%d", &d);
		for (int i = 0; i < d; i++)
		{
			scanf("%s", s);
			int x = s[0] - 'A';
			int y = s[1] - 'A';
			r[x][y] = r[y][x] = 1;
		}
		scanf("%d", &n);
		scanf("%s", s);
		int top = 0;
		int x = s[0] - 'A';
		a[top++] = x;
		for (int i = 1; i < n; i++)
		{
			int x = s[i] - 'A';
			a[top++] = x;
			int y = -1;
			if (top > 1) y = a[top - 2];
			int t = -1;
			if (y != -1) 
			{
				if (f[x][y] != -1) t = f[x][y];
				if (f[y][x] != -1) t = f[y][x];
			}
			if (t != -1)
			{
				top -= 2;
				a[top++] = t;
			}
			else
			{
				for (int j = top - 2; j >= 0; j--)
				{
					int z = a[j];
					if (r[x][z] || r[z][x])
					{
						top = 0;
						break;
					}
				}
			}
		}
		printf("Case #%d: [", ++kase);
		for (int i = 0; i < top; i++)
		{
			putchar(a[i] + 'A');
			if (i != top - 1) printf(", ");
		}
		printf("]\n");
	}
	return 0;
}
