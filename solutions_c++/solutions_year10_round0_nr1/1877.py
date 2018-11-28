#include <cstdio>

int main() {
	int T; scanf("%d", &T);
	for (int cas=0;cas<T;++cas) {
		int N, K;
		scanf("%d%d", &N, &K);
		printf("Case #%d: ", cas+1);
		int M = K%(1<<N);
		if (M==(1<<N)-1) puts("ON"); else puts("OFF");
	}
	return 0;
}
