#include <cstdio>
#include <cstring>


int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int q,n,k,i,j;
    scanf("%d",&q);
    for(int test=1;test<=q;test++){
        scanf("%d%d",&n,&k);
        if((k&((1<<n)-1))==(1<<n)-1)
            printf("Case #%d: ON\n",test);
        else
            printf("Case #%d: OFF\n",test);
    }

    return 0;
}
