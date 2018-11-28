#include <cstdio>
char t[4][4];
int c[4][4];
int row[4], col[4], dig[2];
bool comp;
bool f;
int main()
{
	int n, i, j, k;
	scanf("%d", &n);
	for (i = 0; i < n; i++)
	{
		comp = false;
		f = false;
		for (j = 0; j < 4; j++) 
		{
			row[j] = col[j] = 0;
			scanf("%s", t[j]);
			for (k = 0; k < 4; k++)
			{
				if (t[j][k] == '.') 
				{
					c[j][k] = 0;
					comp = true;
				}
				else if (t[j][k] == 'X') c[j][k] = 1;
				else if (t[j][k] == 'O') c[j][k] = 10;
				else c[j][k] = 100;
				row[j] += c[j][k];
			}
		}
		for (j = 0; j < 4; j++)
		{
			//printf("row: %d %d \n", j, row[j]);
			if (row[j] == 4 || row[j] == 103) 
			{
				printf("Case #%d: X won\n", i+1);
				f= true;
				break;
			}	
			else if (row[j] == 40 || row[j] == 130)
			{
				printf("Case #%d: O won\n", i+1);
				f= true;
				break;
			}
		}
		if (f) continue;
		dig[0] = dig[1] = 0;
		for (j = 0; j < 4; j++)
		{
			dig[0] += c[j][j];
			dig[1] += c[j][3-j];
			for (k = 0; k < 4; k++)
			{
				col[j] += c[k][j];
			}
			//printf("col: %d %d\n", j, col[j]);
			if (col[j] == 4 || col[j] == 103) 
			{
				printf("Case #%d: X won\n", i+1);
				f= true;
				break;
			}	
			else if (col[j] == 40 || col[j] == 130)
			{
				printf("Case #%d: O won\n", i+1);
				f= true;
				break;
			}
		}
		if (f) continue;
		for (j = 0; j < 2; j++)
		{
			//printf("%d %d\n", j, dig[j]);
			if (dig[j] == 4 || dig[j] == 103) 
			{
				printf("Case #%d: X won\n", i+1);
				f= true;
				break;
			}	
			else if (dig[j] == 40 || dig[j] == 130)
			{
				printf("Case #%d: O won\n", i+1);
				f= true;
				break;
			}
		}
		if (f) continue;
		if (comp) printf("Case #%d: Game has not completed\n", i+1);
		else printf("Case #%d: Draw\n", i+1);
	}
	return 0;
}
