#include <cstdio>
#include <cstring>

int main(int argc, char **argv) {
	FILE *in = fopen(argv[1], "r");
	FILE *out = fopen("C-out.out", "w");
	int N;
	char buf[503];
	char *etalon = "welcome to code jam";
	fgets(buf, 503, in);
	sscanf(buf, "%d", &N);
	for (int i = 0; i < N; i++) {
		fgets(buf, 503, in);
		int l = strlen(buf);
		while (buf[l - 1] != ' ' && (buf[l - 1] < 'a' || buf[l - 1] > 'z'))
			l--;
		buf[l] = 0;
		int res = 0;
		if (l >= 19) {
			int tbl[l+1][20];
			for (int j = 0; j < 19; j++)
				tbl[l][j] = 0;
			for (int i = 0; i <= l; i++)
				tbl[i][19] = 1;
			for (int i = l - 1; i >= 0; i--) {
				for (int j = 18; j >= 0; j--) {
					tbl[i][j] = tbl[i + 1][j];
					if (buf[i] == etalon[j])
						tbl[i][j] += tbl[i + 1][j+1];
					tbl[i][j] = tbl[i][j] % 10000;
				}
			}
			res = tbl[0][0];
		}
		fprintf(out, "Case #%d: %d%d%d%d\n", i + 1, res / 1000 % 10, res / 100 % 10, res / 10 % 10, res % 10);
	}
	fclose(out);
	fclose(in);
}
