#include <cstdio>
#include <cmath>
using namespace std;

void test() {
	int n, a, x=0, s=0, mini = 2000000;
	scanf("%d", &n);
	while (n--) {
		scanf("%d", &a);
		x ^= a;
		s += a;
		if (a < mini) mini = a;
	}
	printf(x == 0 ? "%d\n" : "NO\n", s - mini);
}

main() {
	int z;
	scanf("%d", &z);
	for (int c = 0; c<z;c++) {
		printf("Case #%d: ", c+1);
		test();
	}
}

