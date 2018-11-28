// vinicius zambaldi - UFSC

#include <cstdio>

int main (void) {
	long long int n, k;
	int i, t;
	scanf("%d", &t);
	for (i = 0; i != t; ++i) {
		scanf(" %lld %lld", &n, &k);
		printf("Case #%d: %s\n", i+1, ((1<<n)-1) == (k%(1<<n)) ? "ON" : "OFF");
	}
	return 0;
}
