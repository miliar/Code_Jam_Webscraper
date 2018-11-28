#include<stdio.h>
#include<stdlib.h>
int n,inp,rox,mii,cas,sum;
int main(){
    scanf("%d",&cas);
    for(int iii=0;iii<cas;iii++){
        scanf("%d",&n);
        mii=2147483647;
        rox=0;
        sum=0;
        for(int i=0;i<n;i++){
            scanf("%d",&inp);
            rox=rox^inp;
            sum+=inp;
            if(inp<mii)mii=inp;
        }
        if(rox)printf("Case #%d: NO\n",iii+1);
        else printf("Case #%d: %d\n",iii+1,sum-mii);
    }
    scanf(" ");
    return 0;
}
