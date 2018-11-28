#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstdlib>
using namespace std;

int c;
vector< string > cs;

int d;
vector< string > cd;

int n;
string invoke;
char combine[255][255];
bool opposed[255][266];

void input(){
    memset( combine,0,sizeof(combine));
    memset( opposed,0,sizeof(opposed));
    cd.clear();
    cs.clear();

    scanf("%d",&c);
    for( int i = 0; i < c; ++i ){
        string w; cin >> w;
        cs.push_back( w );
        combine[ w[0] ][ w[1] ] = w[2];
        combine[ w[1] ][ w[0] ] = w[2];
    }

    scanf("%d",&d);
    for( int i = 0; i < d; ++i ){
        string w; cin >> w;
        cd.push_back( w );
        opposed[ w[0] ][ w[1] ] = 1;
        opposed[ w[1] ][ w[0] ] = 1;
    }

    scanf("%d",&n);
    cin >> invoke;
}

int main(){
    freopen("Ulaz.txt","r",stdin);
    freopen("Izlaz.txt","w",stdout);
    int tests; scanf("%d",&tests);

    for( int t = 1; t <= tests; ++ t ){
        input();

        vector< char > sol;
        for( int i = 0; i < n; ++i ){
            char c = invoke[i];
            int sz = sol.size();
            if( sz && combine[c][ sol[sz-1] ] != 0 ){
                sol.pop_back();
                sol.push_back( combine[c][ sol[sz-1] ] );
            }else sol.push_back( c );

            bool clr = 0;
            for( int i = 0; i < sol.size(); ++i )
                for( int j = 0; j < sol.size(); ++j )
                    if( opposed[ sol[i] ][ sol[j] ] ) clr = 1;
            if( clr ) sol.clear();
        }


        printf("Case #%d: [",t);
        for( int i = 0; i < sol.size(); ++i ){
            printf("%c",sol[i]);
            if( i != sol.size() - 1 ) printf(", ");
        }printf("]\n");
    }

    return 0;
}
