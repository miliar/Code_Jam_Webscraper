#include <iostream>
#include <vector>

#define HMAX 1000000000

using namespace std;

int highest[3000];
int grad[3000];
vector<int> child[3000];
int height[3000];
bool impossible;

void set(int curr) {
  for (int i = 0; i < child[curr].size(); ++i) {
    grad[child[curr][i]] = grad[curr];
    height[child[curr][i]] = height[curr] - (curr - child[curr][i]) * grad[curr];
    grad[curr]++;
    set(child[curr][i]);
  }
}

int main() {
  int t; cin >> t;
  for (int case_num = 1; case_num <= t; ++case_num) {
    int n; cin >> n;
    for (int i = 0; i < n; ++i) {
      child[i].clear();
    }
    for (int i = 0; i < n - 1; ++i) {
      cin >> highest[i];
      highest[i]--;
      height[i] = -1;

      child[highest[i]].push_back(i);
    }

    grad[n - 1] = 0;
    height[n - 1] = HMAX;

    set(n - 1);

    impossible = false;
    for (int i = 0; i < n; ++i) {
      for (int j = i + 1; j < highest[i]; ++j) {
        if (highest[j] > highest[i]) impossible = true;
      }
    }

    cout << "Case #" << case_num << ":";
    if (impossible) {
      cout << " Impossible" << endl;
    } else {
      for (int i = 0; i < n; ++i) {
        cout << " " << height[i];
      }
      cout << endl;
    }

  }
  return 0;
}