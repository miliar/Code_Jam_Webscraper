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
#include <iostream>
using namespace std;

typedef pair<int,int> ii;

#define INF 2000000000
#define FOR(i,a,n) for(int i=a,_n=n; i<_n; i++)

int main(){
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    int tcase = 1;
    int t; scanf("%d", &t);
    
    while (t--){
          double WP[105];
          double OWP[105];
          double OOWP[105];
          char arr[105][105];
          int n; scanf("%d", &n);
          
          FOR (i, 0, n) scanf("%s", arr[i]);
          
          FOR (i, 0, n){
              int win = 0, lose = 0, match = 0;
              FOR (j, 0, n){
                  if ( arr[i][j] == '1' ) win++;
                  else if ( arr[i][j] == '0' ) lose++;
                  if ( arr[i][j] == '1' || arr[i][j] == '0' ) match++;
              } 
              //printf(">> %d %d\n", win, match);
              WP[i] =  (double)win/match;   
          }  
          
          
          FOR (i, 0, n){
              double sum = 0;
              int opp = 0;
              FOR (j, 0, n){
                  int win = 0, match = 0;
                  if ( arr[i][j] != '.' ){
                     opp++;
                     FOR (k, 0, n){
                         if ( k == i ) continue;
                         if ( arr[j][k] == '1' ) win++;
                         if ( arr[j][k] != '.' ) match++;   
                     }  
                     sum += ((double)win/match);    
                  }  
                  
              }    
              OWP[i] = ( sum/opp );
          }  
           
          
          FOR (i, 0, n){
              double sum = 0;
              int opp = 0;
              FOR (j, 0, n){
                  if ( arr[i][j] != '.' ){
                     opp++;
                     sum += OWP[j];        
                  }    
              }    
              OOWP[i] = (sum/opp);
          }
          
          printf("Case #%d:\n", tcase++);
          
          FOR (i, 0, n){
              double hasil = (WP[i]*0.25) + (OWP[i]*0.50) + (OOWP[i]*0.25);
              cout.precision(12);
              cout << hasil << endl;   
          }
    }

    return 0;
}
