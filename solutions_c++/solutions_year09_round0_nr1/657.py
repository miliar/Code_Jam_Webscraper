#include <stdio.h>
#include <string.h>

#define D 5001
#define L 16

char word[D][L][26];
char dict[D][L];

int main()
{
	int nD, nL, N;
	char ctmp, line[2048];

	for (int i = 0; i<D; i++)
		for (int j = 0; j<L; j++)
			for (int k = 0; k<26; k++)
				word[i][j][k] = 0;

	scanf("%d%d%d", &nL, &nD, &N);

	for (int i = 0; i<nD; i++)
		scanf("%s", dict[i]);

	int l = 0;
	int lefted;
	for (int i = 0; i<N; i++) {
		scanf("%s", line);
		l = 0;
		lefted = 0;
		for (int j = 0; j<strlen(line); j++) {
			if (line[j] == '(') {
				lefted = 1;
			}
			else if (line[j] == ')') {
				lefted = 0;
				l ++;
			}
			else if (line[j] >= 'a' && line[j] <= 'z'){
				word[i][l][line[j]-'a'] = 1;
				if (lefted == 0)	l++;
			}
		}
	}


	for (int i = 0; i<N; i++) {
		int ans = 0;
		for (int j = 0; j<nD; j++) {
			int k;
			for (k = 0; k<nL; k++) {
				if (word[i][k][dict[j][k]-'a'] == 0)
					break;
			}
			if (k >= nL)	ans++;
		}
		printf("Case #%d: %d\n", i+1, ans);
	}
	return 0;
}
