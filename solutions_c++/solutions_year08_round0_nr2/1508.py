#include <stdlib.h>
#include <stdio.h>
#include <string.h>

// A, B, minutes
int tab[2][4000];

int case_cnt;
int case_max;

int addon;
int trains_a;
int trains_b;

int main ( int argc, char ** argv ) {

	scanf("%d", &case_max);
	for (case_cnt = 0; case_cnt < case_max; case_cnt++) {
		scanf("%d", &addon);
		scanf("%d %d", &trains_a, &trains_b);

		int a,b,c,d;
		int x,y;

		int an, ab;

		memset( tab, 0, sizeof(tab) );
		for (x=0; x<trains_a; x++) {
			
			scanf("%d:%d %d:%d", &a, &b, &c, &d);
			ab = a * 60 + b;
			an = c * 60 + d + addon;

			for (y=ab; y<4000; y++) {
				tab[0][y]--;
			}

			for (y=an; y<4000; y++) {
				tab[1][y]++;
			}
		}
	
		for (x=0; x<trains_b; x++) {
			
			scanf("%d:%d %d:%d", &a, &b, &c, &d);
			ab = a * 60 + b;
			an = c * 60 + d + addon;

			for (y=ab; y<4000; y++) {
				tab[1][y]--;
			}

			for (y=an; y<4000; y++) {
				tab[0][y]++;
			}
		}

		int min[2];
		min[0] = 0;
		min[1] = 0;

		for (a=0; a<2; a++) {
			for (b=0; b<4000; b++) {
				if ( tab[a][b] < min[a] ) {
					min[a] = tab[a][b];
				}
			}
		}

		printf("Case #%d: %d %d\n", case_cnt+1, -min[0], -min[1] );





		
	}
	return 0;
}
