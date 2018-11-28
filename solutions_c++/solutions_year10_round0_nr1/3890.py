#include <stdio.h>

int main() {
	int T, _42=1, N, K;
	scanf(" %d", &T);
	while (T--) {
		scanf(" %d %d", &N, &K);
		printf("Case #%d: ", _42++);
		if (((1<<N) - 1) == K%(1<<N))
			printf("ON\n");
		else
			printf("OFF\n");
	}
	return 0;
}
