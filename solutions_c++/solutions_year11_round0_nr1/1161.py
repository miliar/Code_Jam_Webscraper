#include <cstdio>
#include <algorithm>

int main () {
	int T, N, P;
	char bot, current_bot;
	int orange_p, blue_p, result, acc, diff;

	scanf("%i", &T);
	for (int t = 1; t <= T; ++t) {
		scanf("%i ", &N);
		orange_p = blue_p = 1;
		result = 0;
		current_bot = 0;
		acc = 0;
		for (int n = 0; n < N; ++n) {
			scanf("%c %i ", &bot, &P);
			if (bot == 'O') {
				diff = abs(orange_p - P);
			} else {
				diff = abs(blue_p - P);
			}
			if (bot != current_bot) {
				result += std::max(diff - acc, 0) + 1;
				acc = std::max(diff - acc, 0) + 1;
				current_bot = bot;
			} else {
				acc += diff + 1;
				result += diff + 1;
			}
			if (current_bot == 'O') {
				orange_p = P;
			} else {
				blue_p = P;
			}
		}
		printf("Case #%i: %i\n", t, result);
	}
}

