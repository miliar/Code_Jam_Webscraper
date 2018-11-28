#include <cstdio>

int main() {
	
	int T, TT;
	scanf("%d", &TT);
	for (T = 1; T <= TT; T++) {
		int A, B;
		long long t = 0;
		int digits = 1;
		int c;
		int i;
		
		scanf("%d %d", &A, &B);
		i = A;
		while (i > 0) {
			digits*=10;
			i /= 10;
		}
		digits /= 10;
		for (i = A; i < B; i++) {
			c = i;
			c = (c % digits * 10) + c / digits;
			while (c != i) {
				if (c > i && c <= B)
					t++;
				c = (c % digits * 10) + c / digits;
			}
		}
		printf("Case #%d: %I64d\n", T, t);
	}
	
	
}
