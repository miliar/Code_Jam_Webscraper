#include <stdio.h>

#define MAXK 10240

int data[MAXK];

int main(int argc, char *argv[])
{
	int i, j, index;
	int K, n;
	int t, N;

	scanf("%d", &N);
	for(t = 1; t <= N; t++) {
		scanf("%d %d", &K, &n);

		for(i = 1; i <= K; i++)data[i] = 0;
		index = 0;
		for(i = 1; i <= K; i++) {
			for(j = 0; j < i; j++) {
				if(++index > K)index = 1;
				while(data[index] != 0) {
					if(++index > K)index = 1;
				}
			}
			data[index] = i;
		}

		printf("Case #%d:", t);
		for(i = 0; i < n; i++) {
			scanf("%d", &j);
			printf(" %d", data[j]);
		}
		printf("\n");
	}

	return 0;
}
