#include <iostream>
#include <algorithm>
#include <cmath>
#include <queue>
using namespace std;

int main(){
  int T;
  cin >> T;
  for (int iii=0; iii<T; iii++){
    int R,K,N;
    cin >> R >> K >> N;
    queue<int> g;
    int sum = 0;
    for (int i=0; i<N; i++){
      int a;
      cin >> a;
      g.push(a);
      sum += a;
    }
    if (sum <= K){
      printf("Case #%d: %d\n", iii+1, sum * R);
      continue;
    }

    int ans = 0;
    for (int r = 0; r < R; r++){
      int t=0;
      while (t+g.front() <= K){
        t+= g.front();
        ans += g.front();
        g.push(g.front());
        g.pop();
      }
    }

    printf("Case #%d: %d\n", iii+1, ans);
  }
}
