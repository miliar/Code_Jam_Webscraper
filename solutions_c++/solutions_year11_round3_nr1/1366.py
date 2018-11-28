#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <math.h>
using namespace std;

typedef pair<int,int> ii;

#define INF 2000000000
#define FOR(i,a,n) for(int i=a,_n=n; i<_n; i++)

int pr[] = {0,1,1};
int pc[] = {1,0,1};

char arr[60][60];
int r, c;

void cek (int x, int y){
     bool cond = true;
     FOR (i, 0, 3){
         int nr = x + pr[i];
         int nc = y + pc[i];
         
         if ( nr < 0 || nc < 0 || nr == r || nc == c ){
            cond = false;
            break;     
         }  
         if ( arr[nr][nc] != '#' ){
            cond = false;
            break;     
         }  
     }      
     
     if ( cond ){
        arr[x][y] = '/';
        arr[x][y+1] = '\\';
        arr[x+1][y] = '\\';
        arr[x+1][y+1] = '/';     
     }   
}

int main(){
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    int tcase = 1;
    int t; scanf("%d", &t);
    
    while (t--){
          scanf("%d %d", &r, &c);
          
          FOR (i, 0, r) scanf("%s", arr[i]);
          
          FOR (i, 0, r){
              FOR (j, 0, c){
                  if ( arr[i][j] == '#' ){
                     cek (i, j);     
                  }    
              }    
          }  
          
          bool covered = true;
          FOR (i, 0, r){
              FOR (j, 0, c){
                  if ( arr[i][j] == '#' ){
                     covered = false;
                     break;     
                  }    
              }    
          }  
          
          printf("Case #%d:\n", tcase++);
          if ( !covered ) puts ("Impossible");
          else{
               FOR (i, 0, r) printf("%s\n", arr[i]);     
          }  
    }
    
    return 0;
}
