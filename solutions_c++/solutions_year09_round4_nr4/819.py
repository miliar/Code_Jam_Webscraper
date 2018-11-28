#include <iostream>
#include <vector>
#include <map>
#include <cmath>
#include <utility>
#include <set>
#include <string>
#include <algorithm>
#include <queue>
#include <stack>
using namespace std;

typedef pair<int, int> PII;
typedef long long ll;
typedef vector<ll> VI;
typedef vector<bool> VB;
typedef vector<VI> VVI;

struct planta {
  double x, y, r;
};

double dist(double x1, double y1, double x2, double y2) {
  return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
}

int main() {
  cout.setf(ios::fixed);
  cout.precision(9);
  int tt;
  cin >> tt;
  for (int t=1; t<=tt; ++t) {
    cout << "Case #" << t << ": ";
    int n;
    cin >> n;
    vector<planta> v(n);
    double radi = 0.0;
    for (int i=0; i<n; ++i) {
      cin >> v[i].x >> v[i].y >> v[i].r;
      if (v[i].r > radi)
        radi = v[i].r;
    }
    double minim = 1000000000.0;
    for (int i=0; i<(1<<n); ++i) {
      vector<vector<planta> > v1(2);
      for (int j=0; j<n; ++j)
        if ((1<<j)&i)
          v1[0].push_back(v[j]);
        else
          v1[1].push_back(v[j]);
      double maxim = radi*2.0;
      for (int m=0; m<2; ++m)
        for (int j=0; j<v1[m].size(); ++j)
          for (int k=j+1; k<v1[m].size(); ++k)
            if (dist(v1[m][j].x, v1[m][j].y, v1[m][k].x, v1[m][k].y) + v1[m][j].r + v1[m][k].r > maxim)
              maxim = dist(v1[m][j].x, v1[m][j].y, v1[m][k].x, v1[m][k].y) + v1[m][j].r + v1[m][k].r;
      if (maxim < minim)
        minim = maxim;
    }
    cout << minim/2.0 << endl;
  }
}