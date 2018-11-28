#include <iostream>
using namespace std;

int C, N, K;
long long B, T, X[50], V[50];

int main() {
  cin >> C;
  for(int tc = 1; tc <= C; tc++) {
    int done = 0, obstacles = 0, S = 0;
    cin >> N >> K >> B >> T;
    for(int i = 0; i < N; i++) cin >> X[i];
    for(int i = 0; i < N; i++) cin >> V[i];
    for(int i = N-1; i >= 0 && done < K; i--) {
      if(X[i]+V[i]*T < B)
        obstacles++;
      else
        S += obstacles, done += 1;
    }
    if(done < K)
      cout << "Case #"<<tc<<": IMPOSSIBLE\n";
    else
      cout << "Case #"<<tc<<": "<<S<<"\n";
  }
  return 0;
}

