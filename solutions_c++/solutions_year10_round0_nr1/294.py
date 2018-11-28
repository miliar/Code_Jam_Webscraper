#include <stdio.h>
int main() {
	int ncases;
	scanf("%d", &ncases);
	for (int z=1,n,k;2==scanf("%d %d", &n, &k);++z)
		printf("Case #%d: %s\n", z, (k&((1<<n)-1))==((1<<n)-1) ? "ON" : "OFF");
}
