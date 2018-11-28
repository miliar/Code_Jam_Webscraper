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

int tcase = 1;
int main(){
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    int t; scanf("%d", &t);
    
    while (t--){
          int n; scanf("%d", &n);
          vector <int> nextA; vector <int> nextB;
          queue <ii> q;
          int arr[4][105]; memset(arr, 0, sizeof arr);
          
          FOR (i, 0, n){
              char s[4]; int x;
              scanf("%s %d", &s, &x);
              
              if ( s[0] == 'O' ) nextA.push_back( x );
              else if ( s[0] == 'B' ) nextB.push_back( x );
              
              if ( s[0] == 'O' ) q.push( ii(0,x) );
              else if ( s[0] == 'B' ) q.push( ii(1,x) );
              
          }      
          
          int a = 1; int b = 1;
          int next_a = 1; int next_b = 1;
          int times = 0;
          int idx1 = 0; int idx2 = 0;
          
          while ( !q.empty() ){
                ii depan = q.front();
                int d = depan.first; int u = depan.second;
                //printf("yang mau dipencet = %d, %d\n", d, u);

                if ( idx1 + 1 <= nextA.size() ) next_a = nextA[idx1];
                //printf("next_a = %d, ", next_a);
                
                if ( idx2 + 1 <= nextB.size() ) next_b = nextB[idx2];
                //printf("next_b = %d\n", next_b);
                
                int dif_a = next_a - a;
                int dif_b = next_b - b;
                
                if ( d == 0 ){
                   times += abs(dif_a) + 1;
                   a = next_a;
                   idx1++;
                   if ( next_b > b ){
                      b = b + abs(dif_a) + 1;
                      if ( b > next_b ) b = next_b;     
                   }
                   else if ( next_b < b ){
                        b = b - abs(dif_a) - 1;
                        if ( b < next_b ) b = next_b;     
                   }
                   q.pop();  
                }
                
                else if ( d == 1 ){
                     times += abs(dif_b) + 1;
                     b = next_b;
                     idx2++;
                     if ( next_a > a ){
                        a = a + abs(dif_b) + 1;
                        if ( a > next_a ) a = next_a;     
                     }
                     else if ( next_a < a ){
                          a = a - abs(dif_b) - 1;
                          if ( a < next_a ) a = next_a;     
                     }
                     q.pop();    
                }
                
                //printf("dif_a = %d, dif_b = %d\n", dif_a, dif_b);
                
                //printf("a sudah di %d, b sudah di %d, times = %d\n", a, b, times);
                //puts("______________________________________");       
          }
          
          printf("Case #%d: ", tcase++);
          printf("%d\n", times);
    }

    return 0;
}
