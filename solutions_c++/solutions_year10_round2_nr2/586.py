#include <iostream>
#include <list>
#include <cstdio>

using namespace std;

const int chicken_max=50;

int pos[chicken_max];
int speed[chicken_max];
int N, K, B, T;

bool reachable(int n)
{
  return (pos[n] + speed[n] * T)>=B;
}

void solve(void)
{
  int count=0;
  int k=0;
  int target_chick;

  cin >> N >> K >> B >> T;

  for(int i=0; i<N; i++){
    cin >> pos[i];
  }
  for(int i=0; i<N; i++){
    cin >> speed[i];
  }

  k=0;
  target_chick = N-1;
  while(k < K && target_chick >= 0){
    if(reachable(target_chick)){
      for(int j=target_chick+1; j<N; j++){
	if(!reachable(j))count++;
      }
      k++;
    }
    target_chick--;
  }
  if(k < K){
    printf("IMPOSSIBLE\n");
  }
  else{
    printf("%d\n", count);
  }
}

int main()
{
  int C;

  cin >> C;

  for(int i=0; i<C; i++){
    printf("Case #%d: ", i+1);
    solve();
  }
}
