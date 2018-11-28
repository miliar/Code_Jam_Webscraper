#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <set>
using namespace std;


void run(const set<long long>& bac, set<long long>* next) {
  map<long long, int> rq;
  for (set<long long>::const_iterator itr = bac.begin(); itr != bac.end(); ++itr) {
     rq[(*itr) + 1] += 1;
     rq[(*itr) + (1LL << 32)] += 1;
  }

  for (set<long long>::const_iterator itr = bac.begin(); itr != bac.end(); ++itr) {
    if (rq.find(*itr) != rq.end()) {
      next->insert(*itr);
    }
    rq.erase(*itr);
  }
  
  for (map<long long, int>::iterator itr = rq.begin(); itr != rq.end(); ++itr) {
    if (itr->second == 2) {
      next->insert(itr->first);
    }
  }
}

int Go() {
  int r;
  set<long long> bac;
  cin >> r;
  for (int i = 0; i < r; ++i) {
    int x1, y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;
    for (int j = x1; j <= x2; ++j) {
      for (int k = y1; k <= y2; ++k) {
        bac.insert(((j * 1ll) << 32) + k);
      }
    }
  }
  set<long long> next;
  int res = 0;
  while (bac.size() != 0 || next.size() != 0) {
    ++res;
    if (bac.size() == 0) {
      run(next, &bac);
      next.clear();
    } else {
      run(bac, &next);
      bac.clear();
    }
  }
  return res;
}


int main() {
  int t;
  cin >> t;
  for (int i = 0; i < t; ++i) {
    cout << "Case #" << i + 1 << ": " << Go() << endl;
  }

  return 0;
}