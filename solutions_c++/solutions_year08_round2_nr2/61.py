#include <cstdio>
#include <cstring>
#include <cstdlib>
typedef long long int64;

#define maxn (1 << 10)

int p[maxn], sc;

int getp(int v) { return v != p[v] ? p[v] = getp(p[v]) : v; }

void link(int u, int v) {
	u = getp(u);
	v = getp(v);
	if(u == v) return;
	sc--;
	if(rand() & 1) p[v] = u;
	else p[u] = v;
}

int gcd(int a, int b) { return b ? gcd(b, a % b) : a; }


int fact(int n) {
	int mp = 1;
	for(int i = 2; i*i <= n; i++)
		if(n % i == 0) {
			mp = i;
			while(n % i == 0) n /= i;
		}
	if(n > mp) mp = n;
	return mp;
}

int main() {
	srand(666);
	int t, tc;
	scanf("%d", &tc);
	for(t = 1; t <= tc; t++) {
		int a, b, pp, i, j;
		scanf("%d%d%d", &a, &b, &pp);
		for(i = a; i <= b; i++) p[i] = i;
		sc = b-a+1;
		for(i = a; i <= b; i++)
			for(j = i+1; j <= b; j++) {
				int c = gcd(i, j);
				if(fact(c) >= pp) link(i, j);
			}
		printf("Case #%d: %d\n", t, sc);
	}
	return 0;
}
