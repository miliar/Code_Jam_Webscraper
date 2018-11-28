#include <iostream>
#include <iomanip>
#include <utility>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

typedef pair<int, int> PII;
typedef vector<PII> VP;

const double TOL = 1E-2;

bool possible(double T, const VP &vendors, int C, int D) {
  double lastP = double(vendors[0].first) - T - D;

  for (int i = 0; i < C; ++i) {
    double pos = vendors[i].first;
    int nV = vendors[i].second;
    for (int j = 0; j < nV; ++j) {
      double target = max(lastP + D, pos - T);
      if (target > pos+T) return false;
      lastP = target;
      }
    }

  return true;
  }

double binSearch(const VP &vendors, int C, int D) {
  double minT = 0, maxT = 1;

  if (possible(minT, vendors, C, D))
    return minT;

  while (!possible(maxT, vendors, C, D)) {
    minT = maxT;
    maxT *= 2;
    }

  while (maxT - minT > TOL) {
    double mT = (minT + maxT) / 2;

    if (possible(mT, vendors, C, D))
      maxT = mT;
    else
      minT = mT;
    }

  return maxT;
  }

int main() {
  cout << fixed << setprecision(7);
  int T; cin >> T;
  for (int cNum = 1; cNum <= T; ++cNum) {
    int C, D; cin >> C >> D;

    VP vendors(C); int nV = 0;
    for (int i = 0; i < C; ++i) {
      cin >> vendors[i].first >> vendors[i].second;
      nV += vendors[i].second;
      }

    cout << "Case #" << cNum << ": " << binSearch(vendors, C, D) << '\n';
    }
  }
