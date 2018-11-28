#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int PER[10],   P,  T;

string  s1, s2;

int mx, now;

int main() {
    
    freopen( "D-small-attempt0.in", "r", stdin );
    freopen( "D-result.txt", "w", stdout );
    
    cin >> T;
    
    for( int t = 1; t <= T; ++t ) {
        cin >> P;
        cin >> s1;
        s2 = s1;
        for( int i = 0; i < P; ++i )
            PER[i] = i;
        
        mx = 0x7FFFFFFF;
        
        do {
            for( int i = 0; i < P; ++i ) {
                for( int j = 0; j * P < s1.size(); ++j )
                    s2[j*P+PER[i]] = s1[j*P+i];
                now = 0;
            }
                for( int j = 1; j < s1.size(); ++j )
                    now += ( s2[j] != s2[j-1] );
                mx <?= now;
        } while( next_permutation( PER, PER + P ) );
        
        printf( "Case #%d: ", t );
        
        cout << mx +1 << endl;
        
    }

    
}
