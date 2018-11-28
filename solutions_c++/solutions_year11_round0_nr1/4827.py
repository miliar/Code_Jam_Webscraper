#include <stdlib.h>
#include <iostream>

using namespace std;

int main(int argc, char** argv) {
  int T;
  cin >> T;
  for (int i = 1; i <= T; ++i) {
    int N;
    cin >> N;
    int pos_o = 1;
    int pos_b = 1;
    int idle_o = 0;
    int idle_b = 0;
    int total_moves = 0;
    for (int j = 0; j < N; ++j) {
      char c;
      cin >> c;
      int pos;
      cin >> pos;
      if (c == 'O') {
        int move = abs(pos - pos_o);
        int delta_move = (move > idle_o ? move - idle_o + 1 : 1);
        total_moves += delta_move;
        pos_o = pos;
        idle_o = 0;
        idle_b += delta_move;
      }
      if (c == 'B') {
        int move = abs(pos - pos_b);
        int delta_move = (move > idle_b ? move - idle_b + 1 : 1);
        total_moves += delta_move;
        pos_b = pos;
        idle_b = 0;
        idle_o += delta_move;
      }
    }
    cout << "Case #" << i << ": " << total_moves << endl;
  }
  return 0;
}
