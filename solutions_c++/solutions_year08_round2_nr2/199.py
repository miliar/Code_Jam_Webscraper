#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <set>

using namespace std;

#define MAXV 1000010
#define MAX 1001000

int primes[80000], qtde;
char isprime[MAX+1];

void sieve() {
	int i, j;
	memset(isprime,-1,sizeof(isprime));
	isprime[0] = isprime[1] = 0, isprime[2] = 1;
	qtde = 1, primes[0] = 2;
	for (i=4; i <= MAX; i+=2)
		isprime[i] = 0;
	for (j=3; j <= MAX; j+=2) {
		if (isprime[j] == -1) {
			isprime[j] = 1;
			primes[qtde++] = j;
			for (i=2*j; i <= MAX; i+=j)
				isprime[i] = 0;
		}
	}
}

int id[MAXV], sz[MAXV];

void uf_init(int n) {
	int i;
	for (i=0; i < n; i++)
		sz[id[i] = i] = 1;
}

int getid(int v) {
	while (v != id[v]) v = id[v];
	return v;
}

int uf_find(int v, int w) {
	return (getid(v) == getid(w));
}

void uf_union(int v, int w) {
	int i = getid(v), j = getid(w);
	if (i == j) return;
	if (sz[i] < sz[j])
		sz[id[i] = j] += sz[i];
	else
		sz[id[j] = i] += sz[j];
}

long long gcd(long long a, long long b) {
	return b ? gcd(b,a%b) : a;
}

int main() {
	int cases, t = 1;
	long long a, b, p, i, j, factor, k;
	
	sieve();
	
	scanf("%d",&cases);
	while (cases--) {
		set <int> table;
		
		scanf("%lld %lld %lld",&a,&b,&p);
		uf_init((int)(b-a+1));
		
		for (i=a; i <= b; i++) {
			for (j=i+1; j <= b; j++) {
				factor = gcd(i,j);
				for (k=0; primes[k] < factor; k++) {
					while (factor%primes[k] == 0)
						factor /= primes[k];
				}
				if (((factor == 1)?primes[k-1]:factor) >= p)
					uf_union((int)(i-a),(int)(j-a));
			}
		}
		
		for (i=a; i <= b; i++)
			table.insert(getid((int)(i-a)));
		
		printf("Case #%d: %d\n",t++,table.size());
	}
	
	return 0;
}
