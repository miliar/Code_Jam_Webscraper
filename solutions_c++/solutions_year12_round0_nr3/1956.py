#include <cstring>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cmath>

bool visit[2000001];

int main() {
	FILE *fin = fopen("C-large.in", "r");
	FILE *fout = fopen("out.txt", "w");
	int t, a, b;
	//long long sum;
	__int64 sum;
	fscanf(fin, "%d", &t);
	for (int i = 1; i <= t; ++i) {
		fprintf(fout, "Case #%d: ", i);
		fscanf(fin, "%d%d", &a, &b);
		for (int j = a; j <= b; ++j) visit[j] = false;
		sum = 0;
		int rank = 1, ndig = 1;
		for (int j = a; j <= b; ++j) {
			if (visit[j]) continue;
			while (rank * 10 <= j) {
				rank *= 10;
				++ndig;
			}
			__int64 num = 1;
			int newnum = j;
			visit[j] = true;
			for (int k = 1; k < ndig; ++k) {
				int tmp = newnum % 10;
				newnum = newnum / 10 + tmp * rank;
				if (tmp == 0 || newnum > b || newnum < a || visit[newnum]) continue;
				visit[newnum] = true;
				++num;
			}
			sum += ((num * (num - 1)) >> 1);
		}
		fprintf(fout, "%lld\n", sum);
	}
	fclose(fout);
	fclose(fin);
	return 0;
}
