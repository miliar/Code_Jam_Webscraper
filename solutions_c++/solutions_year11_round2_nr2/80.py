#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <climits>
#include <ctime>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <deque>
#include <list>
#include <queue>
#include <set>
#include <map>
#include <limits>

using namespace std;

int minDist;
int nVendors;
int nPoints;
vector<int> vendors;

bool testTime(double t) {
  double x = -1e100;
  for (int i = 0; i < nVendors; i++) {
    double minX = vendors[i] - t, maxX = vendors[i] + t;
    if (maxX < x + minDist) return false;
    x = max(x + minDist, minX);
  }
  return true;
}

int main() {
  int nCases;
  scanf("%d", &nCases);
  for (int iCase = 1; iCase <= nCases; iCase++) {
    cerr << iCase << endl;
    vendors.clear();
    scanf("%d%d", &nPoints, &minDist);
    for (int i = 0; i < nPoints; i++) {
      int position, posCount;
      scanf("%d%d", &position, &posCount);
      for (int i = 0; i < posCount; i++) {
        vendors.push_back(position);
      }
    }
    nVendors = vendors.size();
    double minTime = 0;
    double maxTime = 1;
    if (!testTime(0)) {
      while (!testTime(maxTime)) {
        minTime = maxTime;
        maxTime *= 2.0;
        //cout << maxTime << endl;
      }
      while (maxTime - minTime > 1e-7 && (maxTime - minTime) / minTime > 1e-7) {
        double t = (minTime + maxTime) * 0.5;
        //cout << t << endl;
        //cout << "t=" << t << endl;
        if (testTime(t))
          maxTime = t;
        else
          minTime = t;
      }
    }
    printf("Case #%i: %.12f\n", iCase, minTime);
  }
  return 0;
}
