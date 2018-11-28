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
          int n; scanf("%d", &n);
          int arr[1005];
          
          int sum = 0;
          FOR (i, 0, n){ scanf("%d", &arr[i]); sum += arr[i]; }
          
          printf("Case #%d: ", tcase++);
          int x = arr[0];
          FOR (i, 1, n) x ^= arr[i];
          if ( x != 0 ) puts("NO");
          
          else{
              int min_value = INF;
              FOR (i, 0, n) if ( arr[i] < min_value ) min_value = arr[i];
              printf("%d\n", sum - min_value);
          }     
    }
    
    return 0;
}
