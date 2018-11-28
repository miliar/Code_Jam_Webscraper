#define _CRT_SECURE_NO_DEPRECATE

#include <cstdio>
#include <cstdlib>

int main() {
	int t, tn;
	int n, k, l;
	
	scanf("%d", &tn);
	for (t = 1; t <= tn; t++)  {
		scanf("%d %d", &n, &k);
		l = 1 << n;
		printf("Case #%d: %s\n", t, (k % l == l - 1) ? "ON" : "OFF");
	}
	
	return (0);
} 
