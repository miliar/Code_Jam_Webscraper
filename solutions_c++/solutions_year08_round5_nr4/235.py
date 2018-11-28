#include <cstdio>
#include <cstring>

int W, R, H;
int memo[200][200];

int go(int x, int y)
{
	if( x == H && y == W )
		return 1;
	if( x > H || y > W )
		return 0;
	if( memo[x][y] != -1 )
		return memo[x][y];
	return memo[x][y] = ((go(x+1,y+2)+go(x+2,y+1))%10007);
}

int main()
{
	int K;
	scanf("%d", &K);
	for(int k = 1; k <= K; k++)
	{
		printf("Case #%d: ", k);
		scanf("%d %d %d", &H, &W, &R);

		memset( memo, -1, sizeof( memo ) );
		for(int i = 0; i < R; i++)
		{
			int a, b;
			scanf("%d %d", &a, &b);
			memo[a][b] = 0;
		}

		printf("%d\n", go(1, 1) );
	}
}