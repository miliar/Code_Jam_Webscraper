#include <stdio.h>

int main(){
	int T;
	scanf("%d", &T);
	for (int ttt = 1; ttt <= T; ttt++){
		int N, K;
		scanf("%d%d", &N, &K);
		printf("Case #%d: %s\n", ttt, (K+1)%(1<<N)?"OFF":"ON");
	}
	return 0;
}