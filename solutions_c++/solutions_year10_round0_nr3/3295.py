#include<stdio.h>
long long ans;
int qq,t,q,n,k,r,ansi,g[1005];
int main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&t);
    for (int j=0;j<t;j++){
        ans=0;
        scanf("%d%d%d",&r,&k,&n);
        for (int w=0;w<n;w++)
          scanf("%d",&g[w]);
        q=0;
        for (int i=0;i<r;i++){
            ansi=0;
            qq=q;
            while (ansi+g[q]<=k){
                  if ((qq==q)&&(ansi!=0)) break;
                  ansi=ansi+g[q];
                  q++;
                  q=q%n;
                  }
            ans=ans+ansi;
            }
        printf("Case #%d: %d\n",j+1,ans);
        }
   return 0;
}      
