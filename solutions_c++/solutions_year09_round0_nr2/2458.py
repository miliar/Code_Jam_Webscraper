#include <stdio.h>
#include <string.h>

int p[110][110], r[110][110], t, w, h, ff, highest, basin[300];

int scan(int x, int y, int cur) {
	int yy=cur, b=0, x1,y1;
//	printf("%d %d %d == %d\n", x, y, p[x][y], yy);
	if (x-1>=0 && p[x-1][y] < yy && p[x-1][y]>=0) yy = p[x-1][y];
	if (x+1 < h && p[x+1][y] < yy && p[x+1][y]>=0) yy = p[x+1][y];
	if (y+1 < w && p[x][y+1] < yy && p[x][y+1]>=0) yy = p[x][y+1];
	if (y-1>=0 && p[x][y-1] < yy && p[x][y-1]>=0) yy = p[x][y-1];
	if (yy<cur) {
		b=0;
		if (x+1 < h && p[x+1][y] == yy) {
			b++;
			x1=x+1; y1=y;
		}
		if (y+1 < w && p[x][y+1] == yy) {
			b++;
			x1=x; y1=y+1;
		}
		if (y-1>=0 && p[x][y-1] == yy) {
			b++;
			x1=x; y1=y-1;
			}
		if (x-1>=0 && p[x-1][y] == yy) {
			b++;
			x1=x-1; y1=y;
		}
		return r[x][y] = scan(x1,y1,yy);
	}
	else {
		if (r[x][y]==0) {
			r[x][y] = ff;
			ff--;
		}
		return r[x][y];
	}
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d", &t);
	for (int t1=0; t1<t; t1++) {
		scanf("%d %d", &h, &w);
		highest = 0;
		for (int i=0; i<h; i++) {
			for (int j=0; j<w; j++) {
				scanf("%d", &p[i][j]);
			}
		}
		int flag = 1;
		ff=-100;
		memset(r, 0, sizeof(r));
		while (flag) {
			flag=0;
			highest = -1;
			for (int i=0; i<h; i++) {
				for (int j=0; j<w; j++) {
					if (r[i][j]==0 && p[i][j] > highest) highest = p[i][j];
				}
			}
			if (highest > -1) {
				flag=1;
			}
			else break;
			for (int i=0; i<h; i++) {
				for (int j=0; j<w; j++) {
					if (r[i][j]==0 && highest == p[i][j])
						scan(i,j, p[i][j]);
				}
			}
		}
		printf("Case #%d:\n", t1+1);
		memset(basin, 0, sizeof(basin));
		int bb=0;
		for (int i=0; i<h; i++) {
			for (int j=0; j<w; j++) {
				if (basin[-r[i][j]] == 0) {
					basin[-r[i][j]] = 'a'+bb;
					bb++;
				}
				p[i][j] = basin[-r[i][j]];
			}
		}
		for (int i=0; i<h; i++) {
			for (int j=0; j<w; j++) {
				if (j>0) printf(" %c", basin[-r[i][j]]);
				else printf("%c", p[i][j]);
			}
			printf("\n");
		}
	}
	return 0;
}
