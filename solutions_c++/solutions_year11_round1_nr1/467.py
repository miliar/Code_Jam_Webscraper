#include <iostream>
#include <stdio.h>
using namespace std;

#define ll long long

ll n,p1,p2;
int T;

ll NZD( ll a, ll b )
{
    if ( b == 0LL ) return a;
    return NZD( b, a%b );
}

int main()
{
    freopen("google1.in","r",stdin);
    freopen("google1.out","w",stdout);

    scanf("%d",&T);
    for (int t = 0; t < T; t++) {
        scanf("%lld%lld%lld",&n,&p1,&p2);

        bool ok = true;
        if ( p2 == 100LL && p1 != 100LL ) ok = false;
        if ( p2 == 0LL && p1 != 0LL ) ok = false;

        ll sto = 100LL;
        ll nzd = NZD( sto, p1 );
        ll odi = sto/nzd;

        if ( odi > n ) ok = false;

        printf("Case #%d: ",t+1);
        if ( ok ) printf("Possible\n");
        else      printf("Broken\n");

    }

    return 0;
}
