#include <stdio.h>
#include <vector>

using namespace std;

char *s = "welcome to code jam";
char t[600];
long long a[600][600];
long long b[600];

int main() {
	int N;
	scanf("%d\n", &N);
	for (int n = 0; n < N; n++) {
		gets(t);
		int tlen = 0;
		while (t[tlen] != 0 && t[tlen] != '\r' && t[tlen] != '\n') tlen++;
		t[tlen] = 0;
		int slen = strlen(s);
		for (int i = 0; i <= slen; i++) {
			a[i][0] = 0;
		}
		for (int i = 0; i <= tlen; i++) {
			a[0][i] = 1;
		}
		for (int r = 1; r <= slen; r++) {
			b[0] = 0;
			int last = 0;
			for (int c = 1; c <= tlen; c++) {
				if (s[r - 1] == t[c - 1]) {// && a[r-1][c] > 0) {
					a[r][c] = (a[r-1][c] + a[r][c-1]) % 10000;//a[r-1][c] + (b[c-1] + 1) * a[r-1][last];//((b[c-1] + 1) * a[r-1][c]);
					b[c] = b[c-1] + 1;
					last = c;
				} else {
					a[r][c] = a[r][c-1];
					b[c] = b[c-1];
				}
			}
		}
		/*for (int r = 0; r <= slen; r++) {
			for (int c = 0; c <= tlen; c++) {
				fprintf(stderr, "%d ", a[r][c]);
			}
			fprintf(stderr, "\n");
		}*/
		int ans = a[slen][tlen];
		printf("Case #%d: ", n+1);
		if (ans < 1000) printf("0");
		if (ans < 100) printf("0");
		if (ans < 10) printf("0");
		printf("%d\n", ans);
	}
	return 0;
}