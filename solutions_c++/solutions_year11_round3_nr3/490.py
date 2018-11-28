#include <iostream>
#include <cstdio>
#include <memory.h>
using namespace std;

int a[10000];

void solve(){
     int n, l, h;
     scanf("%d%d%d", &n, &l, &h);
     for (int i=0; i<n; ++i)
         scanf("%d", &a[i]);
     for (int i=l; i<=h; ++i){
         bool good=true;
         for (int j=0; j<n; ++j)
             good&=((a[j]%i==0)||(i%a[j]==0));
         if (good){
            printf("%d\n", i);
            return;
         }
     }
     printf("NO\n");
}

int main(){
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C.out", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i=0; i<t; ++i){
        printf("Case #%d: ", i+1);
        solve();
    }
}
