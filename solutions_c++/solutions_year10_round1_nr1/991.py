#include <cstdio>
#include <iostream>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <map>
#include <string>
#include <vector>

char board[50][50];

using namespace std;

void gravity(int N)
{
    for(int col=0; col<N; col++) {
        int p = N-1;
        for(int row = N-1; row>=0; row--) {
            char x = board[row][col];
            if(x != '.') {
                board[p][col] = x;
                p--;
            }
        }
        //cout << p << endl;
        for( ; p>=0; p--) {
            board[p][col] = '.';
        }
    }
}

int find_row(char c, int K, int N)
{
    int burst = 0;
    for(int i=0; i<N; i++) {
        int x = i;
        burst = 0;
        for(int j=0; j<N; j++) {
            int y = j;
            if( board[x][y]==c )
                burst ++;
            else
                burst = 0;
            if( burst >= K ) {
                board[x][y] += ('r' - 'R');
                return 1;
            }
        }
    }
    for(int i=0; i<N; i++) {
        int y = i;
        burst = 0;
        for(int j=0; j<N; j++) {
            int x = j;
            if( board[x][y]==c )
                burst ++;
            else
                burst = 0;
            if( burst >= K ) {
                board[x][y] += ('r' - 'R');
                return 1;
            }
        }
    }
    for(int i=-N+1; i<N; i++) {
        burst = 0;
        int lo = i;
        int hi = N-1+i;
        if( lo<0 ) lo = 0;
        if( hi>(N-1) ) hi = N-1;
        for(int j=lo; j<=hi; j++) {
            int x = j;
            int y = j-i;
            //cout << "x " << x << "y " << y << " : " << board[x][y] << endl;
            if( board[x][y]==c )
                burst ++;
            else
                burst = 0;
            if( burst >= K ) {
                board[x][y] += ('r' - 'R');
                return 1;
            }
        }
    }
    for(int i=0; i<N; i++) {
        burst = 0;
        for(int j=0; j<=i; j++) {
            int x = j;
            int y = i-j;
            if( board[x][y]==c )
                burst ++;
            else
                burst = 0;
            if( burst >= K ) {
                board[x][y] += ('r' - 'R');
                return 1;
            }
        }
    }
    for(int i=N; i<((N<<1)-1); i++) {
        burst = 0;
        for(int j = i-(N-1); j<=(N-1); j++) {
            int x = j;
            int y = i-j;
            if( board[x][y]==c )
                burst ++;
            else
                burst = 0;
            if( burst >= K ) {
                board[x][y] += ('r' - 'R');
                return 1;
            }
        }
    }
    
    return 0;
}

char test[7][8] =
{
".......",
"...RBBB",
"....RBB",
".....RB",
".....RR",
"....RBB",
"...RBBB"
};

int main()
{
    int T;
    
    cin >> T;

/*    int N = 7, K=4;
    for(int j=N-1; j>=0; j--) {
        for(int h=0; h<N; h++) {
            board[h][j] = test[N-1-j][h];
        }
    }
    gravity(N);  
    int is_red = find_row('R', K, N); 
    for(int j=0; j<N; j++) {
        for(int h=0; h<N; h++) {
            //h--;
            cout << board[j][h];
        }
        cout << endl;
    }
  */  
    for(int i=1; i<=T; i++) {
        int N, K;
        cin >> N;
        cin >> K;
        
        for(int j=N-1; j>=0; j--) {
            for(int h=0; h<N; h++) {
                cin >> board[h][j];
            }
        }
        
        //rotate    
        gravity(N);  
        int is_red = find_row('R', K, N); 
        int is_blu = find_row('B', K, N); 
        /*for(int j=0; j<N; j++) {
            for(int h=0; h<N; h++) {
                //h--;
                cout << board[j][h];
            }
            cout << endl;
        }*/
        cout << "Case #" << i << ": ";
        if( is_red && is_blu )
            cout << "Both" << endl;
        else if( is_red )
            cout << "Red" << endl;
        else if( is_blu )
            cout << "Blue" << endl;
        else
            cout << "Neither" << endl;
    }
    
//    cin >> T;
    return 0;
}
