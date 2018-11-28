#include<stdio.h>
#include<stdlib.h>
int cas,n,inp,cnt;
int main(){
    scanf("%d",&cas);
    for(int iii=0;iii<cas;iii++){
        scanf("%d",&n);
        cnt=0;
        for(int i=1;i<=n;i++){
            scanf("%d",&inp);
            if(inp!=i)cnt++;
        }
        printf("Case #%d: %d.000000\n",iii+1,cnt);
    }
    scanf(" ");
    return 0;
}
        
