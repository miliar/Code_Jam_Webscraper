#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

int prime[100000], p, T;
long long n;
int main() {
	FILE *fin = fopen("C.in", "r");
	FILE *fout = fopen("C.out", "w");

	FILE *pr = fopen("primes.txt", "r");
	do {
		int a;
		fscanf(pr, "%d", &a);
		prime[p++] = a;
	} while (prime[p-1] < 1000000);
	fclose(pr);




	fscanf(fin, "%d", &T);
	for (int test = 0; test < T; test++) {
		fscanf(fin, "%lld", &n);

		if (n == 1) {
			fprintf(fout, "Case #%d: 0\n", test+1);
			continue;
		}


		long long ans = 1;
		for (int i = 0; (long long)prime[i]*(long long)prime[i] <= n; i++) {
			//printf("%d\n", prime[i]);
			long long pr = prime[i], j;
			for (j = 0; pr <= n; pr*=prime[i], j++);
			ans += j-1;
		}
		printf("Case #%d: %lld\n", test+1, ans);
		fprintf(fout, "Case #%d: %lld\n", test+1, ans);
	}

	return 0;
}
