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

double length;
double speed1;
double speed2;
double maxRunTime;
int nWalkways;

struct Walkway {

  double length;
  double speed;
  bool operator<(const Walkway& w) const {
    return speed < w.speed;
  }
};

vector<Walkway> walkways;

int main() {
  int nCases;
  scanf("%d", &nCases);
  for (int iCase = 1; iCase <= nCases; iCase++) {
    walkways.clear();
    scanf("%lf%lf%lf%lf%d", &length, &speed1, &speed2, &maxRunTime, &nWalkways);
    double wlength = 0;
    
    for (int i = 0; i < nWalkways; i++) {
      double x1, x2, speed;
      scanf("%lf%lf%lf", &x1, &x2, &speed);
      walkways.push_back(Walkway());
      walkways.back().length = x2 - x1;
      walkways.back().speed = speed;
      wlength += x2 - x1;
    }
    
    if (length > wlength) {
      walkways.push_back(Walkway());
      walkways.back().length = length - wlength;
      walkways.back().speed = 0;
    }
    
    sort(walkways.begin(), walkways.end());
    
    double time = 0;
    
    for (size_t i = 0; i < walkways.size(); i++) {
      Walkway& w = walkways[i];
      //cout << "w.speed=" << w.speed << " w.length=" << w.length << endl;
      double rt = min(maxRunTime, w.length / (w.speed + speed2));
      time += rt;
      maxRunTime -= rt;
      double rd = rt * (w.speed + speed2);
      double wd = w.length - rd;
      double wt = wd / (w.speed + speed1);
      time += wt;
    }
    
    printf("Case #%i: %.10f\n", iCase, time);
  }
  return 0;
}
