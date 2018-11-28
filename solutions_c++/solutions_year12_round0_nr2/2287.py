#include <iostream>
#include <algorithm>
using namespace std;

int main() {
  int T;
  cin >> T;
  for (int t = 0; t < T; ++t) {
    int S, N, p;
    cin>>N>>S>>p;
    int score;
    int minscore = max(p - 1, 0) * 2 + p;
    int supscore = max(p - 2, 0) * 2 + p;
    int count = 0;
    for (int i = 0; i < N; ++i) {
      cin >> score;
      if (score >= minscore) count++;
      else if (score >= supscore && S > 0) {
        count++;
        S--;
      }
    }
    cout << "Case #" << t + 1 << ": " << count << endl;
  }	
  return 0;
}
