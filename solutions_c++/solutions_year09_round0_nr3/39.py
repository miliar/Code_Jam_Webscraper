#include <cstdio>
#include <cstring>


int N;
char input[5001];

int pd[20];
char teste[50] = "welcome to code jam";

void process() {
	memset(pd, 0, sizeof(pd));
	pd[0] = 1;
	for (int i = 0 ; input[i] ; i++) {
		for (int j = 19 ; j > 0 ; j--) {
			if (input[i] == teste[j-1]) {
				pd[j] += pd[j-1];
				if (pd[j] >= 10000) {
					pd[j] %= 10000;
				}
			}
		}
	}
	printf("%04d\n", pd[19]);
}

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	
	scanf("%d ", &N);
	for (int i = 1 ; i <= N ; i++) {
		printf("Case #%d: ", i);
		gets(input);
		process();
	}
	
	
	return 0;
}
