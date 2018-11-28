#include <stdio.h>
#include <math.h>

int main() {
	int out[] = {5,27,143,751,935,607,903,991,335,47,943,471,55,447,463,991,95,607,263, 151, 855, 527, 743, 351, 135, 407, 903, 791, 135, 647};
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	int ZZ;
	scanf("%d", &ZZ);
	for(int zz = 1; zz <= ZZ; zz++) {
		int n;
		scanf("%d", &n);
		printf("Case #%d: %03d\n", zz, out[n-1]);
	}
	return 0;
}