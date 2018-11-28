#include <cstdio>
#include <cstring>

int n,m,l,c,p,y,x;
long long t;
int main() {
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    int tt,test,i,k,j;
    scanf("%d",&test);
    for (tt = 1; tt<=test; tt++) {
        scanf("%d %d %d",&l,&p,&c);
        t = l * c; x= 1;
        while (t<p) t*=c,x++;
        y=0;
        t=1;
        while (t<x) t*=2,y++;
        printf("Case #%d: %d\n",tt,y);
    }
    return 0;
}
