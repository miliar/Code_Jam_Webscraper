#include<cstdio>
int main(){
  int test,x[77],v[77];
  scanf("%d",&test);
  int testi;
  for(testi=1;testi<=test;++testi){
    int n,k,b,t;
    scanf("%d%d%d%d",&n,&k,&b,&t);
    int i;
    for(i=0;i<n;++i){
      scanf("%d",x+i);
      x[i]=b-x[i];
    }
    for(i=0;i<n;++i)scanf("%d",v+i);
    printf("Case #%d: ",testi);
    int cnt=0;
    for(i=0;i<n;++i)
      if(x[i]<=t*v[i])++cnt;
    if(cnt<k){
      puts("IMPOSSIBLE");
      continue;
    }
    cnt=0;
    int j;
    for(i=n-1;i>=0&&k;--i){
      if(x[i]<=t*v[i]){
        --k;
        for(j=n-1;j>i;--j)
          cnt+=x[j]>t*v[j];
      }
    }
    printf("%d\n",cnt);
  }
  return 0;
}