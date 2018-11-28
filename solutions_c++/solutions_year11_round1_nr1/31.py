#include <iostream>
#include <cstdio>

using namespace std;

int gcd(int a,int b)
{
	if(a == 0)
		return b;
	return gcd(b%a, a);
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t++) {
		int n, k, k2;

		scanf("%d %d %d", &n, &k, &k2);

		printf("Case #%d: ", t+1);
		if (k == 0) {
			if (k2 == 100) {
				printf("Broken\n");
				continue;
			}	
			printf("Possible\n");
			continue;
		}
		if (k2 == 0) {
			if (k > 0) {
				printf("Broken\n");
				continue;
			}
			printf("Possible\n");
			continue;
		}
		
		int ok = 0;

		for (int a = 0; a <= n; a++) {
			if ((100*a)%k)
				continue;
			int D = 100*a/k;
			if (D > n)
				continue;
			if (D == 0)
				continue;
			int b = D-a;
			for (int c = 0; c <= 10000; c++) {
				if (((a+c)*100)%k2)
					continue;
				int g = ((a+c)*100)/k2;
				if (g < D)
					continue;
				int d = g-D-c;
				if (d < 0)
					continue;

//				printf("%d %d %d %d %d %d\n", a, b, D, c, d, g);

				ok = 1;
				goto done;
			}
		}
	done:
		if (ok)
		printf("Possible\n");
		else
			printf("Broken\n");
		
	}

	return 0;
}

