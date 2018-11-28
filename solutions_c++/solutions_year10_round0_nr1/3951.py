#include <iostream>

using namespace std;

int main() {
    int t, n, k;
    int l;
    scanf("%d\n",&t);
    for(int i=1;i<=t;i++)
    {
        scanf("%d %d",&n,&k);
        l = (k+1) / (1<<n);
        if(l != 0 && l*(1<<n) - 1 == k)  {
            printf("Case #%d: ON\n",i);
        }  else {
            printf("Case #%d: OFF\n",i);
        }
    }
    return 0;
}
