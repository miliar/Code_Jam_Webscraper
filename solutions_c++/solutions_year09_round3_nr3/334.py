#include<algorithm>
#include<cstdio>
using namespace std;
bool vis[111];
int p,q,a[777];
int fun(){
  memset(vis,0,sizeof(vis));
  int ans=0,i,j;
  for(i=0;i<q;++i){
    vis[a[i]]=1;
    for(j=a[i]-1;j&&!vis[j];--j)++ans;
    for(j=a[i]+1;j<=p&&!vis[j];++j)++ans;
  }
  return ans;
}
int main(){
  int test;
  scanf("%d",&test);
  int testi;
  for(testi=1;testi<=test;++testi){
    scanf("%d%d",&p,&q);
    int i;
    for(i=0;i<q;++i)
      scanf("%d",a+i);
    int minn=0x7fffffff;
    do{
      minn=min(minn,fun());
    }while(next_permutation(a,a+q));
    printf("Case #%d: %d\n",testi,minn);
  }
  return 0;
}