#include<stdio.h>
#include<algorithm>
using namespace std;

int main()
{
    freopen("c.in", "r", stdin);
    freopen("c.out", "w", stdout);
    
    int T, tt, a1, a2, b1, b2, a, b;
    long long aa, bb, tot;
    
    scanf("%d", &T);
    for(tt=1; tt<=T; tt++){
        printf("Case #%d: ", tt);
        
        scanf("%d%d%d%d", &a1, &a2, &b1, &b2);
        tot=0;
        for(a=a1; a<=a2; a++)
            for(b=b1; b<=b2; b++){
                aa=a;
                bb=b;
                if(aa>bb) swap(aa, bb);
                if((2*aa+bb)*(2*aa+bb)<5*bb*bb) tot++;
            }
        printf("%I64d\n", tot);
    }
    
    return 0;
}
