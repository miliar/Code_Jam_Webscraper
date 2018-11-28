#include<stdio.h>

bool solve() {
	int N, K;
	scanf("%d%d", &N, &K);
	N=(1<<N)-1;
	return (K&N)==N;
}

int main() {
	int T;
	scanf("%d", &T);
	for(int c=1;c<=T;c++) {
		printf("Case #%d: ", c);
		if(solve()) puts("ON");
		else puts("OFF");
	}
}