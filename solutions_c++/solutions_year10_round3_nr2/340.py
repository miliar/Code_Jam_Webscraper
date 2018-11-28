#include <iostream>
#include <cstdio>
#include <fstream>
#include <math.h>
#include <cstdlib>
#include <algorithm>
#include <map>
using namespace std;

typedef long long ll;

#define f first
#define s second
#define mk make_pair
#define pii pair<int,int>

int l,p,c;
map< pii , int > M;

int solve( int can , int cant ){
    if( can * (ll)c >= cant ) return 0;

    int v = M[ mk(can,cant) ];

    if( v > 0 ) return v;

    int sol = 9999;

    int g = cant;

    while( can * c < g ){
        g = ceil( g/(double)c );
        int s1 = solve( g , cant ) + 1;
        int s2 = solve( can , g ) + 1;

        sol = min( sol , max( s1 , s2) );
       // if( can == 50 && cant == 700 )cout<<g<<" = "<<s1<<" "<<s2<<endl;
    }
    return M[ mk(can,cant) ] = sol;
}

int main(){
    freopen("Ulaz.txt","r",stdin);
    freopen("Izlaz.txt","w",stdout);
    int tests;
    scanf("%d",&tests);

    for( int t = 1; t <= tests; ++t ){
        M.clear();
        scanf("%d%d%d",&l,&p,&c);

        printf("Case #%d: %d\n",t,solve( l , p ) );


    }

    return 0;
}
