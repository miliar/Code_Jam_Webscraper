#include<iostream>
#include<vector>

using namespace std;

int main(){
  int T;
  scanf("%d", &T);
  for(int tc = 1; tc <= T; ++tc){
    long long int ans = 0;
    int R,k,N,G[1001];
    long long int people[1001];
    int next[1001];

    scanf("%d%d%d", &R, &k, &N);

    for(int i = 0; i < N; ++i){
      scanf("%d", &G[i]);
    }

    for(int i = 0; i < N; ++i){
      long long int sum = 0;
      int cnt = 0;
      int n = i;

      while(sum<=k&&cnt<=N){
	sum += G[n++];
	++cnt;
	if( n >= N ) n = 0;
      }
      --n;
      if(n<0)n=N-1;
      people[i] = sum - G[n];
      next[i] = n;
    }

    int now = 0;
    for(int i = 0; i < R; ++i){
      ans += people[now];
      now = next[now];
    }

    printf("Case #%d: %lld\n", tc, ans );
  }
  return 0;
}
