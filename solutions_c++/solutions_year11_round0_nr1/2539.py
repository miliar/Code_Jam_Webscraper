#include <cstdio>
#include <queue>
#include <vector>
using namespace std;

int main() {
    
    int T;
    scanf( "%d", &T );
    
    for ( int tc = 1; tc <= T; tc++ ) {
        int sol = 0;
        
        int N;
        scanf( "%d", &N );
        
        queue<int> Q[2];
        vector<pair<int,int> > moves;
        
        for ( int i = 0; i < N; i++ ) {
            char s[10];
            int p;
            scanf( "%s %d", s, &p );
            if ( s[0] == 'O' ) {
                Q[0].push( p );
                moves.push_back( pair<int,int>( 0, p ) );
            }
            else {
                Q[1].push( p );
                moves.push_back( pair<int,int>( 1, p ) );
            }
        }
        
        int pos[2] = { 1, 1 };
        
        for ( int i = 0; i < N; i++ ) {
            int idx = moves[i].first;
            
            while ( true ) {
                sol++;
                
                // move the other one
                if ( pos[idx^1] > Q[idx^1].front() ) pos[idx^1]--;
                else if ( pos[idx^1] < Q[idx^1].front() ) pos[idx^1]++;
                
                if ( pos[idx] > Q[idx].front() ) pos[idx]--;
                else if ( pos[idx] < Q[idx].front() ) pos[idx]++;
                else { // press button             
                    Q[idx].pop();
                    break;
                }              
                
            }
            
        }        
        
        printf( "Case #%d: %d\n", tc, sol );
    }
    
}
