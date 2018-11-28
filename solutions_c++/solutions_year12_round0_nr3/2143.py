#include <cstdio>
#include <set>
#include <algorithm>
#include <functional>

using namespace std;

typedef unsigned long long ull;
inline ull shift10( ull n,int p) {
    return (n/10)+(n%10)*p;
}

int main(){

    int testn;


    scanf("%d\n",&testn);
    for( int test=1;test<= testn; ++test) {

        set<pair<ull,ull> > pairs;
        ull A, B;

        scanf("%llu %llu\n",&A, &B);
        int pow=1, tmpa=A;

        while ( tmpa/=10 ) pow*=10;

        if ( pow>1) {

            for( ull a=A;a<=B; ++a ) {

                ull nshift=a;
                while( true ) {

                    nshift=shift10(nshift,pow);

                    if ( nshift<A || nshift>B) continue;
                    if( nshift==a ) break;

                    if ( a< nshift )
                        pairs.insert(make_pair(a,nshift));
                    else
                        pairs.insert(make_pair(nshift,a));
                }
            }
        }

        printf("Case #%d: %d\n",test,pairs.size());

    }
    return 0;
}

