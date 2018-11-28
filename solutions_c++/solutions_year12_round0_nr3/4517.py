#include <cstdio>
#include <cmath>

int T, A, B;

int ndigits(int n)
{
	int d = 0;

	while(n) {
		d++;
		n /= 10;
	}

	return d;
}

int isrec(int a, int b)
{
	int d = ndigits(a)-1;

	int p = 0;

	for(int i = 0; i < d && !p; ++i) {
//		printf("b1:%d\n", b);
		b = (b/10) + (b%10)*pow(10, d);
//		printf("b2:%d\n", b);


		p = a == b;
	}

	return p;
}

int main()
{
	scanf(" %d", &T);

	for(int _42 = 1; _42 <= T; ++_42) {
		scanf(" %d %d", &A, &B);

		int ans = 0;

		for(int n = A; n <= B; ++n) {
			for(int m = n+1; m <= B; ++m) {
				if(ndigits(n) != ndigits(m)) continue;

				ans += isrec(n, m);
			}
		}

		printf("Case #%d: %d\n", _42, ans);
	}

	return 0;
}
