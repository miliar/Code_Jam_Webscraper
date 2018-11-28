#include<cstdio>
#include<algorithm>

using namespace std;

int main(){
    int Z; scanf("%d",&Z);
    for(int z=1;z<Z+1;z++){
        int N,mini,ksor=0,suma=0,n;
        mini=1000001;
        scanf("%d",&N);
        while(N--){
            scanf("%d",&n);
            ksor= ksor^n;
            suma+=n;
            mini=min(mini,n);
        }
        if(ksor==0)
            printf("Case #%d: %d\n",z,suma-mini);
        else
            printf("Case #%d: NO\n",z);
    }
}
