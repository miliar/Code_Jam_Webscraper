#include<stdio.h>
int gcd(int x,int y){
    int z;
    while (y!=0){
          z=x;
          x=y;
          y=z % x;
          }
    return x;
}
int abs(int x){
    if (x>0) return x; else return -x;
}
int main(){
    freopen("B-small-attempt2.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,i,j,n,a[4],b[3];
    scanf("%d",&t);
    for (i=1;i<=t;i++){
        scanf("%d",&n);
        for (j=1;j<=n;j++) scanf("%d",&a[j]);
        for (j=1;j<n;j++) b[j]=abs(a[j]-a[j+1]);
        if (n==3) b[1]=gcd(b[1],b[2]);//printf("%d\n",gcd(b[2],b[1]));
        for (j=1;;j++) if (b[1]*j>=a[2]) break; 
        printf("Case #%d: %d\n",i,b[1]*j-a[2]);
        }
    
}
