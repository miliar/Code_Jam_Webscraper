#include <cstdio>

int main() {
	int t;
	scanf("%d", &t);
	for (int tt = 1; tt <= t; ++tt) {
		unsigned long long seats, runs, n;
		unsigned long long g[1042];
		unsigned long long eur[1042];

		scanf("%llu %llu %llu", &runs, &seats, &n);
		for (unsigned long long i = 0; i < n; ++i) {
			scanf("%llu", &g[i]);
			eur[i] = 0;
		}

		unsigned long long front = 0;
		unsigned long long eurCycle = 0;
		unsigned long long cycleLen = 0;

		do {
			unsigned long long full = 0;
			unsigned long long next = front;

			while (full + g[next] <= seats) {
				full += g[next];
				next = (next+1) % n;
				if (next == front) break;
			}

			eur[cycleLen] = full;
			eurCycle += full;
			front = next;
			++cycleLen;

		} while (front != 0);

		unsigned long long res = eurCycle * (runs/cycleLen);
		for (unsigned long long i = 0; i < runs%cycleLen; ++i) {
			res += eur[i];
		}
		printf("Case #%d: %llu\n", tt, res);
	}
}
