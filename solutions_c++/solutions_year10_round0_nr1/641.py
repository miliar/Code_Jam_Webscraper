#include <cstdio>

int pow(int n) {
	int i;
	int ans = 1;
	for (i = 0; i < n; i++) {
		ans*=2;
	}
	return ans;
} 

int main() {
	int n, k, t;
	scanf("%d", &t);
	int i;
	for (i = 0; i < t; i++) {
		scanf("%d %d", &n, &k);
		printf("Case #%d: %s\n", i+1, (k % pow(n)) == pow(n)-1? "ON": "OFF");
	}
}
