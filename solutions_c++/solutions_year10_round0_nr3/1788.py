#include <cstdio>
#include <cstring>
#define maxN 2010

using namespace std;

long long n, k, r, i, j, t, sum, curr;
long long viz[maxN], v[maxN];
long long stot[maxN], next[maxN];

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("C.out", "w", stdout);

	scanf("%lld", &t);
	for (long long ii = 1; ii <= t; ii++) {

		memset(stot, 0, sizeof(stot));
		memset(next, 0, sizeof(next));
		sum = 0; 
		curr = 0;

		fprintf(stderr, "%lld\n", ii);

		scanf("%lld%lld%lld", &r, &k, &n);
		for (i = 1; i <= n; i++) {
			scanf("%lld", &v[i]);
			sum += v[i];
			v[i + n] = v[i];
		}

		if (sum <= k) {
			printf("Case #%lld: %lld\n", ii, sum * r);
			continue;
		}

		for (i = 1; i <= n; i++) {
			sum = v[i];
			j = i;
			while (sum <= k) {
				j++;
				sum += v[j];
			}

			sum -= v[j];

			stot[i] = sum;
			if (j > n)	j -= n;
			next[i] = j;

//			fprintf(stderr, "%d  %d %d\n", i, next[i], stot[i]);
		}

//		fprintf(stderr, "\n");


		curr = 1; sum = 0;
		for (i = 1; i <= r; i++) {
			sum = sum + stot[curr];
			curr = next[curr];
		}

		printf("Case #%lld: %lld\n", ii, sum);
		
	}

	return 0;
}
