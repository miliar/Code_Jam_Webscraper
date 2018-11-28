#include <cstdio>
#include <cmath>

int abs(int v) {
	return v < 0 ? -v : v;
}

void test() {
	int n,  time = 0, move;
	int pos[2] = {1,1};
	int tim[2] = {0,0};
	char color;
	scanf("%d ", &n);
	while (n--) {
		scanf(" %c %d ", &color, &move);
		//printf("%c %d\n", color, move);
		int diff = abs(pos[color=='B'] - move) - time + tim[color=='B'];
		//printf("Diff %d\n", diff);
		if (diff > 0) time += diff;
		time++;
		pos[color=='B'] = move;
		tim[color=='B'] = time;
		//printf("Time %d\n", time);
	}
	printf("%d\n", time);
}

main() {
	int z;
	scanf("%d", &z);
	for (int c = 0; c<z;c++) {
		printf("Case #%d: ", c+1);
		test();
	}
}

