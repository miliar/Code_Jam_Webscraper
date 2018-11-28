#include <cstdio>

int main() {
	int caseNum;
	scanf("%d", &caseNum);
	for (int caseIndex = 1; caseIndex <= caseNum; caseIndex++) {
		int n, k;
		scanf("%d%d", &n, &k);
		printf("Case #%d: ", caseIndex);
		int mask = (1 << n) - 1;
		if ((k & mask) == mask) {
			puts("ON");
		} else {
			puts("OFF");
		}
	}
	
	return 0;
}
