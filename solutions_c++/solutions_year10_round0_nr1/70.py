#include <cstdio>
#include <algorithm>
using namespace std;

bool judge(int n, int k) {
	for (int i = 0; i < n; i++) {
		if (k % 2 == 0) return false;
		k /= 2;
	}
	return true;
}

int main() {
	int case_max;
	scanf("%d", &case_max);
	for (int c = 1; c <= case_max; c++ ) {
		int n, k;
		scanf(" %d %d", &n, &k);
		printf("Case #%d: ", c);
		if (judge(n, k)) printf("ON\n"); else printf("OFF\n");		
	}
	return 0;
}