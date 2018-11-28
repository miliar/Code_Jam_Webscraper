#include <stdio.h>

#define MAX 2048000

int a, b, ans;

int get_c(int n) {
	int mul = 1;
	while(n / mul >= 10)mul *= 10;

	int _n = n, c = 0, tmp;
	while(1) {
		tmp = n % 10;
		n /= 10;
		n += tmp * mul;
		if(_n == n)break;
		if(n / mul == 0)continue;
		if(n < a || n > b)continue;
		if(n < _n)return 0;
		c++;
	}
	return c;
}

void action() {
	int c;

	scanf("%d %d", &a, &b);

	ans = 0;
	for(int i = a; i <= b; i++) {
		c = get_c(i);
		if(c > 0)
			ans += c * (c + 1) / 2;
	}
	printf("%d", ans);
}

int main() {
	int t;
	scanf("%d ", &t);
	for(int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		action();
		printf("\n");
	}

	return 0;
}
