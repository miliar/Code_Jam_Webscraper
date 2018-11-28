#include <stdio.h>
#include <string.h>

using namespace std;

int main() {
	int tests;
	scanf("%d", &tests);
	for (int test = 0; test < tests; test++) {
		int n, k;
		scanf("%d %d", &n, &k);
		int l = 1<<n;
		printf("Case #%d: ", test+1);
		if ((k+1) % l == 0) {
			printf("ON\n");
		} else {
			printf("OFF\n");
		}
	}
	return 0;
}

