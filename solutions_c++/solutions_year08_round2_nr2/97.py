#include <cstdio>

int nprime;
int primes[1048576];
int sieve[1048576];

void init_primes(){
	for (int tmp = 2; tmp < 1048576; tmp++)
		if (!sieve[tmp]){
			for (int j = tmp; j < 1048576; j += tmp)
				sieve[j] = 1;
			primes[nprime++] = tmp;
		}
}

int sets[1048576];
int find_head(int k){
	if (sets[k] == k)
		return k;
	return sets[k] = find_head(sets[k]);
}

void join_set(int i, int j){
	int ih = find_head(i), jh = find_head(j);
	if (ih < jh)
		sets[jh] = ih;
	else
		sets[ih] = jh;
}

int main(){
	int c;
	long long a, b, p;

	init_primes();

	scanf("%d", &c);
	for (int cases = 0; cases < c; cases++){
		int result = 0;
		scanf("%lld%lld%lld", &a, &b, &p);

		for (int tmp = 0; tmp <= b-a; tmp++)
			sets[tmp] = tmp;

		if (p >= b-a)
			p = b-a;
		int foo;
		for (foo = 0; primes[foo] < p; foo++);
		for (int tmp = foo; primes[tmp] <= b-a; tmp++){
			long long prime = primes[tmp];
			for (long long i = (a+prime-1)/prime*prime; i + prime <= b; i += prime)
				join_set(i-a, i+prime-a);
		}
		for (int tmp = 0; tmp <= b-a; tmp++)
			if (find_head(tmp) == tmp)
				result++;
		printf ("Case #%d: %d\n", cases+1, result);
	}
	return 0;
}
