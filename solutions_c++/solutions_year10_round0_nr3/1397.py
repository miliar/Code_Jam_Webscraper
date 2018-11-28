#include<cstdio>
#include<cstring>

struct elem{
  long long s;
  int sig;
};

long long a[1005];
elem P[1005];

void precalc(int N,long long K){
  long long sump = 0;
  int last = 0;
  for (int i=0; i < N; ++i){
    while ((sump + a[last])<= K){
      sump+=a[last];
      last = (last + 1)%N;
    }
    P[i].s = sump;
    P[i].sig = last;
    sump-=a[i];
  }
}

int main(){

  int T;
  scanf("%d",&T);
  long long sum;
  int p;
  long long R,K;
  int N;
  
  for (int k=1; k <= T; ++k){
    printf("Case #%d: ",k);
    scanf("%lld %lld %d",&R,&K,&N);
    sum = 0;
    for (int i=0; i < N; ++i){
      scanf("%lld",&a[i]);
      sum+=a[i];
    }
    
    if (sum <= K){
	printf("%lld\n",R*sum);
    }
    else {
      precalc(N,K);      
      p = 0;
      sum = 0;
      for (int i=0; i < R; ++i){
	sum += P[p].s;
	p = P[p].sig;
      }
      printf("%lld\n",sum);
    }
    
  }
  return 0;
}