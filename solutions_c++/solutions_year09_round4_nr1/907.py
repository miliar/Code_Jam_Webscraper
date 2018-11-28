#include <stdio.h>
#include <string.h>
#include <string>
#include <set>
using namespace std;

int i,j,k,n;
char t[50][50];
int cnt;

int main() {
	int test, ntest;
	scanf("%d", &ntest);
	for (test = 1; test <= ntest; test++) {
		printf("Case #%d: ", test);
		scanf("%d", &n);
		for (i = 0; i < n; i++) {
			getchar();
			for (j = 0; j < n; j++) {
				t[i][j] = getchar();
			}
		}
		cnt = 0;
		for (k = 0; k < n; k++) {
			for (i = k; i < n; i++) {
				for (j = k + 1; j < n; j++) {
					if (t[i][j] == '1') break;
				}
				if (j == n) break;
			}
			// i-ty ideme presunut na k-te miesto
			for (; i > k; i--) {
				for (j = 0; j < n; j++) {
					swap(t[i][j], t[i-1][j]);
				}
				cnt++;
			}
		}
		printf("%d\n", cnt);
	}
	return 0;
}
