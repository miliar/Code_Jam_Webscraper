#include <stdio.h>

int main()
{
	int t;
	int clearPair[26][26], transformPair[26][26];
	int queue[101], qlen;
	scanf("%d", &t);
	for (int cases = 0; cases<t; cases++)
	{
		for (int i = 0; i<26; i++)
			for (int j = 0; j<26;j++) {
				clearPair[i][j] = -1;
				transformPair[i][j] = -1;
			}
		qlen = 0;

		int D;
		scanf("%d", &D);
		for (int i = 0; i<D; i++) {
			char str[10];
			scanf("%s", str);
			int from = str[0]-'A';
			int to = str[1] - 'A';
			int result = str[2] -'A';
			transformPair[from][to] = transformPair[to][from] = result;
		}
		int N;
		scanf("%d", &N);
		for (int i = 0; i <N; i++) {
			char str[10];
			scanf("%s", str);
			int from = str[0]-'A', to = str[1]-'A';
			clearPair[from][to] = clearPair[to][from] = 1;
		}

		char str[101];
		int len;
		scanf("%d %s", &len, str);

		int curr, prev;
		qlen = 0;
		for (int i = 0; i<len; i++) {
			curr = str[i] - 'A';
			if (qlen == 0) {
				queue[0] = curr;
				qlen = 1;
				continue;
			}
			prev = queue[qlen-1];
			if (transformPair[prev][curr] != -1) {
				queue[qlen-1] = transformPair[prev][curr];
				curr = queue[qlen-1];
			}
			else {
				queue[qlen] = curr;
				qlen++;
			}
			
			for (int j = 0; j<qlen-1; j++) {
				if (clearPair[curr][queue[j]] == -1)
					continue;

				qlen = 0;
				break;
			}
		}

		printf("Case #%d: [", cases+1);
		if (qlen > 0) {
			printf("%c", queue[0]+'A');
			for (int i = 1; i<qlen; i++) {
				printf(", %c", queue[i]+'A');
			}
		}
		printf("]\n");
	}
	return 0;
}
