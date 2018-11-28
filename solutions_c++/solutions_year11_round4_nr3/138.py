#include <stdio.h>
#include <algorithm>
#include <stdlib.h>
#include <string.h>
#include <math.h>

using namespace std;

int tb[1100000];
long long prime[100000];

int main() {
    int pp,d,i,tt,TT;
    long long n,s,x;
    pp = 1;
    prime[0] = 2;
    for( i=3; i<1100000; i+=2 ) {
        if(!tb[i]) {
            prime[pp++] = i;
            if(i<2000) {
                d = i*i;
                while(d<1100000) {
                    tb[d] = 1;
                    d+=i+i;
                }
            }
        }
    }
    scanf("%d",&TT);
    for( tt=0; tt<TT; tt++ ) {
        scanf("%lld",&n);
        if(n==1) {
            printf("Case #%d: 0\n",tt+1);
            continue;
        }
        s = 1;
        for( i=0; prime[i]*prime[i]<=n; i++ ) {
            x = prime[i]*prime[i];
            while(x<=n) {
                x*=prime[i];
                s++;
            }
        }
        printf("Case #%d: %lld\n",tt+1,s);
    }
    return 0;
}
