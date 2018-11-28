#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

int t,tt,n,num[1010];

int main(){
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
    scanf("%d",&t);
    while( t -- ){
        scanf("%d",&n);
        for(int i=1;i<=n;i++)
            scanf("%d",&num[i]);
        int ans = 0;
        for(int i=1;i<=n;i++)
            if(num[i] != i)
                ans ++;
        printf("Case #%d: %.6f\n",++tt,(double)ans);
    }
    return 0;
}
