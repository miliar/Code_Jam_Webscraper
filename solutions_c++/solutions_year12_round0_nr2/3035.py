#include <stdio.h>
#include <string.h>
#include <string>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <iostream>
#include <math.h>
using namespace std;

typedef struct {
	int score;
	int minAngka;
	int sisa;
	int maxAngka;
} sData;

int cmp(const void *a, const void *b) {
	if ((*(sData *)a).minAngka < (*(sData *)b).minAngka) {
		return 1;
	} else if ((*(sData *)a).minAngka > (*(sData *)b).minAngka) {
		return -1;
	} else if ((*(sData *)a).sisa < (*(sData *)b).sisa) {
		return 1;
	} else if ((*(sData *)a).sisa > (*(sData *)b).sisa) {
		return -1;
	} else return 0;
}


int main() {	
	int T = 0;
	scanf("%d\n",&T);
	for (int i=0; i<T; i++) {
		int N = 0;
		int S = 0;
		int P = 0;
		sData peserta[110];

		scanf("%d",&N);
		scanf("%d",&S);
		scanf("%d",&P);

		for (int j=0; j<N; j++) {
			if (j < N-1) {
				scanf("%d",&peserta[j].score);
			} else {
				scanf("%d\n",&peserta[j].score);
			}			
			peserta[j].maxAngka = 0;
			peserta[j].minAngka = floorl(peserta[j].score/3);
			peserta[j].sisa = peserta[j].score % 3;
			/*if (peserta[j].sisa == 0) {
				peserta[j].sisa = 3;
			}*/
		}

		qsort(peserta,N,sizeof(sData),cmp);

		int jumOverP = 0;

		for (int j=0; j<N; j++) {
			/*if (peserta[j].sisa == 3) {
				peserta[j].sisa = 0;
			}*/
			if (peserta[j].minAngka >= P) {
					if (peserta[j].sisa > 0) {
						peserta[j].maxAngka = peserta[j].minAngka + 1;
					} else {
						peserta[j].maxAngka = peserta[j].minAngka;
					}
			} else {
				if (peserta[j].sisa == 1) {
					peserta[j].maxAngka = peserta[j].minAngka + 1;
				} else {
					if (S > 0) {
						if (peserta[j].sisa == 0) {
							if (peserta[j].score == 0) {
								peserta[j].maxAngka = peserta[j].minAngka;
							} else {
								if (peserta[j].minAngka < 10) {
									peserta[j].maxAngka = peserta[j].minAngka + 1;
									S -= 1;
								} else {
									peserta[j].maxAngka = peserta[j].minAngka;
								}
							}
						} else {
							if (peserta[j].minAngka + 1 >= P) {
								peserta[j].maxAngka = peserta[j].minAngka + 1;
							} else {
								if (peserta[j].minAngka + 2 <= 10) {
									peserta[j].maxAngka = peserta[j].minAngka + 2;
									S -= 1;
								} else {
									peserta[j].maxAngka = peserta[j].minAngka + 1;
								}
							}
						}
					} else {
						if (peserta[j].sisa > 0) {
							peserta[j].maxAngka = peserta[j].minAngka + 1;
						} else {
							peserta[j].maxAngka = peserta[j].minAngka;
						}
					}
				}
			}
			if (peserta[j].maxAngka >= P) {
				jumOverP++;
			}
		}

		printf("Case #%d: %d",i+1,jumOverP);
		//cout << strR;
		printf("\n");
	}
	//while (scanf("%d %d %d\n",&d1,&d2,&d3) != EOF) {
		//jawaban
		//printf("Case #%d: %d\n",d1,d2);
	//}
	//getch(); 
	return 0;
}