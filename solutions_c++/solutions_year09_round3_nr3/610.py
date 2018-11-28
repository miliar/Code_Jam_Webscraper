#include <stdio.h>
#include <stdlib.h>

int P, Q;
int releases[200];
int cells[11000];
int min;

void printP(int tot) {
	return;
	for(int i = 0; i < P; i++) {
		printf("%d", cells[i]);
	}
	printf(" T:%d\n", tot);
}

void calc(int tot) {
	int end = 1;
	printP(tot);
	for(int i = 0; i < Q; i++) {
		if(cells[releases[i]]) {
			end = 0;
			cells[releases[i]] = 0;
			int oldTot = tot;
			for(int j = releases[i] - 1; j >=0; j--) {
				if(cells[j]) tot++;
				else break;
			}
			for(int j = releases[i] + 1; j < P; j++) {
				if(cells[j]) tot++;
				else break;
			}
			if(tot < min)
				calc(tot);
			tot = oldTot;
			cells[releases[i]] = 1;
		}
	}
	if(end) {
		if(tot < min) min = tot;
	}
}

int main() {
	int N;
	scanf("%d", &N);
	for(int n = 1; n <= N; n++) {
		min = 2000000;
		
		scanf("%d %d", &P, &Q);
		for(int i = 0; i < Q; i++) {
			scanf("%d", &releases[i]);
			releases[i]--;
		}
		for(int i = 0; i < 11000; cells[i++] = 1);
		calc(0);
	
		printf("Case #%d: %d\n", n, min);
	}
	return 0;
}
