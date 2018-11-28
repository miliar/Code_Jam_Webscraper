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

const int MAX_N = 110;

struct Point {
  Point(double x = 0, double y = 0) : x(x), y(y) {}
  double x, y;
};

double width;
Point ubound[MAX_N], lbound[MAX_N];
int lcount, ucount;

double computeArea(Point* p, int n, double w) {
  int i = 0;
  double area = 0;
  for (; i < n - 1 && p[i + 1].x < w; i++) {
    area += (p[i].y + p[i + 1].y) * 0.5 * (p[i + 1].x - p[i].x);
  }
  double yy = p[i].y + (p[i + 1].y - p[i].y) * (w - p[i].x) / (p[i + 1].x - p[i].x);
  area += (p[i].y + yy) * 0.5 * (w - p[i].x);
  return area;
}

double computeAreaUL(double w) {
  return computeArea(ubound, ucount, w) - computeArea(lbound, lcount, w);
}

int main() {
  int nCases, nGuests;
  scanf("%d", &nCases);

  for (int iCase = 1; iCase <= nCases; iCase++) {
    scanf("%lf%d%d%d", &width, &lcount, &ucount, &nGuests);
    for (int i = 0; i < lcount; i++) {
      scanf("%lf%lf", &lbound[i].x, &lbound[i].y);
    }
    for (int i = 0; i < ucount; i++) {
      scanf("%lf%lf", &ubound[i].x, &ubound[i].y);
    }
    double partArea = computeAreaUL(width) / nGuests;
    
    printf("Case #%i:\n", iCase);
    for (int i = 1; i < nGuests; i++) {
      double area = partArea * i;
      double EPSILON = 1e-7;
      double xMin = EPSILON, xMax = width;
      while (xMax - xMin >= EPSILON && (xMax - xMin) / xMin >= EPSILON) {
        double x = (xMin + xMax) * 0.5;
        if (computeAreaUL(x) > area)
          xMax = x;
        else
          xMin = x;
      }
      printf("%.10f\n", xMin);
    }
  }
  return 0;
}
