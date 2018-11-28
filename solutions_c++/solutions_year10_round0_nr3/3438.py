#include<stdio.h>
int main(){
    freopen("C-small-attempt1.in","r",stdin);
    freopen("out.txt","w",stdout);
    int g[10],j,i,t,r,k,n,l,temp,ans,tmp;
    scanf("%d",&t);
    for (i=1;i<=t;i++){
        scanf("%d%d%d",&r,&k,&n);ans=0;
        for (j=0;j<n;j++) scanf("%d",&g[j]);
        for (l=0,j=1;j<=r;j++){
            temp=g[l];tmp=l;l++;l%=n;
            while (temp+g[l]<=k && tmp!=l) {temp+=g[l];l++;l%=n;}
            ans+=temp;
            }
        printf("Case #%d: %d\n",i,ans);
        }
}
