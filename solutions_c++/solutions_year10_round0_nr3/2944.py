#include <cstdio>

int main(){
  int t;
  scanf("%d",&t);
  for(int p=0;p<t;p++){
    int r,k,n;
    int g[10];
    int ans=0;
    int point=0;
    scanf("%d%d%d",&r,&k,&n);
    for(int i=0;i<n;i++){
      scanf("%d",&g[i]);
    }
    for(int i=0;i<r;i++){
      int cap=0;
      int j;
      for(j=point;cap+g[j%n]<=k&&j-point<n;j++){
        cap+=g[j%n];
      }
      point=j;
      ans+=cap;
    }
    printf("Case #%d: %d\n",p+1,ans);
  }
}
