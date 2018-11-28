#include <iostream>
#include <fstream>
#include <cstdlib>
#include <math.h>
#include <algorithm>
#include <queue>
#include <map>
using namespace std;

typedef long long ll;

int n,k;

int main(){
    freopen("Ulaz.txt","r",stdin);
    freopen("Izlaz.txt","w",stdout);

    int tests;
    scanf("%d",&tests);
    for( int t = 1; t <= tests; ++t ){
        scanf("%d%d",&n,&k);

        ll cnt = 0;
        for( ll i = 0 , p2 = 1; i < n; ++i , p2 <<= 1 )
            cnt += p2;

        bool on = false;

        if( cnt == k ) on = true;
        else if( cnt < k ){
            ll w = cnt + 1;
            ll d = k / w;

            if( k % w == 0 ) d --;

            k = k - w * d;
            if( cnt == k ) on = true;
        }

        if( on ) printf("Case #%d: ON\n",t);
        else printf("Case #%d: OFF\n",t);

    }

    return 0;
}
