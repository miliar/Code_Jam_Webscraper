#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <complex>
#include <cstdlib>
#include <string>
#include <algorithm>
#include <cassert>
#include <queue>
#include <cctype>
using namespace std;

typedef long double Real;

const Real o = 1e-8;
const Real pi = acos(-1.0);
const int max_c = 64;
const int max_d = 64;

int n, nc, nd;
vector<char> a;
pair<pair<char, char>, char> c[max_c];
pair<char, char> d[max_c];
int T, I;

bool equal(const pair<char, char> &a, const pair<char, char> &b) {
  return a.first == b.first && a.second == b.second ||
    a.first == b.second && a.second == b.first;
}

void input() {
  cin >> nc;
  for (int i = 0; i < nc; ++i) {
    char x, y, z;
    cin >> x >> y >> z;
    c[i] = make_pair(make_pair(x, y), z);
  }
  cin >> nd;
  for (int i = 0; i < nd; ++i) {
    char x, y;
    cin >> x >> y;
    d[i] = make_pair(x, y);
  }
}

void solve() {
  cin >> n;
  a.clear();
  for (int i = 0; i < n; i++) {
    char ch;
    cin >> ch;
    a.push_back(ch);
    if (a.size() >= 2) {
      for (int j = 0; j < nc; ++j) {
        if (equal(c[j].first, make_pair(a[a.size() - 2], a[a.size() - 1]))) {
          a.pop_back();
          a.pop_back();
          a.push_back(c[j].second);
          break;
        }
      }
    }
    if (a.size() >= 2) {
      for (int j = 0; j < nd; ++j) {
        for (size_t k = 0; k + 1 < a.size(); ++k) {
          if (equal(d[j], make_pair(a[k], a[a.size() - 1]))) {
            a.clear();
            break;
          }
        }
      }
    }
  }
}

void output() {
  cout << "Case #" << I + 1 << ": ";
  cout << "[";
  for (size_t i = 0; i < a.size(); ++i) {
    if (i > 0)
      cout << ", ";
    cout << a[i];
  }
  cout << "]\n";
}

int main() {
  cin >> T;
  for (I = 0; I < T; ++I) {
    input();
    solve();
    output();
  }
	return 0;
}

