#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

class Bot {
 public:
  int cur_pos;
  int time;
  Bot() {
    cur_pos = 1;
    time = 0;
  };
  void advance(int b_num, int other_bot_time) {
    int my_time = abs(cur_pos - b_num) + 1;
    time = max(time + my_time, other_bot_time + 1);
    cur_pos = b_num;
  }
};

int main() {
  int n_cases = 0;
  cin >> n_cases;

  for (int i = 0; i < n_cases; ++i) {
    vector<Bot> bots;
    Bot tmp;
    bots.push_back(tmp); // O
    bots.push_back(tmp); // B
    int n_buttons = 0;
    cin >> n_buttons;
    for (int j = 0; j < n_buttons; ++j) {
      char bot_name;
      int b_num;
      cin >> bot_name >> b_num;
      int bot_id = 0;
      if (bot_name == 'B') bot_id = 1;

      bots[bot_id].advance(b_num, bots[!bot_id].time);
      //cout << bot_name << " " << b_num << " - " << " at time " << bots[bot_id].time << endl;
    }
    cout << "Case #" << i + 1 << ": " << max(bots[0].time, bots[1].time) << '\n';
  }
  return 0;
}
