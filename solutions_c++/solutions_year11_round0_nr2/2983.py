#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {	
	int T = 0;
	scanf("%d\n",&T);
	for (int i=0; i<T; i++) {
		int C = 0;
		scanf("%d",&C);

		char strC[38][4];
		for (int j=0; j<38; j++) {
			strcpy(strC[j],"");
		}
		for (int j=0; j<C; j++) {
			scanf("%s",strC[j]);
		}

		int D = 0;
		scanf("%d",&D);

		char strD[30][3];
		for (int j=0; j<30; j++) {
			strcpy(strD[j],"");
		}
		for (int j=0; j<D; j++) {
			scanf("%s",strD[j]);
		}

		int N = 0;
		scanf("%d",&N);

		char strN[103];
		strcpy(strN,"");

		scanf("%s\n",&strN);

		char hasil[103];
		strcpy(hasil,"");
		int posHasil = 0;

		for (int j=0; j<N; j++) {
			if (j==0) {
				hasil[posHasil] = strN[j];
				posHasil++;
			} else {
				char temp[2];
				bool tempB = false;
				strcpy(temp,"");
				for (int k=0; k<C;k++) {
					if (!tempB) {
						if (hasil[posHasil-1] == strC[k][0]) {
							if (strN[j] == strC[k][1]) {
								temp[0] = strC[k][2];
								tempB = true;
							}
						} else if (hasil[posHasil-1] == strC[k][1]) {
							if (strN[j] == strC[k][0]) {
								temp[0] = strC[k][2];
								tempB = true;
							}
						}
					}
				}
				if (tempB) {
					hasil[posHasil-1] = temp[0];
				} else {
					strcpy(temp,"");
					tempB = false;
					for (int k=0; k<D; k++) {
						if (!tempB) {
							if (strN[j] == strD[k][0]) {
								temp[0] = strD[k][1];
								tempB = true;
							} else if (strN[j] == strD[k][1]) {
								temp[0] = strD[k][0];
								tempB = true;
							}
						}
					}
					if (tempB) {
						tempB = false;
						for (int k=0; k<posHasil; k++) {
							if (hasil[k] == temp[0]) {
								tempB = true;
							}
						}
						if (tempB) {
							strcpy(hasil,"");
							posHasil = 0;
						} else {
							hasil[posHasil] = strN[j];
							posHasil++;
						}
					} else {
						hasil[posHasil] = strN[j];
						posHasil++;
					}
				}
			}
		}
		char tempH[5];	
		printf("Case #%d: [",i+1);
		for (int j=0; j<posHasil; j++){
			strcpy(tempH,"");
			if (j==0) {
				tempH[0] = hasil[j];
				tempH[1] = '\0';
				printf("%s",tempH);
			} else {
				tempH[0] = ',';
				tempH[1] = ' ';
				tempH[2] = hasil[j];
				tempH[3] = '\0';
				printf("%s",tempH);
			}
		}
		printf("]\n");
	}
	//while (scanf("%d %d %d\n",&d1,&d2,&d3) != EOF) {
		//jawaban
		//printf("Case #%d: %d\n",d1,d2);
	//}
	//getch(); 
	return 0;
}