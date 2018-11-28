#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <cmath>
#include <map>
#include <string.h>
#include <sstream>
#include <set>
using namespace std;
#define MAXN  10
#define INF  1000000000
typedef long long ll;
int N , M ;
string brd[MAXN];
int dxx[] = {0 ,0 , 1,-1, 1 , 1 , -1 ,-1};
int dyy[] = {1 ,-1, 0, 0, 1 ,-1 , 1  ,-1};
int cntr (int v , int u ,int dx , int dy) {
     int x = v , y = u;
     int cnt = 0;
     while ( x >= 0 && x < N && y >= 0 && y < N && (brd[x][y] == brd[v][u] || brd[x][y] == 'T') )
     {
           cnt ++; x = x + dx , y = y + dy;
     }
     return cnt; 
}
string calc () {
      int cnt = 0; 
      for (int i = 0; i < N; i ++ ) {
          for (int j = 0; j < N; j ++ ) {
              if (brd[i][j] == '.' ) continue;
              cnt ++;
              if (brd[i][j] == 'T') continue;
              string res = "X won";
              if (brd[i][j] == 'O') res = "O won";
              for (int l = 0; l < 8; l ++ ) {
                  int c = cntr (i , j , dxx[l] , dyy[l]) + cntr (i , j , dxx[l] * -1 , dyy[l] * -1);
                  //cout << c << " " << dxx[l] << " " << dyy[l] <<  endl;
                  if (c - 1 >= 4) return res;          
              }
          }    
      }  
      if (cnt == 16 ) return "Draw";
      return "Game has not completed";        
}
int main(){  
    freopen ("A-large.in" , "r" , stdin);
    freopen ("out.txt" , "w" , stdout);
    int T; cin >> T; int t = 1;
    while (T--) {   
       N = 4; 
       for (int i = 0; i < N; i ++ )
            cin >> brd[i];  
       cout <<"Case #"<<t<<": "<<calc () << endl;
       t ++;
    }         
//system("pause");              
return 0;
}

