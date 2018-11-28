#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

int n;

int main(){
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    int t,ans,d;
    scanf("%d",&t);
    for (int cas = 1; cas <= t; ++cas){
        scanf("%d",&n);
        ans = 0;
        for (int i = 1; i <= n; ++i){
            scanf("%d",&d);
            if( d != i ) ++ans;
        }
        printf("Case #%d: %.6f\n",cas,0.0+ans);
    }
    return 0;
}
