#include <iostream>
#include <vector>

using namespace std;

int answer(vector<char>&  order, vector<int>& b, vector<int>& o) {
  int i = 0, t = 0, blue = 1, orange = 1, b_in = 0, o_in = 0;
  const int N = order.size();
  while(i < N) {
    bool pushed = false;
    if(b_in < b.size()) {
      //update blue
      if(b[b_in] == blue) {
        if(order[i] == 'B' && !pushed) {
          ++b_in; ++i;
          pushed = true;
        }
      } else if(b[b_in] < blue) {
        --blue;
      } else if(b[b_in] > blue) {
        ++blue;
      }
    }

    if(o_in < o.size()) {
      if(o[o_in] == orange) {
        if(order[i] == 'O' && !pushed) {
          ++o_in; ++i;
          pushed = true;
        }
      } else if(o[o_in] < orange) {
        --orange;
      } else if(o[o_in] > orange) {
        ++orange;
      }
    }
    ++t;
  }
  return t;
}

int main() {
  int cases;
  cin >> cases;
  for(int i = 1; i <= cases; ++i) {
    vector<int> blue;
    vector<int> orange;
    vector<char> order;
    int targets;
    cin >> targets;
    for(int j = 0; j < targets; ++j) {
      char bot;
      int goal;
      cin >> bot >> goal;
      order.push_back(bot);
      if(bot == 'O') {
        orange.push_back(goal);
      } else {
        blue.push_back(goal);
      }
    }
    cout << "Case #" << i << ": " << answer(order, blue, orange) << "\n";
  }

}
