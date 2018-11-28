#include<iostream>
#include<string>
#include<fstream>
using namespace std;

const int MOD = 10000;

string a, b;
int memo[ 20 ][ 503 ][ 20 ];

ofstream fout("C-large.out");
ifstream fin("C-large.in");

int rek( int n, int m, int k ) {
    
    if( memo[ n ][ m ][ k ] != -1 ) return memo[ n ][ m ][ k ];
    if( !k ) return 1; 
    if( m == b.size() || n == a.size() ) return 0;
    
    int ret = 0;
    
    for( int i = m; i < b.size(); i++ ) { 
         if( b[ i ] == a[ n ] ) { 
             ret = ret + rek( n + 1, i + 1, k - 1 );
             if( ret >= MOD ) ret -= MOD;
         }
         ret += rek( n + 1, i + 1, k );
         if( ret >= MOD ) ret -= MOD;
    }
         
    return memo[ n ][ m ][ k ] = ret; 
        
}

int main() {
    
    int N;
    fin >> N;
    getline( fin, b, '\n' );
    
    a = "welcome to code jam";
    
    for( int i = 0; i < N; i++ ) {
    
         memset( memo, -1, sizeof memo );
         
         getline( fin, b, '\n' );
    
    
         fout << "Case #" << i + 1 << ": ";
         
         int rj = rek( 0, 0, a.size() );
         if( rj >= 1000 ) fout << rj << endl;
         else if( rj >= 100 ) fout << "0" << rj << endl;
         else if( rj >= 10 ) fout << "00" << rj << endl;
         else fout << "000" << rj << endl;
         
    
    }
    
    return 0;    
}
