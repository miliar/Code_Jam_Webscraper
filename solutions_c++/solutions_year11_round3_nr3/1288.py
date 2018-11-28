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

int main(){
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    int tcase = 1;
    int t; scanf("%d", &t);
    
    while (t--){
          int arr[10005];
          int N, L, H; scanf("%d %d %d", &N, &L, &H);
          
          FOR (i, 0, N) scanf("%d", &arr[i]);
          
          int x = -1;
          for (int i=L; i<=H; i++){
              bool cond = true;
              FOR (j, 0, N){
                  if ( i%arr[j] != 0 && arr[j]%i != 0 ){
                     cond = false;
                     break;     
                  }    
              } 
              if ( cond ){
                 x = i;
                 break;     
              }   
          }  
          
          printf("Case #%d: ", tcase++);
          if ( x == -1 ) puts("NO");
          else printf("%d\n", x);    
    }

    return 0;
}
