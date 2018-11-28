#include <stdio.h>
#include <algorithm>
#define MAXN 10
#define MAXLEN 100

using namespace std;

int table[MAXLEN][MAXLEN], rock[MAXLEN][MAXLEN];

int main()
{
	int icase, ncase;
	int H, W, n;
	int x, y;
	int i, j;
	scanf("%d", &ncase);
	for(icase=0; icase<ncase; ++icase){
		scanf("%d%d%d", &H, &W, &n);
		for(i=0; i<H; ++i)
			for(j=0; j<W; ++j)
				table[i][j] = rock[i][j] = 0;
		for(i=0; i<n; ++i){
			scanf("%d%d", &x, &y);
			rock[x-1][y-1] = 1;
		}
		table[0][0] = 1;
		for(i=0; i<H; ++i){
			for(j=0; j<W; ++j){
				if(rock[i][j])
					continue;
				if(i-1>=0 && j-2>=0){
					table[i][j] += table[i-1][j-2];
					table[i][j] %= 10007;
				}
				if(i-2>=0 && j-1>=0){
					table[i][j] += table[i-2][j-1];
					table[i][j] %= 10007;
				}
			}
		}

		printf("Case #%d: %d\n", icase+1, table[H-1][W-1]);;
	}
	return 0;
}
int i, j;
