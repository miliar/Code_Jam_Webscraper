#include<stdio.h>

long long abs(long long x) { return ( x > 0ll ? x : -x ); }
long long gcd(long long x, long long y) { return ( y ? gcd(y, x % y) : abs(x) ) ; }


int main (void) {
	int t,cases;
	long long n,pd,pg;
	scanf("%d",&t);
	for(cases = 1; cases <= t; cases++) {
		scanf("%lld %lld %lld",&n,&pd,&pg);
		printf("Case #%d: ",cases);
		if ( pg == 0ll && pd != 0ll ) printf("Broken\n");
		else if ( pg == 100ll && pd != 100ll ) printf("Broken\n");
		else if ( pd == 0ll ) printf("Possible\n");
		else {
			long long hoje = 100ll/gcd(pd,100ll);
			//long long tot = 100ll/gcd(pg,100ll);
			long long v_hoje = (pd*hoje)/100ll; 
			//v_tot = (pg*tot)/100ll;
			//printf("%lld %lld %lld %lld\n",v_tot,tot,v_hoje,hoje);
			//printf("%lld %lld %lld %lld\n",v_tot,tot,v_hoje,hoje);
			//printf("%lld %lld\n",v_hoje,hoje);
			if ( hoje <= n ) printf("Possible\n");
			else printf("Broken\n");
		}
	}
	return 0;
}
