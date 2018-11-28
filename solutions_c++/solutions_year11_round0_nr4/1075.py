#include <iostream>
using namespace std;

int main() {
  int T;
  cin >> T;
  for (int t = 1; t<=T; t++) {
    int next;
    int N;
    int fixpoints = 0;
    cin >> N;
    for (int i = 1; i<=N; i++) {
      cin >> next;
      if (i == next) {
        fixpoints++;
      }
    }
    cout << "Case #" << t << ": " << (N-fixpoints) << endl;
  }
}
