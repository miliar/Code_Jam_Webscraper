#include <map>
#include <iostream>
#include <vector>
#include <algorithm>
#include <deque>

using namespace std;

int tab [ 1025][11];

int min ( int a, int b) {
    if ( a < b )
    return a;
    return b;
}
long long gcd ( long long a, long long b ) {
     if ( a < b )
        return gcd ( b, a );
     if ( b == 0 )
        return a;
     return gcd (b, a%b);    
     
}
int count ( int seed ) {
    int c = 0;
    for ( int i = 0; i < 20; i ++ )
        if ( seed & ( 1 << i ) )
           c ++;
           
    return c;
}

int main(int argc, char *argv[])
{
    
    
    int testCases;
    cin >> testCases;

    for ( int testCase = 1; testCase <= testCases; testCase ++ ) {
        int M, N; 
        cin >> M  >> N;
        vector <string > board;
        for ( int i = 0; i < M; i ++) {
            string a; cin >> a;
            board.push_back ( a );
        }
        memset ( tab, 0 , sizeof ( tab ));
        int c = 0;
        int r;
        for ( int seed = 0; seed < (1 << M); seed ++) {
              //  cout << "seed " << seed << endl;
                for (  r = 0 ; r < M; r ++)
                    if ( (seed & (1 << r)) && board [r][c] == 'x' )
                       break;
                if ( r == M ) {
                  // cout << "ok" << endl;  
                   tab [ seed ] [c] = count ( seed ); 
                   }                 
                else {
                  //   cout << "conf" << endl;
                     tab [seed][c] = 0; 
                     }   
            }
        
        for ( int c = 1; c < N; c ++ ) {
            for ( int seed = 0; seed < (1 << M); seed ++) {
                int r;
                for (  r = 0 ; r < M; r ++)
                    if ( (seed & (1 << r)) && board [r][c] == 'x' )
                       break;
                if ( r == M ) {
                    int max = 0;
                    for ( int seed2 = 0 ; seed2 < (1 << M); seed2 ++ )
                    if ( ! (seed & seed2) && ! ( seed & (seed2 << 1) ) && ! ( (seed << 1) & seed2 ) )
                       if ( count ( seed ) + tab [seed2][c-1] > max )
                          max = count ( seed ) + tab [seed2][c-1];
                    tab [ seed][c] = max ;
                    //cout << seed << " x " <<  tab [ seed][c] << endl;
                }
               // else cout << "seed " << seed << " " << c << " bad " << endl;
                    
            }        
        }
        int max = 0;
        for ( int seed = 0 ; seed < 1024; seed ++)
            if ( tab [seed][N-1] > max )
               max = tab [seed][N-1] ;        
        cout << "Case #" << testCase << ": "<< max << endl;
          
    }
        
    
    //cout << "done";

    
    
    return 0;
}
