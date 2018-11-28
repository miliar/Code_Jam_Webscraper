#include <iostream>
#include <cstdio>
using namespace std;
int main() {
	int T, cs = 1;
	scanf("%d", &T);
	while(T--) {
		int N, K;
		scanf("%d%d", &N, &K);
		printf("Case #%d: ", cs);
		if(K % (1 << N) == (1 << N) - 1)
			printf("ON\n");
		else
			printf("OFF\n");
		++cs;
	}
	return 0;
}
