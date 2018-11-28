#include<stdio.h>
int t,n,ans;
int a[20];
int main(){
  freopen("c.in","r",stdin);
  freopen("c.out","w",stdout);
  int i,s,j,ca=0;
  int sum1,sum2,k1,k2;
  scanf("%d",&t);
  while (t--){
    ca++;
    scanf("%d",&n);
    for (i=1;i<=n;i++) scanf("%d",&a[i]);
    s=(1<<n);
    ans=-1;
    for (i=1;i<s-1;i++){
      k1=0;k2=0;
      sum1=0;sum2=0;
      for (j=0;j<n;j++)
        if ((i&(1<<j))>0){
          k1=k1^a[j+1];
          sum1+=a[j+1];
        }
        else{
          k2=k2^a[j+1];
          sum2+=a[j+1];
        }
      if (k1==k2){
        if (ans<sum1) ans=sum1;
        if (ans<sum2) ans=sum2;
      }
    }
    if (ans<0) printf("Case #%d: NO\n",ca);
    else printf("Case #%d: %d\n",ca,ans);
  }
  return 0;
}
