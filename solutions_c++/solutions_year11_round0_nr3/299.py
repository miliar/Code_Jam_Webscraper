#include<stdio.h>
#include<algorithm>
using namespace std;

int s[1024];

int main()
{
    freopen("c.in", "r", stdin);
    freopen("c.out", "w", stdout);
    
    int T, tt, n, i, a;
    scanf("%d", &T);
    for(tt = 1; tt <= T; tt++){
        scanf("%d", &n);
        for(i = 0; i < n; i++) scanf("%d", &s[i]);
        sort(s, s+n);
        a = 0;
        for(i = 0; i < n; i++) a = a ^ s[i];
        if(a){
            printf("Case #%d: NO\n", tt);
            continue;
        }
        for(i = 1; i < n; i++) a += s[i];
        printf("Case #%d: %d\n", tt, a);
    }
    
    return 0;
}
