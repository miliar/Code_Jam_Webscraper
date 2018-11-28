#include<cstdio>
#include<algorithm>
using namespace std;

#define MAXN (1<<20)

int num[1000];
int memo[2][MAXN];

int main(){

  int T;
  scanf("%d", &T);

  for(int t = 1; t <= T; t++){
    
    int N, sum = 0, exsum = 0;
    scanf("%d", &N);
    fill(memo[0], memo[0] + MAXN, -1);
    fill(memo[1], memo[1] + MAXN, -1);
    memo[0][0] = 0;

    for(int i = 0; i < N; i++){
      scanf("%d", &num[i]);
      sum += num[i]; exsum ^= num[i];
    }

    if(exsum != 0){
      printf("Case #%d: NO\n", t);
      continue;
    }

    for(int i = 0; i < N; i++){
      for(int j = 0; j < MAXN; j++){
	memo[(i+1)%2][j] = memo[i%2][j];
      }
      int x = num[i];
      for(int j = 0; j < MAXN; j++){
	if(memo[i%2][j] < 0) continue;
	memo[(i+1)%2][j ^ x] = max(memo[i%2][j] + x, memo[i%2][j ^ x]);
      }
    }

    int res = 0;
    for(int i = 1; i < MAXN; i++){
      res = max(res, memo[N%2][i]);
    }
    printf("Case #%d: %d\n", t, res);      
  }

  return 0;
}
