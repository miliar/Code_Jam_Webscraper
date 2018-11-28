#include <cstdio>

int main() {
    int t;
    scanf("%d",&t);
    for(int i=0;i<t;i++) {
        int n;
        int k;
        scanf("%d %d",&n,&k);
        int modded = k % ( 1 << n);
        bool on = (modded == (( 1 << n) - 1));
        printf("Case #%d: %s\n",i+1,on?"ON":"OFF");
    }
    return 0;
}
