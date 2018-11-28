#include<cstdio>
int t,n,k,m;
int main(){
    freopen("A-large.in","r",stdin);
    freopen("output_snapper_large.out","w",stdout);
    scanf("%d",&t);
    for (int i=1; i<=t; i++){
          scanf("%d%d",&n,&k);
          m=1<<n;      
          printf("Case #%d: ",i);
          if (k%m==m-1) printf("ON\n");
          else printf("OFF\n");
    }
    return 0;    
}
