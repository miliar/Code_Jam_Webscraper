#include <stdio.h>

#define MAX_CHICKS 50

int num, target, barn, time;

typedef struct {
	int startloc;
	int speed;
	int can_reach;
	int loc;
} Chick;

Chick chicks[MAX_CHICKS];

int max_in_barn() {
	int result = 0;
	for (int n = 0; n < num; n++) {
		if (time * chicks[n].speed >= barn - chicks[n].startloc) {
			chicks[n].can_reach = (barn - chicks[n].startloc - 1) / chicks[n].speed + 1;
			result++;
		} else {
			chicks[n].can_reach = 0;
		}
	}
	return result;
}

int solve(int max) {
	int swaps = 0;
	int to_pass = 0;
	int passedChicks[MAX_CHICKS];
	int ok = 0;
	for (int n = num - 1; n >= 0; n--) {
		// Check if front chick reaches the barn
		if (chicks[n].can_reach) {
			swaps += to_pass;
			ok++;
			if (ok == target) break;
		} else {
			// Front chick cannot reach the barn... those behind have to pass
			passedChicks[to_pass++] = n;
		}
	}
	return swaps;
}

int main() {
	int cases;
	scanf("%d", &cases);
	
	for (int i = 1; i <= cases; i++) {
		scanf("%d %d %d %d", &num, &target, &barn, &time);
		for (int n = 0; n < num; n++) {
			scanf("%d", &chicks[n].startloc);
		}
		for (int n = 0; n < num; n++) {
			scanf("%d", &chicks[n].speed);
		}
		int max = max_in_barn();
		if (max < target) {
			printf("Case #%d: IMPOSSIBLE\n", i);
		} else {
			int result = solve(max);
			printf("Case #%d: %d\n", i, result);
		}
	}
	return 0;
}
