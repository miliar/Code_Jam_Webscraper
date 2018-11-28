#include <stdio.h>

int T;
int i, j, k, l;
char a[4][4];
char c;

void process(){
	int cas;
	int cnum=0;
	int cnum2=0;
	int cnum3=0;

	FILE *fip, *fop;
	fip = fopen("input.txt", "r");
	fop = fopen("output.txt", "w");

	fscanf(fip, "%d", &T);

	for (k=0; k<T; k++){
		cas = 0;

		for (i=0; i<4; i++){
				fscanf(fip, "%s", &a[i]);
		}
		
		c= 'X';

		for (l=0; l<2; l++){
			cnum = 0;
			for (i=0; i<4; i++){
				if (a[i][0] == c){
					cnum = 0;
					for (j=0; j<4; j++){
						if ((a[i][j] == c) || (a[i][j] == 'T')) cnum++;
					}

					if (cnum == 4){
						if(l==0) cas = 1;
						if(l==1) cas = 2;
					}
				}

				if (a[0][i] == c){
					cnum = 0;
					for (j=0; j<4; j++){
						if ((a[j][i] == c) || (a[j][i] == 'T')) cnum++;
					}

					if (cnum == 4){
						if(l==0) cas = 1;
						if(l==1) cas = 2;
					}
				}
				
				cnum = 0;
				for (j=0; j<4; j++){
					if ((a[j][j] == c) || (a[j][j] == 'T')) cnum++;
				}
				if (cnum == 4){
					if(l==0) cas = 1;
					if(l==1) cas = 2;
				}

				cnum = 0;
				for (j=0; j<4; j++){
					if ((a[4-j-1][j] == c) || (a[4-j-1][j] == 'T')) cnum++;
				}
				if (cnum == 4){
					if(l==0) cas = 1;
					if(l==1) cas = 2;
				}

			}
			c = 'O';
		}



		if (cas == 1) fprintf(fop, "Case #%d: X won\n", k+1);
		else if (cas == 2) fprintf(fop, "Case #%d: O won\n", k+1);
		else if (cas == 0){
			for (i=0; i<4; i++){
				for (j=0; j<4; j++){
					if (a[i][j] == '.'){
						cas = 3;
					}
				}
			}
			if (cas == 3) fprintf(fop, "Case #%d: Game has not completed\n", k+1);
			else fprintf(fop, "Case #%d: Draw\n", k+1);
		}
	}
}

int main(){
	process();
	return 0;
}



