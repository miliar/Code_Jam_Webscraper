#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

int main()
{
    int t,cnt,i,n,value,sum,ans,mmin;
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    scanf("%d",&t);
    for(cnt=1;cnt<=t;cnt++){
        scanf("%d",&n);
        for(i=0,sum=0,mmin=10000000;i<n;i++){
            scanf("%d",&value);
            if(value<mmin)mmin=value;
            if(i==0)ans=value;
            else ans^=value;
            sum+=value;
        }
        printf("Case #%d: ",cnt);
        if(ans){
            printf("NO\n");
            continue;
        }
        else printf("%d\n",sum-mmin);
    }
    return 0;
}