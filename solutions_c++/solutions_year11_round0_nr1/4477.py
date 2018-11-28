#include <iostream>
#include <cmath>

using namespace std;

int main() {
  int T;
  cin >> T;
  for(int t=1; t<=T; t++) {
    int N;
    cin >> N;
    int button;
    char color;
    int
      pos_o = 1,
      steps_o = 0,
      pos_b = 1,
      steps_b = 0;
    
    int steps_total = 0;

    int dist;

    int steps;
    
    for(int i = 1; i<=N; i++) {
      cin >> color;
      cin >> button;
      if(color == 'O') {
	steps = max(abs(button - pos_o) - steps_o,0) + 1;
	steps_total += steps;
	steps_b += steps;
	steps_o = 0;
	pos_o = button;
      } else {
	steps = max(abs(button - pos_b) - steps_b,0) + 1;
	steps_total += steps;
	steps_o += steps;
	steps_b = 0;
	pos_b = button;
      }
    }
    cout << "Case #" << t << ": " << steps_total << endl;
  }
  return 0;
}
