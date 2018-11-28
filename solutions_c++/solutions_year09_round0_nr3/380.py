#include <stdio.h>

#define MAX 512
#define MOD 10000

int mic[MAX][MAX];

char pattern[] = "welcome to code jam";
int len = 19;

void find_ans() {
	int i, j;
	char input[MAX];

	gets(input);
	for(i = 0; input[i] != 0; i++) {
		for(j = 0; j < len; j++)
			mic[i][j] = 0;
		if(input[i] == pattern[0])
			mic[i][0] = 1;
	}

	for(i = 0; input[i] != 0; i++) {
		for(j = 0; j < len; j++) {
			if(i > 0)
				mic[i][j] += mic[i - 1][j];
			if(input[i] == pattern[j])
				if(j > 0)
					mic[i][j] += mic[i][j - 1];
			mic[i][j] %= MOD;
		}
	}

	printf("%04d", mic[i - 1][len - 1] % MOD);
}

int main(int argc, char *argv[])
{
	int i, N;
	char str[MAX];

	gets(str);
	sscanf(str, "%d", &N);
	for(i = 1; i <= N; i++) {
		printf("Case #%d: ", i);
		find_ans();
		printf("\n");
	}

	return 0;
}
