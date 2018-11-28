#include <cstdio>
#include <cstring>
#include <algorithm>

#define NN 2048

int sds(int n, int b) {
	int sum = 0;
	while(n) {
		sum += (n % b) * (n % b);
		n /= b;
	}
	return sum;
}

bool is_happy(int n, int b) {
	int mark[NN];

	for(int i = 0; i < NN; i++)
		mark[i] = 0;
	
	while(!mark[n] && n != 1) {
		mark[n] = 1;
		n = sds(n, b);
	}

	return n == 1;
}

int main(void) {
	int t, c = 1, i, j;
	char line[1024];
	int b[16], bn;

	scanf("%d", &t);
	fgets(line, sizeof(line), stdin);

	for(c = 1; c <= t; c++) {
		fgets(line, sizeof(line), stdin);
		bn = 0;
		char *p = strtok(line, " \n");
		for(bn = 0; p; bn++) {
			b[bn] = atoi(p);
			p = strtok(NULL, " \n");
		}

		for(i = 2;; i++) {
			for(j = 0; j < bn; j++)
				if(!is_happy(sds(i, b[j]), b[j])) break;
			if(j == bn) break;
		}
		printf("Case #%d: %d\n", c, i);
//		else printf("Case #%d: %d is an Unhappy number.\n", c, n);
	}

	return 0;
}
