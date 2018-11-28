#include <stdio.h>

int L, D, N;
char words[5000][16], query[400];
bool pattern[15][26];


int main() {
	scanf("%d %d %d", &L, &D, &N);
	for(int i = 0; i < D; i++) {
		scanf("%s", words[i]);
	}
	for(int casa = 1; casa <= N; casa++) {
		scanf("%s", query);
		for(int i = 0, k = 0; i < L; i++) {
			for(int j = 0; j < 26; j++) {
				pattern[i][j] = false;
			}
			if(query[k] != '(') {
				pattern[i][query[k] - 'a'] = true;
			} else {
				while(query[++k] != ')') {
					pattern[i][query[k] - 'a'] = true;
				}
			}
			k ++;
		}
		int count = 0;
		for(int i = 0; i < D; i++) {
			bool matched = true;
			for(int j = 0; words[i][j] != '\0'; j++) {
				if(!pattern[j][words[i][j] - 'a']) {
					matched = false;
				}
			}
			if(matched) {
				count ++;
			}
		}
		printf("Case #%d: %d\n", casa, count);
	}
	return 0;
}
