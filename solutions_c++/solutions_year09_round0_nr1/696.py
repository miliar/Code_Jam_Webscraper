#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define MAX_L 16
#define MAX_D 5001
#define MAX_N 501

int L, D, N;
char dic[MAX_D][MAX_L];

int match(char* word) {
	int res = 0;
	int length = strlen(word);
	for (int i = 0; i < D; ++i) {
		int ptr = 0;
		bool ok = true;
		for (int j = 0; j< L; ++j) {
			if (ptr >= length) {
				ok = false;
				break;
			}
			if (word[ptr] == '(') {
				bool find = false;
				while (ptr < length && word[ptr] != ')') {
					if (word[ptr] == dic[i][j])
						find = true;
					ptr++;
				}
				if (find == false) {
					ok = false;
					break;
				} else
					ptr++;
			} else {
				if (dic[i][j] != word[ptr]) {
					ok = false;
					break;
				} else
					ptr++;
			}
		}
		if (ok == true)
			res++;
	}
	return res;
}

int main(int argc, char* argv[]) {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	scanf("%d%d%d", &L, &D, &N);
	for (int i = 0; i < D; ++i)
		scanf("%s", dic[i]);

	for (int k = 1; k <= N; ++k) {
		char word[MAX_D];
		scanf("%s", word);
		printf("Case #%d: %d\n", k, match(word));
	}

	return 0;
}
