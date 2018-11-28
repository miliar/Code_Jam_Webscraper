#include<iostream>
#include<cstdio>
using namespace std;
int main(){
    freopen("D-large.in","r",stdin);
    freopen("D-lOut.out","w",stdout);
    int T,N,a;
    scanf("%d",&T);
    for(int I=1;I<=T;I++){
        double ans=0.0;
        scanf("%d",&N);
        for(int i=1;i<=N;i++){
            scanf("%d",&a);
            if(a!=i) ans++;
        }
        printf("Case #%d: %.6lf\n",I,ans);
    }
    return 0;
}
