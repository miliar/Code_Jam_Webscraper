#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;

int n,sum;

int solve(){
    sum=0;
    scanf("%d",&n);
    for (int i=1,temp;i<=n;i++) {
        scanf("%d",&temp);
        if (i!=temp) sum++;
    }
    return sum;
}

int main(){
    
    freopen("D.in","r",stdin);
    freopen("D.out","w",stdout);
    
    int test;
    scanf("%d",&test);
    for (int i=1;i<=test;i++) {
        int ans=solve();
        printf("Case #%d: %.6lf\n",i,double(ans));
    }
    
    
    return 0;
}
