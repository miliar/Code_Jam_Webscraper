#include <cstdio>
#include <cstring>

const int MAX_N = 100 + 5;

int T;
int R;
int a[MAX_N][MAX_N];
int main()
{
	scanf("%d", &T);
	for(int t = 0; t < T; t ++)
	{
		scanf("%d", &R);
		memset(a, 0, sizeof(a));
		for(int i = 0; i < R; i ++)
		{
			int x1, x2, y1, y2;
			scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
			for(int x = x1; x <= x2; x ++)
				for(int y = y1; y <= y2; y ++)
					a[x][y] = 1;
		}
		int ans = 0;
		while( 1 )
		{
			int cnt = 0;
			for(int i = 1; i <= 100; i ++)
				for(int j = 1; j <= 100; j ++)
					cnt += a[i][j];
			if(!cnt)	break;
			ans ++;
			for(int x = 100; x >= 1; x --)
				for(int y = 100; y >= 1; y --)
				{
					if( a[x - 1][y] && a[x][y - 1] )
						a[x][y] = 1;
					if( !a[x - 1][y] && !a[x][y - 1] )
						a[x][y] = 0;
				}
		}
		printf("Case #%d: %d\n", t + 1, ans);
	}
}
