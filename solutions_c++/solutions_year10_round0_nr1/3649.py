//13:46 2010-05-08 begin lsy
#include <cstdio>
#include <cstring>
using namespace std;

int main() {
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int T,n,k,i;
    scanf("%d",&T);
    for (i=1;i<=T;i++) {
        scanf("%d%d",&n,&k);
        printf("Case #%d: ",i);
        if ((k+1)%(1<<n)) printf("OFF\n"); else printf("ON\n");
    }
    return 0;
}

