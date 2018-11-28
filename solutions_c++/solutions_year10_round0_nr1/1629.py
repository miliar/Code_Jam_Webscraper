#include <cstdio>
FILE *in, *out;
int T, N, K;

int main() {
	in = fopen("A-small.in", "r"); out = fopen("dashboard.out", "w");
	fscanf(in, "%d", &T);
	for (int i = 1; i <= T; ++i) {
		fscanf(in, "%d %d", &N, &K);
		fprintf(out, "Case #%d: %s\n", i, (K+1)%(1<<N) ? "OFF" : "ON");
	}
}
