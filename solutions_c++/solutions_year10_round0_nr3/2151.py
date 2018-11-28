#include<cstdio>

using namespace std;

int T,k,N,R,g[1000];
long long int ans;

int main(){
  int t;
  for(scanf("%d",&T),t=1;t<=T;t++){
    ans=0;
    scanf("%d %d %d",&R,&k,&N);
    for(int i=0;i<N;i++)
      scanf("%d",g+i);

    int tmp,i=0,f,a;
    for(int r=0;r<R;r++){
      tmp=0;
      f=-1;
      a=i;
      for(;f+=(a==i),k-tmp>=g[i]&&!f;){
	tmp+=g[i];
	i=(i+1)%N;
      }
      ans+=tmp;
    }
    printf("Case #%d: %lld\n",t,ans);
  }
}
