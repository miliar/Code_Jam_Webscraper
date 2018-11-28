#include <cstdio>

int main(){
    int t;
    scanf("%d", &t);
    
    for (int i = 1; i <= t; i ++){
         int n, k;
         scanf("%d %d", &n, &k);
         int N = 1 << n;
         printf("Case #%d: ", i);
         if (k % N == N - 1)
              printf("ON\n");
         else
              printf("OFF\n");
    }
    return 0;
}
