#include <cstdlib>
#include <iostream>
#include <deque>
#include <queue>
#include <algorithm>
#include <vector>
#include <string>



using namespace std;


int kierunki [101][101];
int sinks [101][101];
int H, W;
int di[4] = { -1, 0, 0, 1};
int dj[4] = { 0, -1, 1, 0};

void dfs ( int curi, int curj, int n ) {
    //if ( curi < 0 || curi >= H || curj < 0 || curj >= W)
     //   return;
    sinks[curi][curj ] = n;
    //cerr << curi << ", " << curj << " " << n << endl;
    for ( int i = 0; i < 4; i ++) {
        int ni, nj;
        ni = curi + di[i];
        nj = curj + dj[i];
        if ( ni < 0 || ni >= H || nj < 0 || nj >= W)
            continue;
      //  cerr << "   ... " << kierunki[ni][nj] << endl;
        if ( kierunki [ni][nj] + i == 3)
            dfs ( ni, nj, n);
    }
        
}

int main(int argc, char *argv[])
{
    int T;
    cin >> T;
  
    
    
    for ( int caseno = 1; caseno <= T; caseno ++) {
        
        cin >> H >> W;    
        
        int mapa [ 101][101];
        
        for ( int i = 0; i < H; i ++)
            for ( int j = 0 ; j < W; j ++) {
                int temp ;
                cin >> temp;
                mapa[i][j] = temp;
                sinks[i][j] = -1;
                kierunki[i][j] = -1;
            }
                
        // ustalic kierunki
        for ( int i = 0; i < H; i ++) {
            for ( int j = 0 ; j < W; j ++) {  
                int minr = 0;
                int mink = 5;
                
                for ( int kier = 0; kier < 4; kier ++) {
                    int ni, nj;
                    ni = i + di[kier];
                    nj = j + dj[kier];
                    if ( ni >= 0 && ni < H && nj >= 0 && nj < W)
                        if ( mapa [ni][nj] - mapa[i][j] < minr ) {
                            minr =  mapa [ni][nj] - mapa[i][j];
                            mink = kier;
                        }   
                }
                kierunki[i][j] = mink;
        //        cerr << kierunki[i][j] << " " ;
            }
            cerr << endl;
        }
        
        // od kazdego sinka startujemy bfs
        int cursink = 0;
         for ( int i = 0; i < H; i ++) {
            for ( int j = 0 ; j < W; j ++) {
                if ( kierunki [i][j] == 5)
                    dfs ( i, j, cursink ++);
            }
        }
        
        
        vector < char >  sink2colorMap ( cursink, -1);
        
        // malujemy
        char curkolor = 'a';
        
         for ( int i = 0; i < H; i ++)
            for ( int j = 0 ; j < W; j ++) {        
                // napotykamy sink
                int sink = sinks[i][j];
                if ( sink2colorMap [sink] == -1)
                    sink2colorMap[sink] = curkolor++;  
                    
            }
          
            
        // output
        cout << "Case #" << caseno << ":" << endl;
        for ( int i = 0; i < H; i ++) {
            for ( int j = 0 ; j < W; j ++) {
                if ( j > 0) cout << " ";
                
                cout << sink2colorMap [ sinks[i][j] ];
            }
            cout << endl;
        }   
        
    }
    
    return EXIT_SUCCESS;
}
