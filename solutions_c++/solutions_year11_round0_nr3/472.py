#include <cstdio>

FILE *in, *out;
const int MAX_N = 1005;
int cumxa[MAX_N], cumsa[MAX_N], T, N;
//Inclusive
int cumx(int st, int en) {
	if (en < st)
		return cumx(st, N-1)^cumx(0, en);
	return cumxa[en]^(st == 0 ? 0 : cumxa[st-1]);
}

int cums(int st, int en) {
	if (en < st)
		return cums(st, N-1) + cums(0, en);
	return cumsa[en]-(st == 0 ? 0 : cumsa[st-1]);
}

int main() {
	in = fopen("candyin.txt", "r"); out = fopen("candyout.txt", "w");
	fscanf(in, "%d", &T);
	for (int t = 1; t <= T; ++t) {
		fscanf(in, "%d", &N);
		int c;
		for (int i = 0; i < N; ++i) {
			fscanf(in, "%d", &c);
			cumsa[i] = (i == 0 ? 0 : cumsa[i-1]) + c;
			cumxa[i] = (i == 0 ? 0 : cumxa[i-1])^c;
		}
		
		int max = -1;
		for (int sz = 1; sz < N; ++sz) {
			for (int i = 0; i < N; ++i) {
				int cx = cumx(i, (i+sz-1)%N), cs = cumsa[N-1]-cums(i, (i+sz-1)%N);
				if (cx == (cumxa[N-1]^cx))
					if (cs > max)
						max = cs;
			}
		}
		fprintf(out, "Case #%d:", t);
		if (max == -1) fprintf(out, " NO\n");
		else fprintf(out, " %d\n", max);
	}
}