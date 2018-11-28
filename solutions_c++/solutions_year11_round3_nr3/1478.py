#include <stdio.h>
int num[10000],n;
int check(int d){
    int j;
    for(j=0;j<n;j++) if(num[j]%d&&d%num[j])  return 0;
    return 1;
}
main(){
       freopen("Cout.txt","w",stdout);
       int T,l,h,i,TC=1;
    scanf("%d",&T);   
    while(T--){
        scanf("%d%d%d",&n,&l,&h);
        for(i=0;i<n;i++) scanf("%d",&num[i]);
        for(i=l;i<=h;i++){
            if(check(i)) break;
        }
        if(i==h+1) printf("Case #%d: NO\n",TC++);
        else printf("Case #%d: %d\n",TC++,i);
    }
    return 0;
}
