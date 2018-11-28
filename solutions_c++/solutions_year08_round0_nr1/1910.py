/* GCJ Problem A */
#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
#include <vector>
#define oo 10000000
using namespace std;

int memo[101][1001];

int S, Q;

vector <string> query, engine;

int go ( int qn, int en ){
    if ( qn == 0 ) return 0;
    if ( query[ qn - 1 ] == engine[ en ] ) return oo ;
    int &ret = memo[ qn ][ en ];
    
    if ( ret != -1 ) return ret;
    
    ret = oo;
    
    ret <?=  go ( qn - 1, en );
    
    for ( int i = 0; i < engine.size(); ++i )
        if ( i != en ) ret <?= 1 + go ( qn - 1, i );
    
    return ret;
}

int getint(){
    char in[10];
    
    gets ( in );
    
    return atoi( in );
}

int main(){
    int tc, t = 0;
    char in[105];
    string inp;
    
    freopen("f:/gcga.txt", "w", stdout);
    
    tc = getint();    

    while ( tc-- ){
        query.clear();
        engine.clear();        

        memset( memo, -1, sizeof( memo ) );
        
        S = getint();

        for ( int i = 0; i < S; ++i ){
            gets ( in );
            inp = in;
            engine.push_back ( inp );
        }

        Q = getint();
        
        for ( int i = 0; i < Q; ++i ){
            gets( in );
            inp = in;
            query.push_back ( inp );
        }        
        
        int opt = oo;
        
        for ( int i = 0; i < S; ++i ){
            opt <?= go ( Q, i );
        }
        
        printf( "Case #%d: %d\n", ++t, opt );
        
    }
}
