#include <iostream>

using namespace std;

int main() {
  int T; cin >> T;
  for(int tc = 1; tc <= T; ++tc) {
    int N, S, p; cin >> N >> S >> p;
    int safepoints = 2*(p-1) + p;
    int surprisingpoints = max(2, 2*(p-2) + p);
    int safescores = 0, surprises = 0;
    for(int i = 0; i < N; ++i) {
      int x; cin >> x;
      if(x >= safepoints) safescores++;
      else if(x >= surprisingpoints) surprises++;
    }
    surprises = min(surprises, S);
    cout << "Case #" << tc << ": " << safescores + surprises << endl;
  }
  return 0;
}
