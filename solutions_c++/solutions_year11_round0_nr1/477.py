#include <cstdio>
#include <algorithm>

FILE *in, *out;
const int MAX_N = 105;
int T, N, orders[MAX_N], ordersO[MAX_N], ordersB[MAX_N];

//O is true
int solve() {
	int B = 0, O = 0;
	int or = 1, bl = 1;
	int time = 0;
	for (int i = 0; i < N; ++i) {
		int maxdist = (orders[i] ? std::abs(or-ordersO[O]) : std::abs(bl-ordersB[B])) + 1;
		int distO = std::min(maxdist, std::abs(or-ordersO[O])), dirO = ordersO[O] < or ? -1 : 1;
		int distB = std::min(maxdist, std::abs(bl-ordersB[B])), dirB = ordersB[B] < bl ? -1 : 1;
		time += maxdist;
		or += dirO*distO;
		bl += dirB*distB;
		if (orders[i]) O++;
		else B++;
	}
	return time;
}

int main() {
	in = fopen("botin.txt", "r"); out = fopen("botout.txt", "w");
	fscanf(in, "%d", &T);
	for (int i = 1; i <= T; ++i) {
		fscanf(in, "%d", &N);
		int B = 0, O = 0;
		char ch;
		int b;
		for (int j = 0; j < N; ++j) {
			fscanf(in, " %c %d ", &ch, &b);
			orders[j] = (ch == 'O');
			if (ch == 'O') ordersO[O++] = b;
			else ordersB[B++] = b;
		}
		fprintf(out, "Case #%d: %d\n", i, solve());
	}
}