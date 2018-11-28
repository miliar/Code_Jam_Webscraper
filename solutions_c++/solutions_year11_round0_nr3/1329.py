#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;

int solve(){
    int n;
    scanf("%d",&n);
    int sum=0,MIN=100000000,s=0;
    for (int i=1;i<=n;i++) {
        int temp;
        scanf("%d",&temp);
        s+=temp;
        sum^=temp,MIN=min(temp,MIN);
    }
    if (sum!=0) return -1; else return s-MIN;
}

int main(){
    
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    
    int test;
    scanf("%d",&test);
    for (int i=1;i<=test;i++) {
        int ans=solve();
        printf("Case #%d: ",i);
        if (ans==-1) printf("NO\n"); else printf("%d\n",ans);
    }
    
    
    return 0;
}
