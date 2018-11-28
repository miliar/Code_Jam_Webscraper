#include <iostream>
#include <cstdio>

using namespace std;

int l, p, c;

int main(){
    int t;
    freopen("B.in", "r",stdin);
    freopen("B.txt","w",stdout);
    scanf("%d",&t);
    for (int i = 0; i < t; ++i){
        printf("Case #%d: ",i + 1);
        scanf("%d%d%d",&l, &p, &c);
        int div = p / l;
        if (p % l) div++;
        int tot = 0;
        __int64 e = 1;
        while (e < div){
            e = e * c;
            tot++;
        }
        
        //printf("div = %d tot = %d e = %I64d\n", div, tot, e);
        
        e = 1;
        int s = 0;
        while (e < tot){
           e = e * 2;
           s++;
        }
        printf("%d\n",s);
    }
    return 0;
}
