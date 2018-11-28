#include<cstdio>
#include<cmath>
int t,n,a[1010];
main(){
  scanf("%d",&t);
  for(int tt=1;tt<=t;tt++){
    scanf("%d",&n);
    for(int i=1;i<=n;i++)scanf("%d",&a[i]);
    double r=0;
    for(int i=1;i<=n;i++)if(a[i]){
      int j=i,cnt=0;
      while(a[j]){
        ++cnt;
        int k=a[j];
        a[j]=0;
        j=k;
      }
      if(cnt>1)r+=cnt;
    }
    printf("Case #%d: %.8lf\n",tt,r);
  }
}

