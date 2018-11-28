#include <cmath>
#include <iostream>
#include <vector>

using namespace std;

const double EPS = 1e-9;

vector<vector<double> > sum_matrix(vector<vector<double> >& m) {
  vector<vector<double> > sm(m.size()+1, vector<double>(m[0].size()+1, 0));
  for (int i = 0; i < int(m.size()); ++i) {
    for (int j = 0; j < int(m[i].size()); ++j) {
      sm[i+1][j+1] = sm[i][j+1]+sm[i+1][j]-sm[i][j]+m[i][j];
    }
  }
  return sm;
}

double f(vector<vector<double> >& m, vector<vector<double> >& sm, int x, int y, int k) {
  return sm[y+k][x+k]-sm[y+k][x]-sm[y][x+k]+sm[y][x]-m[y][x]-m[y+k-1][x]-m[y][x+k-1]-m[y+k-1][x+k-1];
}

bool equal(double a, double b) {
  return abs(a-b) < EPS;
}

int main() {
  int T;
  cin >> T;
  for (int ca = 1; T--; ++ca) {
    int r, c;
    double d;
    cin >> r >> c >> d;
    vector<vector<double> > m(r, vector<double>(c));
    for (int i = 0; i < r; ++i) {
      for (int j = 0; j < c; ++j) {
        char w;
        cin >> w;
        m[i][j] = d+double(w-'0');
      }
    }
    vector<vector<double> > mpx = m, mpy = m;
    for (int i = 0; i < r; ++i) {
      for (int j = 0; j < c; ++j) {
        mpx[i][j] = double(j)*m[i][j];
        mpy[i][j] = double(i)*m[i][j];
      }
    }
    vector<vector<double> > sm = sum_matrix(m), smpx = sum_matrix(mpx), smpy = sum_matrix(mpy);
    int ans = 0;
    for (int k = min(r, c); k >= 3 && ans == 0; --k) {
      for (int y = 0; y+k-1 < r && ans == 0; ++y) {
        for (int x = 0; x+k-1 < c && ans == 0; ++x) {
          double cy = double(y+y+k-1)/2.0, cx = double(x+x+k-1)/2.0;
          double mass = f(m, sm, x, y, k);
          double mcy = f(mpy, smpy, x, y, k)/mass;
          double mcx = f(mpx, smpx, x, y, k)/mass;
          if (equal(cy, mcy) && equal(cx, mcx)) {
            ans = k;
          }
        }
      }
    }
    cout << "Case #" << ca << ": ";
    if (ans < 3) cout << "IMPOSSIBLE" << endl;
    else cout << ans << endl;
  }
}
