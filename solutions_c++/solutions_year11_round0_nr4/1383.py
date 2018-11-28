#include <cstdio>
int main() {
    int j;
    scanf("%d",&j);
    for(int i=1;i<=j;i++) {
        int n,c=0;
        scanf("%d",&n);
        for(int j=1;j<=n;j++) {
            int a;
            scanf("%d",&a);
            if (a!=j) c++;
        }
        printf("Case #%d: %d.000000\n",i,c);
    }
}
