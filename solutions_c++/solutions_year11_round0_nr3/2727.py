#include <cstdio>
using namespace std;

int T,N;
int v[1024];
long long int sum;
int menor;
int x;

int main(){

  scanf("%d",&T);
  for(int t=0;t<T;t++){
    scanf("%d",&N);
    x=0;
    sum=0;
    menor=0x3fffffff;
    for(int i=0;i<N;i++){
      scanf("%d",v+i);
      x^=v[i];
      if(v[i]<menor) menor=v[i];
      sum+=v[i];
    }
    if(x==0){
      printf("Case #%d: %lld\n",t+1,sum-menor);
    } else {
      printf("Case #%d: NO\n",t+1);
    }
  }

  return 0;
}
