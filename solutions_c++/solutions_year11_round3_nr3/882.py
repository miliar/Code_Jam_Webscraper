#include<stdio.h>
#include<algorithm>

int main(){
    int T,cnt,n,l,h,i,player[101],ans,m,j;
    cnt = 0;
    scanf("%d",&T);
    while(T--){
        cnt++;
        ans = 0;
        scanf("%d %d %d",&n,&l,&h);
        for(i=0;i<n;i++) scanf("%d",&player[i]);
        for(i=l;i<=h;i++){
            m = 0;
            for(j=0;j<n;j++)
                if(player[j]%i != 0 && i%player[j] != 0){
                    m = 1;
                    break;
                }
            if(!m){
                ans = i;
                break;
            }
        }
        printf("Case #%d: ",cnt);
        if(!ans) printf("NO\n");
        else printf("%d\n",ans);
    }
    return 0;
}
