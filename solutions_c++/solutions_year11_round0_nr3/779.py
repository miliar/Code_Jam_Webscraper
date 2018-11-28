#include <cstdio>

int main() {
	int ncases;
	scanf("%d", &ncases);
	for(int casenum = 1; casenum <= ncases; casenum++) {
		int n;
		scanf("%d", &n);
		int Xor = 0;
		int minv = 100000000;
		int sum = 0;
		for(int i = 0; i < n; i++) {
			int value;
			scanf("%d", &value);
			Xor ^= value;
			if(value < minv)
				minv = value;
			sum += value;
		}
		printf("Case #%d: ", casenum);
		if(Xor == 0)
			printf("%d\n", sum - minv);
		else
			printf("NO\n");
	}
}
