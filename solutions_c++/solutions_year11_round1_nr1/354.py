#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>

using namespace std;

int gcd( int x, int y )
{
    if ( x < y )
        return gcd(y,x);
    if ( !y )
        return x;
    if ( x&1 ) {
        if ( y&1 )
            return gcd(y,x-y);
        return gcd(x,y>>1);
    }
    else {
         if ( y&1 )
             return gcd(x>>1,y);
         return gcd(x>>1,y>>1)<<1;
    }
}

int T, Pd, Pg;
long long N;

int main()
{
	freopen("A-large.in","r",stdin);

	int t = 0, d;

	for ( scanf("%d",&T); T; T-- ) {
		scanf("%lld%d%d",&N,&Pd,&Pg);
		printf("Case #%d: ",++t);	

		
		d = gcd(Pd,100);
		d = 100 / d;

		if ( d > N ) {
			printf("Broken\n");
			continue;
		}
		if ( !Pd ) {
                        if ( Pg == 100 )
                                printf("Broken\n");
                        else
                                printf("Possible\n");
                        continue;
                } 

		if ( !Pg ) {
			if ( !Pd )
				printf("Possible\n");
			else
				printf("Broken\n");
			continue;
		}

		if ( Pd < 100 ) {
			if ( Pg == 100 )
				printf("Broken\n");
			else
 				printf("Possible\n");
		}
		else
			printf("Possible\n");
	}

	return 0;
}
			
