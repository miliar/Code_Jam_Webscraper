#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <iostream>

int main() {	
	int T = 0;
	scanf("%d\n",&T);
	for (int i=0; i<T; i++) {
		int N = 0;
		scanf("%d\n",&N);
		char data[101][101];
		long double WP[101];
		long double OWP[101];
		long double OOWP[101];
		long double RPI[101];
		for (int j=0; j<101; j++) {
			strcpy(data[j],"");
			WP[j] = 0;
			OWP[j] = 0;
			OOWP[j] = 0;
			RPI[j] = 0;
		}
		for (int j=0; j<N; j++) {
			scanf("%s\n",&data[j]);
		}
		for (int j=0; j<N; j++) {
			int jumWin = 0;
			int jumLose = 0;
			for (int k=0; k<N; k++) {
				if (data[j][k] == '1') {
					jumWin++;
				} else if (data[j][k] == '0') {
					jumLose++;
				}
			}
			if (jumWin + jumLose == 0) {
				WP[j] = 0;
			} else {
				WP[j] = jumWin*1.0 / ((jumWin+jumLose)*1.0);
			}
		}
		for (int j=0; j<N; j++) {
			double tempWPT = 0;
			int count = 0;
			for (int k=0; k<N; k++) {
				if (j != k && data[k][j] != '.') {
					count++;
					int jumWinT = 0;
					int jumLoseT = 0;
					for (int l=0; l<N; l++) {
						if (j != l) {
							if (data[k][l] == '1') {
								jumWinT++;
							} else if (data[k][l] == '0') {
								jumLoseT++;
							}
						}
					}
					if (jumWinT+jumLoseT == 0) {
						tempWPT = tempWPT;
					} else {
						tempWPT += (jumWinT*1.0/((jumWinT+jumLoseT)*1.0));
					}
				}
			}
			if (count == 0) {
				OWP[j] = 0;
			} else {
				OWP[j] = tempWPT / (count*1.0);
			}
		}
		printf("Case #%d:\n",i+1);
		for (int j=0; j<N; j++) {
			double tempOOW = 0;
			int count = 0;
			for (int k=0; k<N; k++) {
				if (data[j][k] != '.') {
					tempOOW += OWP[k];
					count++;
				}
			}
			if (count == 0) {
				OOWP[j] = 0;
			} else {
				OOWP[j] = tempOOW / (count*1.0);
			}
			RPI[j] = 0.25 * WP[j] + 0.50 * OWP[j] + 0.25 * OOWP[j];
			//printf("%f\n",RPI[j]);
			std::cout << RPI[j] << '\n';
		}
	}
	//while (scanf("%d %d %d\n",&d1,&d2,&d3) != EOF) {
		//jawaban
		//printf("Case #%d: %d\n",d1,d2);
	//}
	//getch(); 
	//MyBig temp = 9999999999;
	//std::cout << temp;
	return 0;
}