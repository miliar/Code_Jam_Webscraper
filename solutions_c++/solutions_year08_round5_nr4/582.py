#include<stdio.h>

int flag[110][110];
int not[110][110];
int h,w;

int search( int i, int j)
{
	if( i > h || j > w )
		return 0;
	if( not[i][j] == 1) 
		return 0;
	if( flag[i][j] != 0 )
		return flag[i][j];
	if( i == h && j == w )
	{
		flag[i][j] = 1;
		return 1;
	}
	int cur = 0;
	cur += search(i+1, j+2) + search(i+2, j+1);
	flag[i][j] = cur % 10007;
	return cur;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	int ca;
	for( ca = 1; ca <= T; ca ++ )
	{
		int i, j;
		for( i=0; i<110; i++)
			for(j=0; j<110; j++)
			{
				flag[i][j] =0;
				not[i][j] = 0;
			}
		int r;
		scanf("%d%d%d", &h, &w, &r);
		while( r -- )
		{
			int x,y;
			scanf("%d%d", &x, &y);
			not[x][y] = 1;
		}
	//	search(1, 1);
		flag[1][1] = 1;
		for( i=1; i<=h; i++ )
		{
			for( j=1; j<=w; j++ )
			{
				flag[i+1][j+2] += flag[i][j];
				flag[i+1][j+2] = flag[i+1][j+2]%10007;
				if( not[i+1][j+2] == 1 )
					flag[i+1][j+2] = 0;
				flag[i+2][j+1] += flag[i][j];
				flag[i+2][j+1] = flag[i+2][j+1]%10007;
				if( not[i+2][j+1] == 1 )
					flag[i+2][j+1] = 0;
			}
		}
		printf("Case #%d: %d\n", ca, flag[h][w]);
	}
	return 0;
}