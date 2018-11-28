#include <cstdio>

#define rep(i, a, b) for(int i = (a); i < int(b); ++i)
#define trav(it, v) for(typeof((v).begin()) it = (v).begin(); \
                        it != (v).end(); ++it)

typedef long long ll;

template <class Z> Z gcd(Z a, Z b) {
	return b==0 ? a : gcd(b, a%b);
}

int main() {
	int T;
	scanf("%d", &T);
	rep(t,0,T) {
		printf("Case #%d: ",t+1);
		int Pd, Pg;
		ll N;
		scanf("%lld%d%d", &N, &Pd, &Pg);
		int a, b, c, d;
		int g = gcd(Pd, 100);
		a = Pd/g;
		b = 100/g;
		g = gcd(Pg, 100);
		c = Pg/g;
		d = 100/g;
		
		bool pos = b<=N;
		if(a) pos = pos && c>0;
		if(b-a) pos = pos && d-c>0;
		printf(pos ? "Possible\n" : "Broken\n");
	}
	
	
	return 0;
}