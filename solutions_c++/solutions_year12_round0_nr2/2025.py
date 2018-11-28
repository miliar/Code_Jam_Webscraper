#include <cstdio>
using namespace std;

int main()
{
    int n;
    scanf("%d", &n);
    for(int i = 1; i <= n; ++ i){
        int m, s, c, w=0;
        scanf("%d %d %d", &m, &s, &c);
        int d = c<<1;
        while(m --){
            int a;
            scanf("%d", &a);
            a -= c;
            if(a >= d-2 && a >= 0) ++ w;
            else if((a == d-4 || a == d-3) && s && a >= 0){
                -- s; ++ w;}
        }
        printf("Case #%d: %d\n", i, w);
    }
}
