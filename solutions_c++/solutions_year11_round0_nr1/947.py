#include <iostream>
#include <cstdlib>
using namespace std;

int main(void) {
  cin.sync_with_stdio(0);

  int CASES; cin >> CASES;
  for (int tt=1; tt<=CASES; ++tt) { // caret here
    int t = 0;
    struct { int time, pos; } state[2] = {{0, 1}, {0, 1}};

    int ncmd; cin >> ncmd;
    while (ncmd-- > 0) {
      string who_str;
      int where;
      cin >> who_str >> where;
      int who = who_str == "O";

      int dt = abs(where - state[who].pos);
      state[who].time = t = max(t, state[who].time + dt) + 1;
      state[who].pos = where;
    }

    cout << "Case #" << tt << ": " << t << "\n";
  }

  return 0;
}
