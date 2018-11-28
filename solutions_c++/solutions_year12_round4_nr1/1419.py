#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <set>
using namespace std;

int main() {
  int T, C = 1, n;
  cin >> T;
  while (T-- && cin >> n) {
    vector<int> D, L;
    for (int i = 0; i < n; ++i) {
      int d, l;
      cin >> d >> l;
      D.push_back(d), L.push_back(l);
    }
    int d;
    cin >> d;

    bool f = false;
    queue<pair<int, int> > q;
    set<pair<int, int> > seen;
    q.push(make_pair(0, D[0]));
    while (q.size()) {
      int i = q.front().first;
      int x = q.front().second;
      q.pop();
      if (D[i] + x >= d) {
        f = true;
        break;
      }
      for (int j = i+1; j < n && D[j] <= D[i] + x; ++j) {
        pair<int, int> p = make_pair(j, min(D[j]-D[i], L[j]));
        if (seen.find(p) == seen.end()) q.push(p), seen.insert(p);
      }
    }
/*
    int i = 0, x = D[0]*2;
    while (x < d) {
      int bx = x, bj = i;
      for (int j = i+1; j < n && D[j] <= x; ++j) {
        int y = D[j] + min(D[j]-D[i], L[j]);
        if (y > bx)
          bx = y, bj = j;
      }
      if (bj == i)
        break;
      i = bj, x = bx;
    }
*/

    string yes;
    if (f) yes = "YES";
    else yes = "NO";
    cout << "Case #" << C++ << ": " << yes << endl;
  }
}
