#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <map>
#include <set>
#define mp make_pair
using namespace std;

char mat [5000][5000][2];
int nl [5000];
int nc [5000];
int n;
int mx, my;

int read () {
	memset (mat, 0, sizeof (mat));
	int r;
	scanf ("%d", &r);
	
	int x1, x2, y1, y2;
	n = mx = my = 0;
	for (int i = 0; i < r; ++i) {
		scanf ("%d%d%d%d", &x1, &y1, &x2, &y2);
		for (int i = y1; i <= y2; ++i) {
			for (int j = x1; j <= x2; ++j) {
				n += 1-mat[i][j][0];
				mat[i][j][0] = 1;
				
				my = max (my, i);
				mx = max (mx, j);
			}
		}
	}
}

int caso = 1;
void process () {
	int t = 0;
	int l = 0, l2 = 1, cont;
	while (n) {
		t++;
		//printf ("%d %d (%d): %d %d\n", t, l, n, my, mx);
		for (int i = 0; i <= my+1; ++i) {
			for (int j = 0; j <= mx+1; ++j) {
				//printf ("%d", mat[j][i][l]);
				cont = 0;
				if (j && mat[i][j-1][l]) cont++;
				if (i && mat[i-1][j][l]) cont++;
				switch (cont) {
					case 0:
						if (mat[i][j][l]) {
							n--;
						}
						mat[i][j][l2] = 0;
						break;
					case 1:
						mat[i][j][l2] = mat[i][j][l];
						break;
					case 2:
						if (!mat[i][j][l]) n++;
						mat[i][j][l2] = 1;
				}
				if (mat[i][j][l]) {
					if (i > my) my = i;
					if (j > mx) mx = j;
				}
			}	
			//printf ("\n");
		}
		l = l2;
		l2 = 1-l2;
		//printf ("\n");
	}
	printf ("Case #%d: %d\n", caso++,t);
	fflush (stdout);
}

int main () {
	int t;
	scanf ("%d", &t);
	
	while (t--) { read(); process(); }
	return 0;
}

