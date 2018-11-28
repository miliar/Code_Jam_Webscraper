#include <iostream>
using namespace std;

int main() {
  int T, N, S, p, next; cin>>T;
  for (int i = 1; i <= T; ++i) {
    cin>>N>>S>>p;
    int yes = 0, pos = 0;
    for (int j = 0; j < N; ++j) {
      cin>>next;
      if (next >= p * 3 - 2) yes++;
      else if (next >= p * 3 - 4 && next >= p) pos++;
    }
    cout << "Case #" << i << ": " << (yes + min(pos, S)) << endl;
  }
}
