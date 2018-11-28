#include <iostream>
#include <vector>
using namespace std;

int main()
{
  int T, R, k, N;
  cin >> T;
  for (int i = 0; i < T; ++i){
    cin >> R >> k >> N;
    vector<int> g(N);
    for (int j = 0; j < N; ++j){
      int G;
      cin >> G;
      g[j] = G;
    }
    vector<int> p(N, -1);
    vector<int> next(N, -1);
    int cur = 0;
    while (next[cur] == -1) {
      int prev = cur;
      int count = g[cur];
      cur = (cur + 1) % N;
      for (; cur != prev; cur = (cur+1)%N){
	if (count + g[cur] > k) break;
	count += g[cur];
      }
      p[prev] = count;
      next[prev] = cur;      
    }
    long long ans = 0;
    int loopStart = cur;
    int loopSize = 1;
    long long loopSum = p[loopStart];
    for (int j = next[loopStart]; j != loopStart; j = next[j]) {
      ++loopSize;
      loopSum += p[j];
    }
    cur = 0;
    while (R > 0 && cur != loopStart) {
      ans += p[cur];
      cur = next[cur];
      --R;
    }
    ans += R / loopSize * loopSum;
    R %= loopSize;
    while (R > 0) {
      ans += p[cur];
      cur = next[cur];
      --R;
    }
    cout << "Case #" << i+1 << ": " << ans << "\n";
  }
}
