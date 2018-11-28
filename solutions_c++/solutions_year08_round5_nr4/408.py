/* kaneko-A.cc
 */
#include <iostream>
#include <cstdio>
using namespace std;
const int Q = 10007;
int T, H, W, R, table[100][100], rock[100][100];
int main()
{
    cin >> T;
    for (int t=0; t<T; ++t) {
	cin >> H >> W >> R;
	for (int y=0; y<H; ++y)
	    for (int x=0; x<W; ++x)
		table[x][y] = rock[x][y] = 0;
	for (int i=0; i<R; ++i) {
	    int r, c;
	    cin >> r >> c;
	    rock[c-1][r-1] = 1;
	}
	table[0][0] = 1;
	for (int y=0; y+1<H; ++y) {
	    for (int x=0; x+1<W; ++x) {
		if (!table[x][y]) continue;
		if (x+2<W && rock[x+2][y+1] == 0)
		    table[x+2][y+1] = (table[x+2][y+1]+table[x][y])%Q;
		if (y+2<H && rock[x+1][y+2] == 0)
		    table[x+1][y+2] = (table[x+1][y+2]+table[x][y])%Q;
	    }
	}
#if 0
	for (int y=0; y<H; ++y) {
	    for (int x=0; x<W; ++x)
		printf(" %5d", rock[x][y] ? -1 : table[x][y]);
	    printf("\n");
	}
#endif
	printf("Case #%d: %d\n", t+1, table[W-1][H-1]);
    }
}
