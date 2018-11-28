#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int perm[10],   K,  T;

string  s1, s2;

int mx, now;

int main() {
    
    freopen( "D-small-attempt0.in", "r", stdin );
    freopen( "D-result.txt", "w", stdout );
    
    cin >> T;
    
    for( int t = 1; t <= T; ++t ) {
        cin >> K;
        cin >> s1;
        s2 = s1;
        for( int i = 0; i < K; ++i )
            perm[i] = i;
        
        mx = 0x7FFFFFFF;
        
        do {
            for( int i = 0; i < K; ++i ) {
                for( int j = 0; j * K < s1.size(); ++j )
                    s2[j*K+perm[i]] = s1[j*K+i];
                now = 0;
            }
                for( int j = 1; j < s1.size(); ++j )
                    now += ( s2[j] != s2[j-1] );
                mx <?= now;
        } while( next_permutation( perm, perm + K ) );
        
        printf( "Case #%d: ", t );
        
        cout << mx +1 << endl;
        
    }

    
}
