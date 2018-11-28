#include<stdio.h>
#include<stdlib.h>
#include<math.h>

char a[110][110];
int n,m;

int checkcross(int i, int j, char num) {
	int k;
	int row = 0;
	for (k=0;k<n;k++) {
		if (a[k][j] == num || a[k][j] == 'T') {
			row++;
		}
	}
	if (row > 3) {
		return ( num == 'X' ? 1 : 2);
	}
	row = 0;
	for (k=0;k<m;k++) {
		if (a[i][k] == num || a[i][k] == 'T') {
			row++;
		}
	}
	if (row > 3) {
		return ( num == 'X' ? 1 : 2);
	}
	return 0;
}

int main() {
	FILE *f;
	FILE *g;
	int i,j,testnum,testi;
	fopen_s(&f,"A-large.in","r");
	fopen_s(&g,"output.txt","w");
	fscanf_s(f, "%d\n", &testnum);
	for (testi = 0; testi<testnum; testi++) {
		int gamestatus = 0;
		int haveempty = 0;
		n=m=4;
		for (i=0;i<n;i++) {
			for (j=0;j<m;j++) {
				fscanf_s(f, "%c", &a[i][j], 1);
			}
			fscanf_s(f, "%c", &a[5][5], 2);
		}
		fscanf_s(f, "%c", &a[5][5], 2);
		for (i=0;i<n;i++) {
			for (j=0;j<m;j++) {
				if (a[i][j] == '.') {
					haveempty = 1;
				}
				else {
					gamestatus = checkcross(i,j,a[i][j]);
					if ( gamestatus > 0 ) {
						break;
					}
				}
			}
			if (gamestatus>0) {
				break;
			}
		}
		//check dia
		if ( gamestatus == 0 &&
			 (a[0][0] == 'X' || a[0][0] == 'T') &&
			 (a[1][1] == 'X' || a[1][1] == 'T') &&
			 (a[2][2] == 'X' || a[2][2] == 'T') &&
			 (a[3][3] == 'X' || a[3][3] == 'T') ) {
			 gamestatus = 1;
		} 
		if ( gamestatus == 0 &&
			 (a[0][0] == 'O' || a[0][0] == 'T') &&
			 (a[1][1] == 'O' || a[1][1] == 'T') &&
			 (a[2][2] == 'O' || a[2][2] == 'T') &&
			 (a[3][3] == 'O' || a[3][3] == 'T') ) {
			 gamestatus = 2;
		} 
		if ( gamestatus == 0 &&
			 (a[3][0] == 'X' || a[3][0] == 'T') &&
			 (a[2][1] == 'X' || a[2][1] == 'T') &&
			 (a[1][2] == 'X' || a[1][2] == 'T') &&
			 (a[0][3] == 'X' || a[0][3] == 'T') ) {
			 gamestatus = 1;
		} 
		if ( gamestatus == 0 &&
			 (a[3][0] == 'O' || a[3][0] == 'T') &&
			 (a[2][1] == 'O' || a[2][1] == 'T') &&
			 (a[1][2] == 'O' || a[1][2] == 'T') &&
			 (a[0][3] == 'O' || a[0][3] == 'T') ) {
			 gamestatus = 2;
		} 


		if (gamestatus == 0 && haveempty == 0) {
			fprintf_s(g, "Case #%d: Draw\n", testi+1);
		}
		else if (gamestatus == 1) {
			fprintf_s(g, "Case #%d: X won\n", testi+1);
		}
		else if (gamestatus == 2) {
			fprintf_s(g, "Case #%d: O won\n", testi+1);
		}
		else {
			fprintf_s(g, "Case #%d: Game has not completed\n", testi+1);
		}
	}
	fclose(f);
	fclose(g);
	return 0;
}