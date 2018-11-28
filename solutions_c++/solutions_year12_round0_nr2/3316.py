#include <cstdio>

int main() {
	
	int T, TT;
	scanf("%d", &TT);
	for (T = 1; T <= TT; T++) {
		int googs, surps, min;
		int t = 0;
		int c;
		int i;
		
		scanf("%d %d %d", &googs, &surps, &min);
		for (i = 0; i < googs; i++) {
			scanf("%d", &c);
			if ((c+2) / 3 >= min) {
				t++;
				continue;
			}
			if ((c+4) / 3 >= min && surps > 0 && min > 1) {
				t++;
				surps--;
			}
		}
		printf("Case #%d: %d\n", T, t);
	}
	
	
}
