#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

struct level {
  int time;
  int prob;
  int index;
};

bool cmp (level a, level b) {
  int heura = a.time * (100 - b.prob);
  int heurb = b.time * (100 - a.prob);
  if (heura == heurb) {
    return (a.index < b.index);
  } else {
    return (heura < heurb);
  }
}

int main() {
  int t; cin >> t;
  for (int case_num = 1; case_num <= t; ++case_num) {
    int n; cin >> n;

    vector<level> v;
    for (int i = 0; i < n; ++i) {
      level l;
      cin >> l.time;
      l.index = i;

      v.push_back(l);
    }
    for (int i = 0; i < n; ++i) {
      int dying; cin >> dying;
      v[i].prob = (100 - dying);
    }

    sort(v.begin(), v.end(), cmp);

    cout << "Case #" << case_num << ":";

    for (int i = 0; i < v.size(); ++i) {
      cout << " " << v[i].index;
    }
    cout << endl;
  }
  return 0;
}