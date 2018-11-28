#include <cstdio> 
using namespace std;

int main(){
    int t,n,k,suf;

    scanf("%d", &t);
    for(int i=1; i<=t; ++i){
        scanf("%d%d", &n, &k);
        suf = (1<<n) - 1;
        if((k & suf)  == suf)
            printf("Case #%d: ON\n", i);
        else
            printf("Case #%d: OFF\n", i);
    }
}

