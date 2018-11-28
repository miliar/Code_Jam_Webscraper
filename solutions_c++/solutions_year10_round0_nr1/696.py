#include<iostream>
#include<algorithm>

using namespace std;

int main(){
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int t,i,n,k;
    scanf("%d",&t);
    for(i=1;i<=t;++i){
        printf("Case #%d: ",i);
        scanf("%d%d",&n,&k);
        if(k%(1<<n)==(1<<n)-1)printf("ON");else printf("OFF");
        printf("\n");
    }
}

