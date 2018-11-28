#include<vector>
#include<string>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<cstdio>

using namespace std;

int a, n, m;
int teste, t;
int main() {
    int i, j;
    int aux;
    scanf("%d\n", &teste);
    for (t=0; t<teste; t++){
        scanf("%d %d %d\n", &n, &m, &a);
        for (i=1; i<=n; i++) {
           if (a%i==0) {
              if (a/i<=m) {
                 printf("Case #%d: 0 0 %d 0 0 %d\n", t+1, i, a/i);
                 break;
              }
           }
           else {
              if (a/i+1<=m) {
                 printf("Case #%d: 0 0 %d 1 %d %d\n", t+1, i, i-a%i, a/i+1);
                 break;
              }
           }
        }
        if (i > n)
           printf("Case #%d: IMPOSSIBLE\n", t+1);
    }
    return 0;    
}
