#include<iostream>
#include<stdlib.h>
#include<stdio.h>
#include<cstring>
#include<string.h>
#include<algorithm>
#include<math.h>
#include<cmath>
using namespace std;

int main(){
    const int N = 1001;
    int T, R, k, n, a[2*N], next[N];
    long long s[N];
    scanf("%d",&T);
    for(int cs=1; cs<=T; cs++){
        scanf("%d%d%d",&R,&k,&n);
        for(int i=0; i<n; i++){ scanf("%d",&a[i]); a[n+i] = a[i]; }
        for(int i=0; i<n; i++){
            s[i] = 0;  next[i] = i;
            for(int j=i; j<=i+n-1; j++){
                if( s[i]+a[j]>k ){ next[i] = j%n; break; }
                s[i] += a[j];
            }
        }
        long long money = 0;
        for(int i=0,u=0; i<R; i++){ money += s[u]; u = next[u]; }
        printf("Case #%d: %lld\n",cs,money);
    }
    return 0;
}