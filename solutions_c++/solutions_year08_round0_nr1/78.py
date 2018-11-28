#include <cassert>
#include <iostream>
#include <algorithm>
#include <vector>
#include <deque>
#include <string>
#include <map>
using namespace std;
typedef deque<int> di;
#define REP(i,n) for (int i = 0; i < (int)(n); ++i)
#define FOR(i,c) for (__typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)

class QuerySwitch {
public:
  void input() {
    cin >> s_;
    cin.ignore();
    for (int i = 0; i < s_; ++i) {
      string str;
      getline(cin, str);
      assert(nam_.find(str) == nam_.end());
      nam_[str] = i;
    }
    tbl_.resize(s_);
    cin >> q_;
    cin.ignore();
    for (int i = 0; i < q_; ++i) {
      string str;
      getline(cin, str);
      assert(nam_.find(str) != nam_.end());
      int idx = nam_[str];
      assert(idx >= 0 && idx < tbl_.size());
      tbl_[idx].push_back(i);
    }
  }

  int calc() {
    int r = 0;
    int cur = -1;
    for (;;) {
      //      cout << endl << "#" << r << "---" << endl;
      //      print();
      int maxi = -1, midx = -1;
      for (unsigned i = 0; i < s_; ++i) {
        if (i == cur) continue;
        if (tbl_[i].empty()) {
          //          cout << "Last Choice: " << server(i) << endl;
          return r;
        }
        if (maxi < tbl_[i].front()) {
          maxi = tbl_[i].front();
          midx = i;
        }
      }
      //      cout << "Choice: " << server(midx) << endl;
      assert(maxi >= 0);
      for (unsigned i = 0; i < s_; ++i) {
        while (!tbl_[i].empty() && tbl_[i].front() < maxi) {
          tbl_[i].pop_front();
        }
      }
      ++r;
      cur = midx;
    }
  }

  string server(int idx) {
    FOR(i, nam_) {
      if (i->second == idx) return i->first;
    }
    return string("Unknown");
  }

  void print() {
    for (unsigned i = 0; i < s_; ++i) {
      cout << server(i) << ": " << endl;
      for (unsigned j = 0; j < tbl_[i].size(); ++j) {
        cout << "   " << tbl_[i][j];
      }
      cout << endl;
    }
    cout << endl << endl << endl;
  }

private:
  int s_, q_;
  map<string, int> nam_;
  vector<di> tbl_;
};

int main() {
  int n;
  cin >> n;
  for (int t = 1; t <= n; ++t) {
    QuerySwitch qs;
    qs.input();
    int r = qs.calc();
    cout << "Case #" << t << ": " << r << endl;
  }
}
