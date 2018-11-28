#include <iostream>
#include <cstdlib>

using namespace std;

void do_case(int case_no) {
  int n;
  cin >> n;
  int o_button = 1;
  int b_button = 1;
  int movies = 0;
  int o_credit = 0;
  int b_credit = 0;
  for (int i = 0; i < n; ++i) {
    int to_move;
    char color;
    int button;
    cin >> color;
    cin >> button;
    if (color == 'O') {
        // move
        to_move = abs(button - o_button);
        to_move -= o_credit;
        if (to_move < 0) {
          to_move = 0;
        }
        // press
        to_move += 1;
        movies += to_move;
        b_credit += to_move;
        o_credit = 0;
        o_button = button;
    } else {
        // move
        to_move = abs(button - b_button);
        to_move -= b_credit;
        if (to_move < 0) {
          to_move = 0;
        }
        // press
        to_move += 1;
        movies += to_move;
        o_credit += to_move;
        b_credit = 0;
        b_button = button;
    }
  }
  cout << "Case #" << case_no << ": " << movies << '\n';
}

int main() {
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    do_case(i);
  }
  return 0;
}

