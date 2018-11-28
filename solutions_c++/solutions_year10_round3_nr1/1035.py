// Problem A: (Round 1C, Google Code Jam 2010)
// Author: Su Shi (Carmack.Shi@gmail.com)
// Usage: [execute] < inputfile > outputfile

#include <iostream>
#include <vector>

using namespace std;

typedef struct Wire_ {

  int start;
  int end;
} Wire;

bool IsIntersect(const Wire& wire_a, const Wire& wire_b) {
  if (wire_a.start < wire_b.start && wire_a.end > wire_b.end)
    return true;

  if (wire_a.start > wire_b.start && wire_a.end < wire_b.end)
    return true;

  return false;
}

int NumberOfIntersections(const vector<Wire>& wires) {

  int count = 0;

  for (int i = 0; i < wires.size(); ++i) {
    for (int j = i + 1; j < wires.size(); ++j) {
      if (IsIntersect(wires[i], wires[j]))
        ++count;
    }
  }

  return count;
}
int main() {

  int t, n;

  cin >> t;

  for (int i = 1; i <= t; ++i) {
    cin >> n;

    vector<Wire> wires(n);

    for (int j = 0; j < n; ++j) {
      cin >> wires[j].start >> wires[j].end;
    }

    cout << "Case #" << i << ": "
         << NumberOfIntersections(wires) << endl;
  }

  return 0;

}