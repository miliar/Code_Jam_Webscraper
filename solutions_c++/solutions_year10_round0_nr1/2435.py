#include"stdio.h"
#include"string.h"
#include"iostream"
#include"algorithm"
using namespace std;
int t,n,k;
int main(){
    int x;
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        scanf("%d%d",&n,&k);
        x=1<<n;
        printf("Case #%d: ",i);
        if(k%x==x-1) printf("ON\n");
        else printf("OFF\n");
    }
    return 0;
}
