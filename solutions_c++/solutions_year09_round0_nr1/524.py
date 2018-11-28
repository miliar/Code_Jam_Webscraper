#include <cstdio>
char word[5005][20], test[20];
	
int main() {
	int i, j, c, l, d, n, k, num, matched, inside;
	
	FILE* in = fopen("alien.in", "r");
	FILE* out = fopen("alien.out", "w");
	fscanf(in, "%d %d %d", &l, &d, &n);
	printf("%d %d %d\n", l, d, n);
	for (i = 0; i < d; i++) fscanf(in, "%s", word[i]);
	for (i = 0; i < n; i++) {
		printf("%d\n", i);
		fscanf(in, "%s", test);
		num = 0;
		for (k = 0; k < d; k++) {
			matched = 0;
			inside = 0;
			c = 0;
			for (j = 0; test[j]; j++) {
				if (test[j] == word[k][c]) matched = 1;
				if (test[j] == '(') inside = 1;
				if (test[j] == ')') inside = 0;
				if (!inside) {
					if (!matched) break;
					else matched = 0;
					c++;
				}
			}
			if (!test[j]) num++;
		}
		fprintf(out, "Case #%d: %d\n", (i+1), num);
	}
	fclose(in);
	fclose(out);
	return 0;
}
	
