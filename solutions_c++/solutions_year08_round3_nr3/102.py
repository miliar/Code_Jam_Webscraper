#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <stack>
#include <queue>

#define f(x,y) for(int x=0; x<(y); ++x)
using namespace std;
long long int N, n, m, X, Y, Z, A[1005], R[1005], res[1005], result;
int main(){
  scanf("%d", &N);
  f(t, N){
    scanf("%d%d%d%d%d", &n, &m, &X, &Y, &Z);
    f(i, m) scanf("%d", &A[i]);
    f(i, n){
      R[i]=A[i%m];
      A[i%m] = ((X * A[i%m])%Z + (Y*(i+1))%Z)%Z;
    }
    result=0;
    for(int i=0; i<n; ++i){
      long long int temp=1;
      for(int j=0; j<i; ++j)
	if(R[j]<R[i]){
	  temp+=res[j];
	  temp%=1000000007;
	}
      temp%=1000000007;
      res[i]=temp;
      result+=temp;
      result%=1000000007;
      //printf("(%lld %lld)\n", R[i], temp);
    }
    printf("Case #%d: %lld\n", t+1, result);
  }
  return 0;
}
