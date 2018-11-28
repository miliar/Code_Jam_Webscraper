#include <iostream>
#include <cmath>
#include <cassert>

using namespace std;

double dist(double x, double y)
{
  return sqrt(x*x+y*y);
}

int main()
{
  int n;
  cin >> n;

  for (int k = 0; k < n; k++) {
    double f, R, t, r, g;
    cin >> f >> R >> t >> r >> g;

    //cout << f << " " << R << " " << t << " " << r << " " << g << endl;
    double fg = g - f - f;
    if (fg < 0) fg = 0;
    double Rt = R - t;
    double Rtf = Rt-f;
    if (Rtf < 0) Rtf = 0;
    
    double all = R * R * M_PI;
    double ng = 0;
    for (int i = 0; ; i++) {
      double x = i * (g + r + r);
      if (x + r > Rt) break;
      for (int j = 0; ; j++) {
        double y = j * (g + r + r);
        if (y + r > Rt) break;
        double x1 = x + r + g / 2 - fg / 2;
        double y1 = y + r + g / 2 - fg / 2;
        double x2 = x + r + g / 2 + fg / 2;
        double y2 = y + r + g / 2 + fg / 2;
        bool a = dist(x1, y1) < Rtf;
        bool b = dist(x1, y2) < Rtf;
        bool c = dist(x2, y1) < Rtf;
        bool d = dist(x2, y2) < Rtf;
        double ng2 = 0;
        if (d) {
          ng2 += fg * fg;
        } else if (c && b) {
#if 1
          double x4 = sqrt(Rtf*Rtf-y2*y2);
          double y4 = sqrt(Rtf*Rtf-x2*x2);
          double x3 = x2/y4*y1;
          double y3 = y2/x4*x1;
          assert(x3 <= x2);
          assert(y3 <= y2);
          assert(x1 <= x4 && x4 <= x2);
          assert(y1 <= y4 && y4 <= y2);
          double cost = (x2*x4+y2*y4)/Rtf/Rtf;
          double theta = acos(cost);
          ng2 += Rtf*Rtf*theta/2;
          if (y3 < y1) {
            assert(x1 <= x3);
            double x5 = x4/y2*y1;
            ng2 += (x4-x1 + x5-x1) * (y2-y1) / 2;
            ng2 += (y4-y1) * (x2-x3) / 2;
            ng2 -= (x3-x5) * y1 / 2;
          } else if (x3 < x1) {
            assert(y1 <= y3);
            double y5 = y4/x2*x1;
            ng2 += (y4-y1 + y5-y1) * (x2-x1) / 2;
            ng2 += (x4-x1) * (y2-y3) / 2;
            ng2 -= (y3-y5) * x1 / 2;
          } else {
            ng2 += (x4-x1) * (y2-y3) / 2;
            ng2 += (y4-y1) * (x2-x3) / 2;
            ng2 -= (x3-x1) * y1 / 2;
            ng2 -= (y3-y1) * x1 / 2;
          }
#endif
        } else if (c && !b) {
#if 1
          //double x4 = sqrt(Rtf*Rtf-y2*y2);
          double y4 = sqrt(Rtf*Rtf-x2*x2);
          double x3 = x2/y4*y1;
          double y3 = sqrt(Rtf*Rtf-x1*x1);
          double cost = (x2*x1+y3*y4)/Rtf/Rtf;
          double theta = acos(cost);
          ng2 += Rtf*Rtf*theta/2;
          //ng2 += (x4-x1) * (y2-y3) / 2;
          ng2 += (y4-y1) * (x2-x3) / 2;
          ng2 -= (x3-x1) * y1 / 2;
          ng2 -= (y3-y1) * x1 / 2;
#endif
        } else if (!c && b) {
#if 1
          double x4 = sqrt(Rtf*Rtf-y2*y2);
          //double y4 = sqrt(Rtf*Rtf-x2*x2);
          double x3 = sqrt(Rtf*Rtf-y1*y1);
          double y3 = y2/x4*x1;
          double cost = (x3*x4+y2*y1)/Rtf/Rtf;
          double theta = acos(cost);
          ng2 += Rtf*Rtf*theta/2;
          ng2 += (x4-x1) * (y2-y3) / 2;
          //ng2 += (y4-y1) * (x2-x3) / 2;
          ng2 -= (x3-x1) * y1 / 2;
          ng2 -= (y3-y1) * x1 / 2;
#endif
        } else if (a) {
#if 1
          //double x4 = sqrt(Rtf*Rtf-y2*y2);
          //double y4 = sqrt(Rtf*Rtf-x2*x2);
          double x3 = sqrt(Rtf*Rtf-y1*y1);
          double y3 = sqrt(Rtf*Rtf-x1*x1);
          double cost = (x3*x1+y3*y1)/Rtf/Rtf;
          double theta = acos(cost);
          ng2 += Rtf*Rtf*theta/2;
          //ng2 += (x4-x1) * (y2-y3) / 2;
          //ng2 += (y4-y1) * (x2-x3) / 2;
          ng2 -= (x3-x1) * y1 / 2;
          ng2 -= (y3-y1) * x1 / 2;
#endif
        }
        if (ng2 < 0) {
          //abort();
        }
        ng += ng2;
      }
    }
    
    cout << "Case #" << k+1 << ": " << (all - 4 * ng) / all << endl;
  }

  return 0;
}

