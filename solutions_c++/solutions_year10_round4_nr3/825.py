#include <stdio.h>
#include <string.h>

int a[110][110];

int T, ti, ans, i, j, x, y, r,x1, y1, x2, y2;
bool flag;

int main()
{
	freopen("c.txt", "r", stdin);
	freopen("c.out", "w", stdout);	
	scanf("%d", &T);
	for (ti=1; ti<=T; ti++)
	{
		scanf("%d", &r);
		memset(a, 0, sizeof(a));
		for (i=0; i<r; i++)
		{
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			for (x=x1; x<=x2; x++)
			 for (y=y1; y<=y2; y++)
			   a[x][y]=1;
		}
		for (ans=1; ans; ans++)
		{
			bool flag=false;
			for (i=100; i>=1; i--)
			 for (j=100; j>=1; j--)
			 {
			 	if (a[i-1][j] && a[i][j-1]) a[i][j]=1;
			 	if (!a[i-1][j] && !a[i][j-1]) a[i][j]=0;
			 	if (a[i][j]) flag=true;
			 }
			if (!flag) break; 
		}
		printf("Case #%d: %d\n",ti, ans);
	}

	return 0;
}
