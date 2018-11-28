#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;
typedef long long ll;
int gi[1010], sum[1010],next[1010];
int R, k, N, T;

ll go(){
  ll ans = 0;
  for(int i = 0; R > 0 && sum[i]; R--, i = next[i]){
    ans += sum[i];
  }
  return ans;
}
  
int main(){

  scanf("%d", &T);

  for(int ii = 1; ii <= T; ii++){
    scanf("%d%d%d", &R, &k, &N);
    for(int i = 0; i < N; i++)
      scanf("%d", gi+i);
    
    memset(sum, -1, sizeof(sum));
    
    int p = 0;
    while(sum[p] == -1){
      int pp = p;
      if(gi[p] > k){
	sum[p] = 0;
	next[p] = p;
	break;
      }
      sum[p] = gi[p];
      p = (p+1)%N;
      for( ; p != pp && sum[pp] + gi[p] <= k; p = (p+1)%N ){
	sum[pp] += gi[p];
      }
      //printf("%d -> %d sum:%d\n", pp, p, sum[pp]);
      next[pp] = p;
    }

    if(!sum[p]){ 
      printf("Case #%d: %lld\n", ii, go());
      continue;
    }

    ll ans = 0, csum = 0;
    for(int i = 0;  R > 0 && i != p; i = next[i], R--){
      ans += sum[i];
    }
    if(R == 0){
      printf("Case #%d: %lld\n", ii, ans);
      continue;
    }
    int num = 1;
    int pp = p;
    csum = sum[p];
    pp = next[p];
    for(; pp != p; num++, pp = next[pp] ){
      csum += sum[pp];
    }
    ans += (R / num) * csum;
    R %= num;
    for(int i = p; R > 0; i = next[i], R--){
      ans += sum[i];
    }
    printf("Case #%d: %lld\n", ii, ans);

  }
}
    
	
  
