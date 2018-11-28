#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct {
	int robot;
	int button;
	int urutan;
	int time;
} sData;

int cmp(const void *a, const void *b) {
	if ((*(sData *)a).robot < (*(sData *)b).robot) {
		return -1;
	} else if ((*(sData *)a).robot > (*(sData *)b).robot) {
		return 1;
	} else if ((*(sData *)a).urutan > (*(sData *)b).urutan) {
		return 1;
	} else if ((*(sData *)a).urutan < (*(sData *)b).urutan) {
		return -1;
	} else if ((*(sData *)a).button > (*(sData *)b).button) {
		return 1;
	} else if ((*(sData *)a).button < (*(sData *)b).button) {
		return -1;
	} else return 0;
}

int main() {	
	int T = 0;
	scanf("%d\n",&T);
	sData data[101];
	for (int i=0; i<T; i++) {
		for (int j=0; j<101; j++) {
			data[j].robot = 0;
			data[j].button = 0;
			data[j].urutan = j+1;
			data[j].time = 0;
		}
		int N = 0;
		int posO = -1;
		int posB = -1;
		int limitB=-1;
		scanf("%d",&N);
		for (int j=0; j<N; j++) {
			char temp[2] = " ";
			scanf("%s %d",&temp,&data[j].button);
			if (temp[0] == 'O') {
				data[j].robot = 1;
			} else if (temp[0] == 'B') {
				data[j].robot = 2;
			}
		}
		scanf("\n");
		qsort(data,N,sizeof(sData),cmp);
		int tempO = 1;
		int tempB = 1;
		for (int j=0; j<N; j++) {
			if (data[j].robot == 1 && posO == -1) {
				posO = j;
			}
			else if (data[j].robot == 2 && posB == -1) {
				posB = j;
				limitB = j;
			}
			if (data[j].robot == 1) {
				if (data[j].button >= tempO) {
					data[j].time = (data[j].button-tempO)+1;
					tempO = data[j].button;
				} else {
					data[j].time = (tempO-data[j].button)+1;
					tempO = data[j].button;					
				}
			} else if (data[j].robot == 2) {
				if (data[j].button >= tempB) {
					data[j].time = (data[j].button-tempB)+1;
					tempB = data[j].button;
				} else {
					data[j].time = (tempB-data[j].button)+1;
					tempB = data[j].button;					
				}
			}
		}
		bool keluar=false;
		int time=0;
		int buttonO = 0;
		int buttonB = 0;
		int posUrutan=1;
		if (limitB == -1) {
			limitB = N;
		}
		while (!keluar) {
			if ((posO == limitB || posO == -1) && (posB == N || posB == -1)) {
				keluar=true;
			} else {
				if (posO == -1 || posO == limitB) {
					if (data[posB].time-buttonB > 0) {
						time += data[posB].time-buttonB;
						buttonB = 0;
						posB++;				
					} else {
						time++;
						buttonB = 0;
						posB++;
					}
				} else if (posB == -1 || posB == N) {
					if (data[posO].time-buttonO > 0) {
						time += data[posO].time-buttonO;
						buttonO = 0;
						posO++;
					} else {
						time++;
						buttonO = 0;
						posO++;
					}
				} else {
					if (posUrutan == data[posO].urutan) {
						if (data[posO].time-buttonO > 0) {
							time += data[posO].time-buttonO;
							buttonB += data[posO].time-buttonO;
							buttonO = 0;
							posO++;
							posUrutan++;
						} else {
							time += 1;
							buttonB += 1;
							buttonO = 0;
							posO++;
							posUrutan++;
						}
					} else if (posUrutan == data[posB].urutan) {
						if (data[posB].time-buttonB > 0) {
							time += data[posB].time-buttonB;
							buttonO += data[posB].time-buttonB;
							buttonB = 0;
							posB++;
							posUrutan++;
						} else {
							time += 1;
							buttonO += 1;
							buttonB = 0;
							posB++;
							posUrutan++;
						}
					}
				}
			}
		}
		printf("Case #%d: %d\n",i+1,time);
	}
	//while (scanf("%d %d %d\n",&d1,&d2,&d3) != EOF) {
		//jawaban
		//printf("Case #%d: %d\n",d1,d2);
	//}
	//getch(); 
	return 0;
}