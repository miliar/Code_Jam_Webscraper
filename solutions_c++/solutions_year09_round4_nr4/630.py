#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <sstream>
#include <set>
#include <list>
#include <fstream>
#include <cmath>

using namespace std;

ifstream fin("D-small-attempt1.in");
ofstream fout("file.out");

#ifdef _DEBUG
#define fin cin
#define fout cout
#endif

double dist(double x1, double y1, double x2, double y2) {
  return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
}

int main() {
  int C = 0;
  fin >> C;
  for(int c = 0; c < C; c++) {
    double result = 0;
    int N = 0;
    fin >> N;
    vector<double> x, y, r;
    for(int i = 0; i < N; i++) {
      int xx, yy, rr;
      fin >> xx >> yy >> rr;
      x.push_back(xx);
      y.push_back(yy);
      r.push_back(rr);
    }
    switch(N) {
      case 1:
        result = r.front();
        break;
      case 2:
        result = *max_element(r.begin(), r.end());
        break;
      case 3:
        result = max(r.at(0), r.at(1)+r.at(2)+dist(x[1], y[1], x[2], y[2]))/2;
        result = min(result, max(r.at(1), r.at(0)+r.at(2)+dist(x[0], y[0], x[2], y[2]))/2);
        result = min(result, max(r.at(2), r.at(0)+r.at(1)+dist(x[0], y[0], x[1], y[1]))/2);
    }
    fout.precision(10);
    fout << "Case #" << c+1 << ": " << result << endl;
  }
}
