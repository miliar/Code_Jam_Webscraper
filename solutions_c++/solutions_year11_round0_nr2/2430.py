#include <cstdio>
#include <cstring>
#include <vector>
#include <deque>
using namespace std;

int present[256];
char conv[256][256];

int main() {
    
    int T;
    scanf( "%d", &T );
    
    for ( int tc = 1; tc <= T; tc++ ) {
        memset( present, 0, sizeof(present) );
        memset( conv, 0, sizeof(conv) );
        
        int C, D;
        
        scanf( "%d", &C );
        for ( int i = 0; i < C; i++ ) {
            char s[10];
            scanf( "%s", s );
            conv[s[0]][s[1]] = conv[s[1]][s[0]] = s[2];
        }
        
        vector<pair<char, char> > opp;
        
        scanf( "%d", &D );
        for ( int i = 0; i < D; i++ ) {
            char s[10];
            scanf( "%s", s );
            opp.push_back( pair<char, char>( s[0], s[1] ) );
        }
        
        char inv[200];
        int N;
        scanf( "%d %s", &N, inv );
        
        //data
        /*
        printf( "C = %d D = %d N = %d\n", C, D, N );
        for ( int i = 0; i < opp.size(); i++ )
            printf( "X %c %c\n", opp[i].first, opp[i].second );
        printf( "--> %s\n", inv );
        //break;
        */
        
        deque<char> res;
        
        for ( int i = 0; i < N; i++ ) {
            res.push_back( inv[i] );
            present[inv[i]]++;
            
            int ss = res.size();
            
            if ( ss > 1 ) {
                if ( conv[res[ss-1]][res[ss-2]] ) {
                    //printf( "R %c %c %c\n", res[ss-1], res[ss-2], conv[res[ss-1]][res[ss-2]] );
                    present[res[ss-1]]--;
                    present[res[ss-2]]--;
                    char nele = conv[res[ss-1]][res[ss-2]];
                    present[nele]++;
                    res.pop_back();
                    res.pop_back();
                    res.push_back( nele );
                }
                
                for ( int j = 0; j < opp.size(); j++ ) {
                    if ( present[opp[j].first] && present[opp[j].second] ) {
                        //printf( "X i = %d j = %d\n", i, j );
                        res.clear();
                        memset( present, 0, sizeof(present) );
                        break;
                    }
                }
            } 
        }
        
        printf( "Case #%d: ", tc );
        printf( "[" );
        for ( int i = 0; i < res.size(); i++ ) {
            printf( "%c", res[i] );
            if ( i + 1 < res.size() ) printf( ", " );
        }
        printf( "]\n" );
    }
    
}
