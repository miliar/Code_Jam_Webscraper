#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
int main(){
  long long t;
  scanf("%lld", &t);
  for(long long i=0; i<t; i++){
    long long r, K, n;
    scanf("%lld%lld%lld", &r, &K, &n);
    long long A[1099];
    long long Cost[1099];
    long long Next[1099];
    bool Visit[1099];
    long long Suma=0;
    for(long long k=0; k<n; k++){
      scanf("%lld", &A[k]);
      Cost[k]=0 ;
      Next[k]=-1;
      Visit[k]=0;
      Suma+=A[k];
    }
    for(long long k=0; k<n; k++){
      long long j=k;
      while(Cost[k]+A[j]<=K && Cost[k]+A[j]<=Suma){
	Cost[k]+=A[j];
	j++;
	j%=n;
      }
      Next[k]=j;
    }
    /*for(int k=0; k<n; k++){
      printf("k:%d Cost: %d Next: %d A: %d\n", k, Cost[k], Next[k], A[k]);
      }*/
    long long t=0;
    long long SumaC=0;
    long long Ile=0;
    while(!Visit[t]){
      Visit[t]=1;
      SumaC+=Cost[t];
      t=Next[t];
      Ile++;
      if(Ile==r)
	break;
    }
    long long start_c=t;
    if(Ile==r){
      printf("Case #%lld: %lld\n", i+1, SumaC);
    }else{
      t=0;
      long long wynik=0;
      while(t!=start_c){
	wynik+=Cost[t];
	SumaC-=Cost[t];
	t=Next[t];
	r--;
	Ile--;
      }
      wynik+=SumaC*(r/Ile);
      r=r-((r/Ile)*Ile);
      t=start_c;
      while(r>0){
	wynik+=Cost[t];
	t=Next[t];
	r--;
      }
      printf("Case #%lld: %lld\n", i+1, wynik);
    }
  }
  return 0;
}
