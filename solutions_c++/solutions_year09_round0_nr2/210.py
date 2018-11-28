#include <stdio.h>

int alt [100][100];
int rep[100][100];
char let[100][100];
int inci[5] = {-1,0,0,1,0};
int incj[5] = {0,-1,1,0,0};

char nl;
char fs (int i, int j) {
	if (let[i][j]) return let[i][j];
	else if (rep[i][j] == 5) return let[i][j] = nl++;
	else return let[i][j] = fs (i + inci[rep[i][j]], j + incj[rep[i][j]]);
}

int main () {
	int h, w;
	int t;
	freopen ("B.in","r",stdin);
	freopen ("B-large.out","w",stdout);
	scanf ("%d", &t);
		
	for (int caso = 1; caso <= t; ++caso) {
		scanf ("%d%d", &h, &w);
		for (int i = 0; i < h; ++i) {
			for (int j = 0; j < w; ++j) {
				scanf ("%d", &alt[i][j]);	
				rep[i][j] = 5;
				let[i][j] = 0;
			}
		}
		int m;
		int pm;
		nl = 'a';
		for (int i = 0; i < h; ++i) {
			for (int j = 0; j < w; ++j) {
				m = alt[i][j];
				pm = 5;
				for (int k = 0; k < 4; ++k) {
					int ni = i + inci[k];
					int nj = j + incj[k];
					if (ni < 0 || ni >= h || nj < 0 || nj >= w) continue;
					if (alt[ni][nj] < m) {
						m = alt[ni][nj];
						pm = k;	
					}
				}
				rep[i][j] = pm;
			}	
		}
		
		printf ("Case #%d:\n", caso);
		for (int i = 0; i < h; ++i) {
			for (int j = 0; j < w; ++j) {
				if (j) printf (" %c", fs(i,j));
				else printf ("%c", fs(i,j));
			}
			printf ("\n");
		}
	}
	return 0;	
}
