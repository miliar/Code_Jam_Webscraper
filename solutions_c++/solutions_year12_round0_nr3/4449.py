#include <vector>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <map>
using namespace std;

int T;

int main() {
    freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
    scanf( "%d", &T );
	for ( int I=1; I<=T; I++ ) {
        int A,B;
        scanf( "%d%d", &A, &B );
        int tot = 0;
        for ( int i=A; i<=B-1; i++ )
        for ( int j=i+1; j<=B; j++ ) {
            int len = 0;
            int tj =j;
            while ( tj!=0 ) {
                  tj /= 10;
                  len++;
            }
            
            int cw = 1;
            for ( int k=0; k<len-1; k++ ) cw *= 10;
            
            tj = j;
            for ( int k=0; k<len; k++ ) {
                int t = tj%10;
                tj /= 10;
                tj = t*cw+tj;
                //cout << i << " " << tj << " " << tot<< endl;
                if ( tj==i ) {
                   tot++;
                   break;
                }
            }
        }
        
        printf( "Case #%d: %d\n", I, tot );
    }
}
