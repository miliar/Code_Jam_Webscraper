
#include <cmath>
#include <cstdio>
#include <cstdlib>

int t, n;

int main() {
	FILE * fin = fopen("bot_trust.in", "r");
	FILE * fout = fopen("bot_trust.out", "w");
	int i, j, time, pos, bot, bp[2], bt[2];
	char c;
	fscanf(fin, "%d", &t);
	for (i = 0; i < t; ++i) {
		time = 0;
		bp[0] = 1;
		bp[1] = 1;
		bt[0] = 0;
		bt[1] = 0;
		fscanf(fin, "%d", &n);
		for (j = 0; j < n; ++j) {
			fscanf(fin, " %c %d", &c, &pos);
			switch (c) {
			case 'O':
				bot = 0;
				break;
			case 'B':
				bot = 1;
				break;
			default:
				exit(1);
				break;
			}
			if (time < bt[bot] + abs(pos - bp[bot])) {
				time = bt[bot] + abs(pos - bp[bot]);
			}
			++time;
			bp[bot] = pos;
			bt[bot] = time;
		}
		fprintf(fout, "Case #%d: %d\n", i + 1, time);
	}
	fclose(fout);
	fclose(fin);
	return 0;
}
