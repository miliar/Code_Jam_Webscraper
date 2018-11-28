#include <cstdio>

int main() {
	int i, j, n, val[256], num;
	long long total, b;
	char s[100];
	
	FILE* in = fopen("base.in", "r");
	FILE* out = fopen("base.out", "w");
	fscanf(in, "%d", &n);
	for (i = 0; i < n; i++) {
		fscanf(in, "%s", s);
		for (j = 0; j < 255; j++) val[j] = -1;
		val[s[0]] = 1;
		num = 1;
		for (j = 0; s[j]; j++) {
			if (val[s[j]] < 0) {
				val[s[j]] = num++;
				if (val[s[j]] == 1) val[s[j]] = 0;
			}
		}
		if (num == 1) num = 2;
		for (total = 0, b = 1, j--; j >= 0; j--, b *= (long long)num) {
			total += b * (long long)val[s[j]];
		}
		fprintf(out, "Case #%d: %lld\n", (i+1), total);
	}
	fclose(in);
	fclose(out);
	return 0;
}

