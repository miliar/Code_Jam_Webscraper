#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define MAX_ALT 10001
#define MAX_SIZE 102

int alt[MAX_SIZE][MAX_SIZE];
int dir[MAX_SIZE][MAX_SIZE];
int conv[4][2]={{-1,0},{0,-1},{0,1},{1,0}};
int basin[MAX_SIZE][MAX_SIZE];
char names[30];
int i, j, k, l, m, s;
bool solved;

int N, H, W;

int main() {
	scanf("%d", &N);

	for (i=1; i<=N; i++) {
		scanf("%d %d", &H, &W);
	
		for (k=0;k<=W+1;k++) 
			alt[0][k] = alt[H+1][k] = MAX_ALT;

		for (j=1;j<=H; j++) {
			alt[j][0] = alt[j][W+1] = MAX_ALT;
			for (k=1;k<=W;k++) scanf("%d", &alt[j][k]);
		}

		/* find the sinks */
		s=1;
		for (j=1;j<=H;j++)
			for (k=1;k<=W;k++) 
				if (alt[j][k]<=alt[j-1][k] &&
						alt[j][k]<=alt[j+1][k] &&
						alt[j][k]<=alt[j][k-1] &&
						alt[j][k]<=alt[j][k+1]) {
					basin[j][k]=s++;
				} else {
					basin[j][k]=0;
					m=MAX_ALT;
					for (l=0;l<=3;l++) {
						if (alt[j+conv[l][0]][k+conv[l][1]] < m) {
							m=alt[j+conv[l][0]][k+conv[l][1]];
							dir[j][k]=l;
						}
					}
				}

		/* fill basins */
		do {
			solved = true;

			for (j=1;j<=H;j++) 
	            for (k=1;k<=W;k++)
					if (!basin[j][k]) {
						if (basin[j+conv[dir[j][k]][0]][k+conv[dir[j][k]][1]])
							basin[j][k]=basin[j+conv[dir[j][k]][0]][k+conv[dir[j][k]][1]];
						else
							solved=false;
					}
		} while (!solved);

		m='a';
		memset(names,0,sizeof(names));
		printf("Case #%d:\n", i);
        for (j=1;j<=H;j++) {
            for (k=1;k<=W;k++) {
				if (k>1) printf(" ");
				if (!names[basin[j][k]])
					names[basin[j][k]]=m++;
				printf("%c ", names[basin[j][k]]);
			}
			printf("\n");
		}


	}
}
