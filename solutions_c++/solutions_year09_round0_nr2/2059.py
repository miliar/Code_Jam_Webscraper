#include <iostream>
#include <string>
#include <queue>
#include <vector>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <set>
#include <algorithm>
using namespace std;

int T, H, W;
int m[101][101];
char out[101][101];
char nextBasins = 'a';

char dfs(int lin, int col) {
   int minLin, minCol, MIN = 20000;

   if(out[lin][col]!='*') return out[lin][col];


//In case of a tie, water will choose the first direction with the lowest 
//altitude from this list: North, West, East, South.

   if(lin>0 && m[lin-1][col]<MIN ) {
      MIN = m[lin-1][col];
      minLin = lin-1;
      minCol = col;
   }
   if(col>0 && m[lin][col-1]<MIN ) {
      MIN = m[lin][col-1];
      minLin = lin;
      minCol = col-1;
   }
   if(col<W-1 && m[lin][col+1]<MIN ) {
      MIN = m[lin][col+1];
      minLin = lin;
      minCol = col+1;
   }
   if(lin<H-1 && m[lin+1][col]<MIN ) {
      MIN = m[lin+1][col];
      minLin = lin+1;
      minCol = col;
   }
   if(m[lin][col]<=MIN) {
      return out[lin][col] = nextBasins++;
   }
   else {
      return out[lin][col] = dfs(minLin, minCol);
   }
}


int main() {
    int i, j;
    
    cin >> T;
    for(int t=1; t<=T; t++) {
       cin >> H >> W;
       nextBasins = 'a';
       
       for(i=0; i<H; i++) {
          for(j=0; j<W; j++) {
             cin >> m[i][j];
             out[i][j] = '*';
          }
       }
       for(i=0; i<H; i++) {
          for(j=0; j<W; j++) {
             if(out[i][j]=='*') {
                dfs(i,j);
             }
          }
       }

       cout << "Case #" << t << ":" << endl;
       for(i=0; i<H; i++) {
          cout << out[i][0];
          for(j=1; j<W; j++) {
             cout << ' ' << out[i][j];
          }
          cout << endl;
       }
       
    }
    
}
