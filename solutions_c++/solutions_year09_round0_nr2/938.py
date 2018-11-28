#include <cstdio>

using namespace std;

const int MAXN	= 128;
const int dy[] 		= {-1, 0, 0, 1};
const int dx[] 		= {0, -1, 1, 0};
const int dsize		= 4;

int test_cases;
int H, W;
int gmap[MAXN][MAXN];
char dp[MAXN][MAXN];
char alpha;

char solve(int posy, int posx) {
	//printf("%d; %d\n", posy, posx);
	int minn = 10001, index = -1;
	
	for (int k = 0; k < dsize; ++k) {
		int d1y = posy + dy[k];
		int d1x = posx + dx[k];
		if ( d1y >= 0 && d1y < H && d1x >= 0 && d1x < W && gmap[d1y][d1x] < minn ) {
			minn = gmap[d1y][d1x];
			index = k;
		}
	}
	if (minn >= gmap[posy][posx])
		return dp[posy][posx] = alpha++;
	if ( dp[ posy + dy[index] ][ posx + dx[index] ] != '-' )
		return dp[posy][posx] = dp[ posy + dy[index] ][ posx + dx[index] ];
	return dp[posy][posx] = solve( posy + dy[index], posx + dx[index] );
}

int main () {
	
	scanf ("%d", &test_cases);
	
	for (int i = 1; i <= test_cases; ++i) {
		scanf ("%d %d", &H, &W);
		alpha = 'a';
		
		for (int j = 0; j < H; ++j)
			for (int k = 0; k < W; ++k)
				scanf ("%d", &gmap[j][k]);
		
		for (int i1 = 0; i1 < H; ++i1)
			for (int j1 = 0; j1 < W; ++j1) dp[i1][j1] = '-';
				
		for (int i1 = 0; i1 < H; ++i1)
			for (int j1 = 0; j1 < W; ++j1)
				if ( dp[i1][j1] == '-' )
					solve(i1, j1);
				
		printf("Case #%d:\n", i);
		for (int i1 = 0; i1 < H; ++i1)
			for (int j1 = 0; j1 < W; ++j1)
				printf ("%c%c", dp[i1][j1], (j1 == W-1) ? '\n' : ' ');
	}
	
	return 0;
}