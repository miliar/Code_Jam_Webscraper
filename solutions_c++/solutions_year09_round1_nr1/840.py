#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAXN 50000

int hp[51][MAXN+1] = {0};

int convert(int n, int k) {
	int sum = 0;
	int d = 1;
	while (n > 0) {
		int m = n % k;
		sum += d * m;
		d *= 10;
		n /= k;
	}
	return sum;
}

int isHappy(int n, int k) {
	int used[MAXN+1] = {0};
	while (1) {
		used[n] = 1;
		int m = convert(n,k);
		//printf("%d %d\n", n, m);
		int sum = 0;
		while (m > 0) {
			int d = m % 10;
			sum += d * d;
			m /= 10;
		}
		n = sum;
		//printf("%d\n", n);
		if (hp[k][n] == 1) return 1;
		if (hp[k][n] == -1) return -1;
		if (used[n] == 1) return -1;
		if (n == 1) return 1;
	}
	return -1;
}

int toInteger(char* str, int start, int stop) {
	int k = 1;
	int sum = 0;
	for (int i=stop; i>=start; i--) {
		sum += k * (str[i] - '0');
		k *= 10;
	}
	return sum;
}

int main(void) {
	for (int k=2; k<=10; k++) {
		for (int i=2; i<=MAXN; i++) {
			if (isHappy(i,k) == 1) hp[k][i] = 1;
			else hp[k][i] = -1;
			
		}
	}
	int t;
	scanf("%d\n", &t);
	for (int c=1; c<=t; c++) {
		int p[502] = {0};
		int start = 0;
		int size = 0;
		char line[100];
		gets(line);
		int len = strlen(line);
		for (int i=0; i<=len; i++) {
			if (line[i] == ' ' || line[i] == '\0') {
				p[size++] = toInteger(line,start,i-1);
				start = i+1;
			}
		}
		printf("Case #%d: ", c);
		for (int n=2; n<=MAXN; n++) {
			int happy = 1;
			for (int i=0; i<size && happy; i++) {
				//printf("Test hp[%d][%d] = %d\n", p[i], n, hp[p[i]][n]);
				if (hp[p[i]][n] != 1) happy = 0;
			}
			if (happy == 1) {
				printf("%d\n", n);
				break;
			}
		}
	}
	return 0;
}
