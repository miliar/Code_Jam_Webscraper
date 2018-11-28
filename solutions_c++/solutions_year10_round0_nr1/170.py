#include <stdio.h>
#include <string.h>

int main() {
	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; i++) {
		int N, K;
		scanf("%d %d", &N, &K);
		printf("Case #%d: %s\n", i+1, ((K & ((1 << N)-1))==((1<<N)-1))?"ON":"OFF");
	}
	return 0;
}
