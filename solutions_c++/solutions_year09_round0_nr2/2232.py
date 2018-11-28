#include<iostream>
#include<cstdio>

using namespace std;

const int dx[4] = {-1, 0, 0, 1};
const int dy[4] = {0, -1, 1, 0};

int Map[110][110];
char cc[10010];
int W, H;
int father[10010];

int findfather( int t )
{
	if ( father[t] == -1 ) return t;
	else return (father[t] = findfather(father[t]));
}

int main()
{
	freopen( "in.txt", "r", stdin );
	freopen( "out.txt", "w", stdout );
	int test_cases; scanf( "%d", &test_cases );
	for (int TT = 0; TT < test_cases; TT++ )
	{
		scanf( "%d %d", &H, &W );
		for (int i = 0; i < H; i++ )
			for (int j = 0; j < W; j++ )
				scanf( "%d", &Map[i][j] );
		memset( father, 0xff, sizeof( father ) );
		for (int i = 0; i < H; i++ )
			for (int j = 0; j < W; j++ )
			{
				int tmin = Map[i][j], tx, ty;
				for (int k = 0; k < 4; k++ )
				{
					tx = i + dx[k]; ty = j + dy[k];
					if ( tx < 0 || tx >= H || ty < 0 || ty >= W ) continue;
					if ( Map[tx][ty] >= tmin ) continue;
					tmin = Map[tx][ty];
					father[i * W + j] = tx * W + ty;
				}
			}
		char r = 'a';
		memset( cc, 0, sizeof( cc ) );
		for (int i = 0; i < H; i++ )
			for (int j = 0; j < W; j++ )
			if ( cc[findfather(i * W + j)] == 0 )
				cc[findfather(i * W + j)] = r ++;
		printf( "Case #%d:\n", TT + 1 );
		for (int i = 0; i < H; i++ )
			for (int j = 0; j < W; j++ )
				printf( "%c%c", cc[findfather(i * W + j)], (j == W - 1 ? '\n' : ' ') );
	}
}
