#include <iostream>
#include <cstdio>

using namespace std;

long long N, Pd, Pg;

long long gcd(long long a, long long b)
{
	if (b == 0) return a;
	return gcd(b, a % b);
}

int main()
{
	int numCase = 0, T;
	scanf("%d", &T);
	while (T--) {
		scanf("%I64d%I64d%I64d", &N, &Pd, &Pg);
		printf("Case #%d: ", ++numCase);
		long long g = gcd(Pd, 100);
		long long P = 100 / g, w = Pd / g, l = P - w;
		if (P > N) {
			puts("Broken");
			continue;
		}
		long long g2 = gcd(Pg, 100);
		long long x = Pg / g2, y = 100 / g2 - x;
		if (x == 0 && w != 0) {
			puts("Broken");
			continue;
		}
		if (y == 0 && l != 0) {
			puts("Broken");
			continue;
		}
		puts("Possible");
	}
}
