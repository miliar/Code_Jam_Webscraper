#include<stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

int num[1010];
int n,t,tt;

int main(){
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    scanf("%d",&t);
    while( t -- ){
        scanf("%d",&n);
        for(int i=1;i<=n;i++)
            scanf("%d",&num[i]);
        sort(num + 1, num + 1 + n);
        int ans = 0;
        int sum = 0;
        for(int i=1;i<=n;i++){
            ans ^= num[i];
            sum += num[i];
        }
        if(ans != 0)
            printf("Case #%d: NO\n",++tt);
        else
            printf("Case #%d: %d\n",++tt,sum - num[1]);
    }
    return 0;
}

