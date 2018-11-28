#include <cstdio>

int getKeyNumber(int a) {
	int ret = 1;
	while (a != 0) {
		ret *= 10;
		a /= 10;
	}

	return ret / 10;
}

int rotate(int a, int keyNumber) {
	int ret = a / 10;
	ret += keyNumber * (a % 10);

	return ret;
}

void handle() {
	int a, b;
	scanf("%d %d ", &a, &b);

	int keyNumber = getKeyNumber(a);

	int ret = 0;

	for (int i = a; i <= b; i++) {
		int start = i;
		for (int j = 1; j < keyNumber; j++) {
//			printf("%d ", start);
			start = rotate(start, keyNumber);
//			printf("%d\n", start);
			if (start == i) {
				break;
			} else if (start > i && start <= b) {
				ret++;
			}
		}
	}

	printf("%d\n", ret);
}

int main() {
	int t;
	scanf("%d ", &t);

	for (int i = 0; i < t; i++) {
		printf("Case #%d: ", i + 1);

		handle();
	}

	return 0;
}
