#include <algorithm>
#include <iomanip>
#include <iostream>
#include <cmath>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

#define FR first
#define SC second
#define L FR.FR
#define P FR.SC

using namespace std;

typedef pair<int, int> PII;

const int INF = 1000000000;

template <class Ta, class Tb> inline Tb cast(Ta a) {
  stringstream ss;
  ss << a;
  Tb b;
  ss >> b;
  return b;
}

bool comp(const pair<PII, int>& a, const pair<PII, int>& b) {
  if (a.L*100 + b.L*a.P != b.L*100 + a.L*b.P) {
    return a.L*100 + b.L*a.P < b.L*100 + a.L*b.P;
  }
  return a.SC < b.SC;
}

int main() {
  int T;
  cin >> T;
  for (int ca = 1; T--; ++ca) {
    int n;
    cin >> n;
    vector<pair<PII, int> > lvl(n);
    for (int i = 0; i < n; ++i) {
      lvl[i].SC = i;
    }
    for (int i = 0; i < n; ++i) {
      cin >> lvl[i].L;  // L
    }
    for (int i = 0; i < n; ++i) {
      cin >> lvl[i].P;
      lvl[i].P = 100-lvl[i].P;  // P
    }
    sort(lvl.begin(), lvl.end(), comp);
    
    cout << "Case #" << ca << ":";
    for (int i = 0; i < n; ++i) {
      cout << " " << lvl[i].SC;
    }
    cout << endl;
  }
}
