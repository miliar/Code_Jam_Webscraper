#include <stdio.h>

#define MAX_ROUNDS 11
#define MAX_TEAMS 1024

#define NO_GAME -1

int cost[MAX_ROUNDS][MAX_TEAMS];
int teams[MAX_TEAMS];
int missed[MAX_ROUNDS][MAX_TEAMS];
int num_rounds;
int num_teams;

#define min(a,b) ((a) < (b) ? (a) : (b))

int calc(int depth, int match, int num_missed) {
	if (num_missed > missed[depth][match]) {
		//printf("Match (%d %d %d) ", depth, match, num_missed);
		//printf("num missed > %d\n", missed[depth][match]);
		return NO_GAME;
	}
	if (depth >= num_rounds) {
		return 0;
	}
	int one;
	{
		int total = cost[depth][match];
		int p1 = calc(depth + 1, match * 2, num_missed);
		int p2 = calc(depth + 1, match * 2 + 1, num_missed);
		if (p1 == NO_GAME || p2 == NO_GAME) {
			one = NO_GAME;
		} else {
			one = total + p1 + p2;
		}
	}
	int two;
	{
		int p1 = calc(depth + 1, match * 2, num_missed + 1);
		int p2 = calc(depth + 1, match * 2 + 1, num_missed + 1);
		if (p1 == NO_GAME || p2 == NO_GAME) {
			two = NO_GAME;
		} else {
			two = p1 + p2;
		}
	}
	//printf("Match (%d %d %d) ", depth, match, num_missed);
	//printf("cost = %d or %d\n", one, two);
	if (one == NO_GAME) {
		return two;
	}
	if (two == NO_GAME) {
		return one;
	}
	return (one < two) ? one : two;
}

int getCost() {
	
	// Calculate missed matrix
	int max = num_teams / 2;
	for (int r = num_rounds - 1; r >= 0; r--, max /= 2) {
		for (int m = 0; m < max; m++) {
			missed[r][m] = min(missed[r+1][2*m], missed[r+1][2*m+1]);
			//printf("%d ", missed[r][m]);
		}
		//printf("\n");
	}
	
	return calc(0, 0, 0);
}

int main() {
	int cases;
	scanf("%d", &cases);
	
	for (int i = 1; i <= cases; i++) {
		scanf("%d", &num_rounds);
		num_teams = 1 << num_rounds;
		for (int n = 0; n < num_teams; n++) {
			scanf("%d", &missed[num_rounds][n]);
			//printf("%d ", missed[num_rounds][n]);
		}
		//printf("\n");
		
		int matches = num_teams;
		for (int n = num_rounds - 1; n >= 0; n--) {
			matches = matches / 2;
			for (int m = 0; m < matches; m++) {
				scanf("%d", &cost[n][m]);
				//printf("%d ", cost[n][m]);
			}
			//printf("\n");
		}
		
		int cost = getCost();
		printf("Case #%d: %d\n", i, cost);
	}
	return 0;
}
