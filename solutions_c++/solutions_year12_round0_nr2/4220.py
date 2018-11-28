#include <iostream>
using namespace std;

int main() {
  int T;
  cin >> T;
  for(int t = 1; t <= T; t++) {
    int N, S, p, score, possible = 0;
    cin >> N >> S >> p;
    for(int i = 0; i < N; i++) {
      cin >> score;
      if(score >= 3*p-2) possible++;
      else if(S > 0 && score >= 3*p-4 && p != 1) {possible++; S--;}
    }
    cout << "Case #" << t << ": " << possible << endl;
  }
}
