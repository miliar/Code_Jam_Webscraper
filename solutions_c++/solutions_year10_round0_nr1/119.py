#include <stdio.h>
int main(int argc, char* argv[]) {
	int T;
	scanf("%d", &T);
	int kth;
	for (kth=1; kth<=T; ++kth) {
		int N, K;
		scanf("%d%d", &N, &K);
		bool ok = (K%(1<<N) == ((1<<N)-1));
		printf("Case #%d: %s\n", kth, ok ? "ON" : "OFF");
	}
	return 0;
}