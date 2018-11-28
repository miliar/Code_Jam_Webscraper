#include <cstdio>

void possible(int test) {
	printf("Case #%d: Possible\n", test);
}

void broken(int test) {
	printf("Case #%d: Broken\n", test);
}

int main() {
	int TESTS;
	scanf("%d", &TESTS);
	for(int TEST = 1; TEST<=TESTS; TEST++) {
		long long N, Pd, Pg;
		scanf("%Ld%Ld%Ld", &N, &Pd, &Pg);
		if (Pg == 100 && Pd != 100) {
			broken(TEST);
		} else if(Pg == 0 && Pd != 0) {
			broken(TEST);
		} else if(Pd == 0) {
			possible(TEST);
		} else {
			int twos = 0;
			while(Pd % 2 == 0) {
				twos++;
				Pd/=2;
			}
			int fives = 0;
			while(Pd % 5 == 0) {
				fives++;
				Pd/=5;
			}
			int res = 1;
			for(int two = 0; two<2-twos; two++) {
				res *= 2;
			}
			for(int five = 0; five<2-fives; five++) {
				res *= 5;
			}
			if(res <= N) {
				possible(TEST);
			} else {
				broken(TEST);
			}
		}
	}
	return 0;
}
