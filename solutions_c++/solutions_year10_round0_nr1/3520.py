#include<stdio.h>

int main() {
	int cases;
	scanf("%d", &cases);
	for(int Case = 1; Case <= cases; ++Case) {
		int state = 0, power = 1;
		int n, k;
		scanf("%d%d", &n, &k);
		for(int i = 0; i < k; ++i) {
			state = (power ^ state);
			power = (state+1)^state;
		}
		printf("Case #%d: %s\n", Case, ((power>>n)&1) ? "ON" : "OFF");
	}
	return 0;
}
