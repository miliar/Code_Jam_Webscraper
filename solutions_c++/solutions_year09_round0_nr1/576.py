#include<stdio.h>
#include <stdlib.h>

char dict[5000][16];
char patt[100000];

bool match(char *patt, char *str) {
	int p1 = 0, p2 = 0;
	while (patt[p1] && patt[p2]) {
		if (patt[p1] == '(') {
			while (patt[p1] != ')') {
				if (patt[p1] == str[p2]) {
					break;
				}
				else p1++;
			}
			if (patt[p1] == ')') {
				return false;
			}
			else {
				while (patt[p1] != ')') p1++;
				p1++;
				p2++;
				continue;
			}
		}
		else {
			if (patt[p1] != str[p2]) {
				return false;
			}
			else {
				p1++;
				p2++;
			}
		}
		
	}
	if (patt[p1] == 0 && str[p2] == 0) return true;
	return false;
}

int main() {
	int i, j;
	int res;
	int L, D, N;
	scanf("%d%d%d", &L, &D, &N);
	for (i = 0; i < D; i++) {
		scanf("%s", dict[i]);
	}
	for (i = 0; i < N; i++) {
		res = 0;
		scanf("%s", patt);
		for (j = 0; j < D; j++) {
			if (match(patt, dict[j])) {
				res++;
			}
		}
		printf("Case #%d: %d\n", i + 1, res);
	}
	
	return 0;
}
