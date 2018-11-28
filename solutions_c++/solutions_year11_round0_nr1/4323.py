#include <iostream>
#include <vector>
#include <string>

using namespace std;

// Order = T * N * 

struct Robot {
  int pos;
  int command_pos;
  vector<int> button;
};

int main() {
  int T; cin >> T;
  for (int test_case_num = 1; test_case_num <= T; ++test_case_num) {
    int N; cin >> N;
    Robot O, B;
    vector<char> order;
    for (int i = 0; i < N; ++i) {
      char c; int n; cin >> c >> n;
      order.push_back(c);
      if (c == 'O') O.button.push_back(n);
      else B.button.push_back(n);
    }
    // #1 にてbutton[command_pos]がorverflowを引き起こすので、以下の措置。
    O.button.push_back(1000); B.button.push_back(1000);
    int time = 0;
    O.pos = 1; B.pos = 1;
    O.command_pos = 0; B.command_pos = 0;
    for (int i = 0; i < N; ++i) {
      bool isPushed = false;
      Robot* Main; Robot* Sub;
      while (!isPushed) {
	if (order[i] == 'O') {
	  //	  Robot* Main = &O; Robot* Sub = &B;
	  Main = &O; Sub = &B;
	} else {
	  //	  Robot* Main = &B; Robot* Sub = &O;
	  Main = &B; Sub = &O;
	}
	// #1 {
	if (Main->pos == Main->button[Main->command_pos]) {
	  if (Sub->pos == Sub->button[Sub->command_pos]) {}
	  else if (Sub->pos < Sub->button[Sub->command_pos]) { Sub->pos++; }
	  else { Sub->pos--; }
	  isPushed = true;
	}
	else if (Main->pos < Main->button[Main->command_pos]) {
	  if (Sub->pos == Sub->button[Sub->command_pos]) {}
	  else if (Sub->pos < Sub->button[Sub->command_pos]) { Sub->pos++; }
	  else { Sub->pos--; }
	  Main->pos++;
	}
	else {
	  if (Sub->pos == Sub->button[Sub->command_pos]) {}
	  else if (Sub->pos < Sub->button[Sub->command_pos]) { Sub->pos++; }
	  else { Sub->pos--; }
	  Main->pos--;
	} // } #1
	time++;
      }
      Main->command_pos++;
    }

    cout << "Case #" << test_case_num << ": " << time << endl;
  }
  return 0;
}
