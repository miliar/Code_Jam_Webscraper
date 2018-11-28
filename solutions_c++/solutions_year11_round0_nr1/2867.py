#include <iostream>
#include <algorithm>
#include <cstdlib>
using namespace std;

main() {
  int T;
  cin >> T;
  for(int tc = 0; tc < T; ++tc) {
    int N;
    int t[2], pos[2];
    pos[0] = pos[1] = 1;
    t[0] = t[1] = 0;
    cin >> N;
    for(int i = 0; i < N; ++i) {
      char c;
      int p;
      cin >> c >> p;
      int k = c == 'B' ? 0 : 1;
      t[k] = max(t[k]+abs(p - pos[k])+1, t[1-k]+1);
      pos[k] = p;
    }
    cout << "Case #" << tc+1 << ": " << max(t[0], t[1]) << endl;
  }
}
