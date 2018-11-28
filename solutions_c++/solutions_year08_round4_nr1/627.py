#include <cstdio>
#include <string>
#include <algorithm>

using namespace std;

#define MAXN 10020
#define INF 100001

int sol[MAXN][2];
int gate[MAXN][2];
int m, v, inter, leaf;

int okreni(int n){
    if ( n == 1 ) return 0;
    return 1;
}

int solve(int x, int v);

void solve_step(int l, int r, int t, int &ret, int a){
       if ( t == 0 ){
           // OR
           if ( v == 0 ){
              // sum oba 0
              int sl = solve(l, 0);
              int sr = solve(r, 0);
              if ( sl != INF && sr != INF ){
                 if ( sl + sr + a < ret || ret == INF ) ret = sl + sr + a;
              }
           }
           if ( v == 1 ){
              // manji od 1
              int sl = solve(l, 1);
              int sr = solve(r, 1);
              if ( sl != INF && sl + a < ret ) ret = sl + a;
              if ( sr != INF && sr + a < ret ) ret = sr + a;
           }
        }
        else {
           // AND
           if ( v == 1 ){
              // sum oba 1
              int sl = solve(l, 1);
              int sr = solve(r, 1);
              if ( sl != INF && sr != INF ){
                 if ( sl + sr + a < ret || ret == INF ) ret = sl + sr + a;
              }
           }
           if ( v == 0 ){
              // manji od 0
              int sl = solve(l, 0);
              int sr = solve(r, 0);
              if ( sl != INF && sl + a < ret ) ret = sl + a;
              if ( sr != INF && sr + a < ret ) ret = sr + a;
           }             
        }
        
}

int solve(int x, int v){
     int &ret = sol[x][v];
     if ( ret != -1 ) return ret;
     ret = INF;
     
     if ( x < leaf ) {        
        int l = x * 2;
        int r = x * 2 + 1;
        
        int t = gate[x][0];
        solve_step(l, r, t, ret, 0);       
        
        if ( gate[x][1] ){
           t = okreni(t);
           solve_step(l, r, t, ret, 1); 
        }
           
     }
     else {
          if ( gate[x][0] == v ) ret = 0;
     }     
     
    // printf("%d %d %d\n", x, v, ret);
     
     return ret;
}

int main(){
    int tcc = 0, tc = 0;
    for(scanf("%d", &tc); tc; --tc){
                    memset(sol, -1, sizeof(sol));
                    scanf("%d %d", &m, &v);
                    inter = (m-1)/2;
                    leaf = (m+1)/2;
                    
                    for (int i = 1; i <= inter; i++)
                        scanf("%d %d", &gate[i][0], &gate[i][1]);
                    
                    for (int i = 1; i <= leaf; i++)
                        scanf("%d", &gate[inter + i][0]);
                    
                    int solution = solve(1, v);

                    if ( solution != INF )
                         printf("Case #%d: %d\n", ++tcc, solution);  
                    else
                         printf("Case #%d: IMPOSSIBLE\n", ++tcc);  
    }
    return 0;    
}
