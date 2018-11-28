#include<iostream>
#include<queue>
#include<cstdlib>
#include<algorithm>

using namespace std;

template <class T>
T& select_by_kind(char kind, T& orange, T& blue) {
  return kind == 'O' ? orange : blue;
}

int solve(queue<char>& robot, queue<int>& oq, queue<int>& bq) {

  int o_pos = 1, b_pos = 1;
  int sum = 0;

  while (!robot.empty()) {
    char kind = robot.front();
    robot.pop();

    queue<int>& target_queue = select_by_kind(kind, oq, bq);
    queue<int>& other_queue = select_by_kind(kind, bq, oq);
    int& target_pos = select_by_kind(kind, o_pos, b_pos);
    int& other_pos = select_by_kind(kind, b_pos, o_pos);

    int target = target_queue.front();
    target_queue.pop();

    int time = abs(target_pos - target) + 1;

    target_pos = target;
    sum += time;

    int other_diff = other_queue.empty() ? 0 : other_pos - other_queue.front();
    other_pos += (other_diff > 0 ? -1 : 1) * min(abs(other_diff), time);
  }

  return sum;
}

int main() {
  int t;
  cin >> t;

  for (int s = 0; s < t; ++s) {
    int n;
    cin >> n;

    queue<char> robot;
    queue<int> oq, bq;
    for (int i = 0; i < n; ++i) {
      char kind;
      int pos;
      cin >> kind >> pos;
      robot.push(kind);
      select_by_kind(kind, oq, bq).push(pos);
    }

    cout << "Case #" << s+1 << ": " << solve(robot, oq, bq) << endl;
  }
}
