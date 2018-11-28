#include<iostream>
#include<cstdio>
using namespace std;
int main(){
    freopen("C-large.in","r",stdin);
    freopen("C-largeout.out","w",stdout);
    int T,N,a;
    scanf("%d",&T);
    for(int I=1;I<=T;I++){
        scanf("%d",&N);
        int p=0,m=100000000,total=0;
        while(N--){
            scanf("%d",&a);
            p^=a;
            total+=a;
            m=min(m,a);
        }
        if(p!=0) printf("Case #%d: NO\n",I);
        else printf("Case #%d: %d\n",I,total-m);
    }
    return 0;
}
