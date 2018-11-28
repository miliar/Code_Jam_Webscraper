#include <iostream>
#include <algorithm>
#define MAXN 1000
using namespace std;
int candy[MAXN];
int main(){
    int T, N, xr, maxx, tc = 1;
    scanf("%d", &T);
    while(T--){
           maxx = 0, xr = 0;    
           scanf("%d", &N);
           for(int i = 0; i < N; i++)
               scanf("%d", &candy[i]);
           sort(candy, candy + N);
           for(int i = N - 1; i >= 1; i--){
                   xr = xr ^ candy[i];
                   maxx += candy[i];
           }
           if(xr == candy[0])
                 printf("Case #%d: %d\n", tc, maxx);
           else 
                 printf("Case #%d: NO\n", tc);     
           tc++;
    }
    return 0;
}

