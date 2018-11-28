#include <cstdio>
#include <cstring>
int main() {
	int i, j, num[50], pos[50], ans, n, t, T;
	bool taken[50];
	char c;

	FILE* in = fopen("rows.in", "r");
	FILE* out = fopen("rows.out", "w");
	fscanf(in, "%d", &T);
	for (t = 0; t < T; t++) {
		fscanf(in, "%d\n", &n);
		ans = 0;
		for (i = 0; i < n; i++) {
			num[i] = -1;
			for (j = 0; j < n; j++) {
				fscanf(in, "%c\n", &c);
				if (c == '1') num[i] = j;
			}
		}
		memset(taken, 0, sizeof(taken));
		for (i = 0; i < n; i++) {
			for (j = num[i]; j < n; j++) {
				if (!taken[j]) {
					taken[j] = true;
					pos[i] = j;
					break;
				}
			}
		}
					
		for (i = 0; i < n; i++) {
			for (j = n-1; j > 0; j--) {
				if (pos[j] == i && pos[j] < j) {
					ans++;
					pos[j] ^= pos[j-1];
					pos[j-1] ^= pos[j];
					pos[j] ^= pos[j-1];
				}
			}
		}
		fprintf(out, "Case #%d: %d\n", t+1, ans);
	}
	fclose(in);
	fclose(out);
	return 0;
}
