#include <stdio.h>
#include <stdlib.h>
#include <math.h>
long long  T,zu,N,c,d,flag;
long long ai,bi,tem,p;

long long gcd (long long aa, long long bb) 
{
    if (bb == 0)
       return aa;
       else
       return gcd (bb, aa % bb);
}

int main(){
	/*freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);*/
	scanf("%lld",&T);
	for (zu = 1; zu <= T; zu++){
		scanf("%lld%lld%lld",&N,&c,&d);
		if (c == 0 && d == 0) printf("Case #%lld: Possible\n",zu);
		else if (c != 0 && d == 0 ) printf("Case #%lld: Broken\n",zu);
			else if (c == 0 && d != 0 ){
					if (d != 100) printf("Case #%lld: Possible\n",zu);
					else printf("Case #%lld: Broken\n",zu);
					}
				else{	p = gcd(100, c);
						if (N >= (100/p) && (d != 100 || (d == 100 && c == 100))) printf("Case #%lld: Possible\n",zu);
						else printf("Case #%lld: Broken\n",zu);
				}
	}
	return 0;
}