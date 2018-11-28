#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int T, N;

int main() {
  cin >> T;

  for(int t = 0; t < T; t++) {
    vector<char> turn;
    vector<int> button;

    cin >> N;

    for(int i = 0; i < N; i++) {
      char c;
      int b;
      cin >> c >> b;
      turn.push_back(c);
      button.push_back(b);
    }

    int Opos = 1, Bpos = 1;
    int lastO = 0, lastB = 0;
    int time = 0;
    for(int i = 0; i < N; i++) {
      //cout << i << "  " << time << endl;
      if(turn[i] == 'O') {
	time += max(abs(button[i]-Opos)-(time-lastO), 0)+1;
	lastO = time;
	Opos = button[i];
      } else {
	time += max(abs(button[i]-Bpos)-(time-lastB), 0)+1;
	lastB = time;
	Bpos = button[i];
      }
    }

    cout << "Case #" << t+1 << ": " << time << endl;
  }

  return 0;
}
