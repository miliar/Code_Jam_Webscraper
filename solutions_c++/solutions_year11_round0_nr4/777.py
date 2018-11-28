#include <cstdio>

int main() {
	int ncases;
	scanf("%d", &ncases);
	for(int casenum = 1; casenum <= ncases; casenum++) {
		int n;
		scanf("%d", &n);
		int count = 0;
		for(int i = 1; i <= n; i++) {
			int v;
			scanf("%d", &v);
			if(v != i)
				count++;
		}
		printf("Case #%d: %d.000000\n", casenum, count);
	}
}

