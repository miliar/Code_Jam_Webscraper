#define _USE_MATH_DEFINES
#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <algorithm>
#include <numeric>
#include <utility>
#include <map>
#include <set>
#include <queue>
#include <complex>
#include <cmath>
#include <cassert>

using namespace std;
typedef complex<double> P;

struct DT {
  double w;
  string f;
  DT* left;
  DT* right;

  DT(double w) : w(w), f(), left(NULL), right(NULL) {}
  DT(double w, string f, DT* left, DT* right) : w(w), f(f), left(left), right(right) {}
};

DT* parse(istringstream& s)
{
  char c;
  double w;
  s >> c >> w; // '('
  s >> c;
  if (c == ')') {
    return new DT(w);
  } else {
    s.putback(c);
    string str; s >> str;
    DT* left = parse(s);
    DT* right = parse(s);
    s >> c; // ')'
    return new DT(w, str, left, right);
  }
}

double solve(double p, DT* dt, const set<string>& features)
{
  if (dt == NULL) { return p; }
  p *= dt-> w;

  if (left != NULL) {
    if (features.count(dt->f)) {
      return solve(p, dt->left, features);
    } else {
      return solve(p, dt->right, features);
    }
  } else {
    return p;
  }
}

int main(void)
{
  int N; cin >> N;
  for (int i = 0; i < N; ++i) {
    cout << "Case #" << (i+1) << ":" << endl;

    int L; cin >> L; // skip.
    string str; getline(cin, str);
    while (L--) {
      string l; getline(cin, l);
      str += l;
    }

    istringstream ss(str);

    DT* dt = parse(ss);
    int A; cin >> A;
    while (A--) {
      string name; cin >> name;
      int n; cin >> n;
      set<string> features;
      while (n--) {
        cin >> str; features.insert(str);
      }

      double ct = solve(1.0, dt, features);
      char buf[256]; sprintf(buf, "%.6f", ct);
      cout << buf << endl;
    }
  }

  return 0;
}

