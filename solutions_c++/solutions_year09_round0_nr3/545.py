#include <cstdio>
#include <cstring>
#include <cstdlib>
int num[505][505];

int main() {
	int n, i, j, t;
	char str[505], target[] = "welcome to code jam";
	
	FILE* in = fopen("welcome.in", "r");
	FILE* out = fopen("welcome.out", "w");
	
	fscanf(in, "%d\n", &n);
	for (t = 0; t < n; t++) {
		fgets(str, 505, in);
		memset(num, 0, sizeof(num));
		num[0][0] = (str[0] == target[0]);
		for (i = 1; str[i]; i++) {
			for (j = 0; j < 19; j++) {
				num[i][j] = num[i-1][j];
				if (str[i] == target[j]) num[i][j] = (num[i][j] + (j ? num[i-1][j-1] : 1)) % 10000;
			}
		}
		fprintf(out, "Case #%d: %.4d\n", (t+1), num[i-1][18]);
	}
	fclose(in);
	fclose(out);
	return 0;
}

				
