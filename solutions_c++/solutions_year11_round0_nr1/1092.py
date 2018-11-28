#include <cstdio>

#define BLUE 0
#define ORANGE 1

int RDES[2];
int rdes[2][1000];
int rdesi[2];
int loc[2];

int DES;
int des[1000];
int color[1000];

void moverobot(int r) {
	if(rdesi[r] != RDES[r] && loc[r] != rdes[r][rdesi[r]]) {
		if(loc[r] < rdes[r][rdesi[r]]) {
			loc[r]++;
		} else {
			loc[r]--;
		}
	}
}

int main() {
	int T;
	scanf("%d", &T);
	for(int t = 1; t<=T; t++) {
		scanf("%d", &DES);
		RDES[0] = RDES[1] = 0;
		for(int i = 0; i<DES; i++) {
			char col;
			int loc;
			scanf(" %c %d", &col, &loc);
			des[i] = loc;
			color[i] = col == 'O' ? ORANGE : BLUE;
			rdes[color[i]][RDES[color[i]]++] = loc;
		}
		rdesi[0] = rdesi[1] = 0;
		loc[0] = loc[1] = 1;
		int time = 0;
		for(int i = 0; i<DES; i++) {
			while(loc[color[i]] != des[i]) {
				for(int j = 0; j<2; j++) {
					moverobot(j);
				}
				time++;
			}
			rdesi[color[i]]++;
			moverobot(1-color[i]);
			time++;
		}
		printf("Case #%d: %d\n", t, time);
	}
	return 0;
}
