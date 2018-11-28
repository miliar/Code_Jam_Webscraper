#include <stdio.h>
#include <string.h>
#define W 100
#define H 100
#define R 10
#define MOD 10007

int map[H+1][W+1];
int evil[R][2];


int main(void)
{
    int ncase;
    scanf("%d", &ncase);
    for (int casen=1; casen<=ncase; casen++) {
	int h,w,r;
	scanf("%d %d %d", &h, &w, &r);
	for(int i=0; i<r; i++) {
	    scanf("%d %d", &evil[i][0], &evil[i][1]);
	}
	memset(map, 0, sizeof(map));
	map[1][1] = 1;

	for(int i=1; i<=h; i++)
	    for(int j=1; j<=w; j++) {
		int isevil = 0;
		for(int k=0; k<r; k++)
		    if(i == evil[k][0] && j == evil[k][1]) {
			isevil = 1;
			break;
		    }

		if (isevil)
		    map[i][j] = 0;
		else {
		    if(j>2)
			map[i][j] += map[i-1][j-2];
		    if(i>2)
			map[i][j] += map[i-2][j-1];
		    map[i][j] %= MOD;
		}
		//printf("%d%c", map[i][j], j==w?'\n': ' ');
	    }
	
	printf("Case #%d: %d\n", casen, map[h][w]);
    }
}
