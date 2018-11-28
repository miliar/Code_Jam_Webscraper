#include <algorithm>
#include <cmath>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

typedef __int64 ll;
const double kPi = atan(1.0) * 4;

ifstream in("in.txt");
ofstream out("out.txt");
void SolveCase();

int main() {
  int ncases;
  in >> ncases;
  for (int tc = 0; tc < ncases; tc++) {
    out << "Case #" << (tc+1) << ": ";
    SolveCase();
  }
  return 0;
}

ll Pow(int b, int e, int m) {
  if (e == 0) return 1;
  ll x = Pow(b, e/2, m);
  x = (x*x)%m;
  if (e%2 == 1) x = (x*b)%m;
  return x;
}

void SolveCase() {
  int n, m, t;
  in >> n >> m;
  vector<vector<pair<int, bool> > > clauses(m);
  for (int i = 0; i < m; i++) {
    in >> t;
    clauses[i].resize(t);
    for (int j = 0; j < t; j++) {
      int a, b;
      in >> a >> b;
      clauses[i][j].first = a-1;
      clauses[i][j].second = (b > 0);
    }
  }

  bool contradiction = false;
  vector<bool> state(n, false);
  while (!contradiction) {
    bool changed = false;
    for (int i = 0; i < (int)clauses.size(); i++) {
      bool is_sat = false;
      int pos = -1;
      for (int j = 0; j < (int)clauses[i].size(); j++) {
        if (clauses[i][j].second == state[clauses[i][j].first]) is_sat = true;
        if (clauses[i][j].second) pos = clauses[i][j].first;
      }
      if (!is_sat) {
        if (pos == -1) {
          contradiction = true;
        } else {
          state[pos] = true;
          changed = true;
        }
      }
    }
    if (!changed)
      break;
  }

  if (contradiction) {
    out << "IMPOSSIBLE" << endl;
  } else {
    for (int i = 0; i < n; i++) {
      out << (state[i]? "1" : "0");
      if (i == n-1)
        out << endl;
      else
        out << " ";
    }
  }
}
