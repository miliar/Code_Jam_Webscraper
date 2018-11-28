// Problem C: Theme Park (Qualification Round, Google Code Jam 2010)
// Author: Su Shi (Carmack.Shi@gmail.com)
// Usage: [execute] < inputfile > outputfile

#include <iostream>
#include <queue>
#include <cassert>

using namespace std;

struct GroupData {
  GroupData()
    : current_load(-1), current_earning(-1), current_position(-1) { }
  long long current_load;
  long long current_earning;
  int current_position;
};

long long GetMoney(const vector<int>& groups, int r, int k) {
  size_t n = groups.size();

  assert(n >= 1 && r >= 1 && k >= 1);

  // Store group-index in the queue.
  queue<int> group_indices;
  for (int i = 0; i < n; ++i)
    group_indices.push(i);

  // In order to speed up the looking-up for maximum persons the coaster can
  // hold for current queue, we would like to use cache to record intermediate
  // data.
  vector<GroupData> group_table(n);

  long long earned_money = 0;

  for (int j = 1; j <= r; ++j) {
    int start_group_index = group_indices.front();
    // Let's read data from cache firstly.
    long long current_load = group_table[start_group_index].current_load;
    if (current_load == -1) {
      // Calculate it.
      current_load = 0;

      for (int group_index = group_indices.front();
           (group_index != start_group_index) || (current_load == 0);
           group_index = group_indices.front()) {
        int load = groups[group_index];
        if ((current_load + load) > k)
          break;

        current_load += load;
        group_indices.pop();
        group_indices.push(group_index);
      }

      group_table[start_group_index].current_load = current_load;
      group_table[start_group_index].current_earning = earned_money;
      group_table[start_group_index].current_position = j;
    } else {
      // We find it in the cache which means we get into a cycle.
      long long cycle_load = earned_money -
                       group_table[start_group_index].current_earning;
      int cycle_unit = j - group_table[start_group_index].current_position;
      int can_cycle_times = ((r + 1) - j) / cycle_unit;

      if (can_cycle_times > 0) {
        current_load = can_cycle_times * cycle_load;
        j += can_cycle_times * cycle_unit - 1;
      } else {
        int temp_load = 0;
        for (int group_index = group_indices.front();
             temp_load != current_load;
             group_index = group_indices.front()) {
          int load = groups[group_index];
          temp_load += load;
          group_indices.pop();
          group_indices.push(group_index);
        }
      }
    }

    earned_money += current_load;
  }

  return earned_money;
}

int main() {

  int t, r, k, n, g;

  cin >> t;

  for (int i = 1; i <= t; ++i) {
    cin >> r >> k >> n;
    vector<int> groups;
    groups.reserve(n);

    while (n--) {
      cin >> g;
      groups.push_back(g);
    }

    cout << "Case #" << i << ": " << GetMoney(groups, r, k) << endl;
  }

  return 0;
}