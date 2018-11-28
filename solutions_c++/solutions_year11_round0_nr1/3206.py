#include <cstdio>

int abs(int x) {
	if (x < 0) return -x;
	return x;
}

int main() {
	int t;
	scanf("%d", &t);
	for (int tt = 1; tt <= t; ++tt) {
		int n;
		scanf("%d", &n);
		char kto[n];
		int kde[n];
		for (int i = 0; i < n; ++i) {
			kto[i] = getchar();
			while (kto[i] != 'O' && kto[i] != 'B') kto[i] = getchar();
			scanf("%d", &kde[i]);
		}

		int opos = 1, bpos = 1, ofree = 0, bfree = 0;
		int time = 0;

		for (int i = 0; i < n; ++i) {
			if (kto[i] == 'O') {
				int najskor = ofree + abs(opos-kde[i]);
				if (najskor > time) time = najskor;
				++time;
				ofree = time;
				opos = kde[i];
			} else {
				int najskor = bfree + abs(bpos-kde[i]);
				if (najskor > time) time = najskor;
				++time;
				bfree = time;
				bpos = kde[i];
			}
			//printf("%c%d : %d\n", kto[i], kde[i], time);
		}

		printf("Case #%d: %d\n", tt, time);
	}
}
