#include <iostream>
#include <algorithm>

using namespace std;

void process(int button, int &pos, int &lastT, int &curT) {
  int newT = max(curT + 1, lastT + abs(pos - button) + 1);
  lastT = curT = newT;
  pos = button;
  }

int main() {
  int T; cin >> T;
  for (int cNum = 1; cNum <= T; ++cNum) {
    int N; cin >> N;
    
    int oPos = 1, bPos = 1;
    int oT = 0, bT = 0, curT = 0;
    for (int i = 0; i < N; ++i) {
      char c; int button; cin >> c >> button;
      if (c == 'O')
        process(button, oPos, oT, curT);
      else
        process(button, bPos, bT, curT);
      }

    cout << "Case #" << cNum << ": " << curT << '\n';
    }
  }
