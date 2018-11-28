#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

int i,j,k,n;
int cnt[10];
char s[100], r[100], p[100];

int main() {
	int test, ntest;
	scanf("%d", &ntest);
	for (test = 1; test <= ntest; test++) {
		printf("Case #%d: ", test);
		scanf("%s", s);
		for (i = 0; i < 10; i++) cnt[i] = 0;
		for (i = 0; i < strlen(s); i++) {
			cnt[s[i]-'0']++;
		}
		// najvacsie cislo
		r[strlen(s)] = '\0';
		k = 0;
		for (i = 9; i >= 0; i--) {
			for (j = 0; j < cnt[i]; j++) r[k++] = i + '0';
		}
		if (strcmp(r, s) == 0) { // staci pridat nulu
			r[strlen(s)+1] = '\0';
			r[1] = '0';
			for (i = 1; i <= 9; i++) if (cnt[i] > 0) break;
			cnt[i]--;
			r[0] = i + '0';
			k = 2;
			for (i = 0; i <= 9; i++) {
				for (j = 0; j < cnt[i]; j++) r[k++] = i + '0';
			}
		} else { // treba permutovat
//			for (k = 0; k < strlen(s); k++) r[k] = s[k];
			r[0] = '9' + 1; r[1] = '\0';
			p[strlen(s)] = '\0';
			for (k = 0; k < strlen(s); k++) {
				for (i = 0; i < k; i++) p[i] = s[i];
				for (i = 0; i < 10; i++) cnt[i] = 0;
				for (i = k; i < strlen(s); i++) cnt[s[i]-'0']++;

				for (i = s[k] - '0' + 1; i <= 9; i++) {
					if (cnt[i] > 0) break;
				}
				if (i > 9) continue;
				p[k] = i + '0'; cnt[i]--;
				n = k + 1;
				for (i = 0; i <= 9; i++) {
					for (j = 0; j < cnt[i]; j++) p[n++] = i + '0';
				}
				if (strcmp(p, s) > 0 && strcmp(r, p) > 0) {
					strcpy(r, p);
				}
			}
		}
		printf("%s\n", r);
	}
	return 0;
}
