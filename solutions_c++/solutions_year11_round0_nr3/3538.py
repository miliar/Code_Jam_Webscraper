#include <cstdlib>
#include <algorithm>
#include <limits.h>
#include <stdio.h>
using namespace std;
int main() {
    freopen("/home/gaia/Downloads/in","r",stdin);
    freopen("/home/gaia/Downloads/out","w",stdout);
    int T,cas=1;
    scanf("%d",&T);
    while(T--){
        int n;
        scanf("%d",&n);
        int sta=0;
        int ans=INT_MAX;
        int sum=0;
        for(int i=0;i<n;i++){
            int x;
            scanf("%d",&x);
            sta^=x;
            ans=min(ans,x);
            sum+=x;
        }
        printf("Case #%d: ",cas++);
        if(sta)puts("NO");
        else printf("%d\n",sum-ans);
    }
    return 0;
}

