#include <iostream>
#include <cstdio>
#include <memory.h>
#include <algorithm>
using namespace std;

long long dm[2000000];
int a[10000];

void solve(){
     int L, n, c;
     long long t;
     long long global=0;
     scanf("%d%lld%d%d", &L, &t, &n, &c);
     for (int i=0; i<c; ++i)
         scanf("%d", &a[i]);
     for (int i=0; i<c; ++i)
         for (int k=0; c*k+i<n; ++k)
             global+=(dm[c*k+i]=a[i]*2);
     long long ans=0;
     int cur=0;
     while (ans+dm[cur]<t && cur<n)
          ans+=dm[cur++];
     if (cur!=n){
          dm[cur]=(ans+dm[cur]-t);
          sort(dm+cur, dm+n);
          reverse(dm+cur, dm+n);
          while (L && cur<n){
              global-=dm[cur++]/2;
              L--;
          }
     }
     printf("%lld\n", global);
}

int main(){
    freopen("B-small-attempt1.in", "r", stdin);
    freopen("B.out", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i=0; i<t; ++i){
        printf("Case #%d: ", i+1);
        solve();
    }
}
