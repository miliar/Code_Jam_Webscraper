#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
  int tt;
  cin >> tt;

  for (int t = 1; t <= tt; ++t) {
    int n;
    cin >> n;
    vector< pair<int, int> > wires(n);
    for (int i = 0; i < n; ++i)
      cin >> wires[i].first >> wires[i].second;

    sort(wires.begin(), wires.end());

    int intersect = 0;
    for (int i = 0; i < n; ++i) {
      for (int j = i + 1; j < n; ++j) {
        if (wires[i].second > wires[j].second)
          ++intersect;
      }
    }

    cout << "Case #" << t << ": " << intersect << endl;
  }

  return 0;
}
