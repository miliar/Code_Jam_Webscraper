#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

#define STEPS 10000

#define For(i,n) for(int i=0;i<(n);++i)

inline double possqrt(double x) {
  if (x<0) return 0;
  else return sqrt(x);
}

inline double areapart(double x) {
  double res = (x*sqrt(1-x*x) + asin(x))/2;
  //  cerr << x << ":" << res << endl;
  return res;
}

double intersec(double x0, double y0, double w, double h, double R) {
  double Rsq = R*R;
  double x = x0;
  double dx = w / STEPS;

  double area = 0;
  For(i, STEPS) {
    if (x>R) break;

    double y1 = possqrt(Rsq-x*x);
    double h1 = y1 - y0;
    if (h1<0) h1=0;
    else if (h1>h) h1=h;

    x += dx;
    double y2 = possqrt(Rsq-x*x);
    double h2 = y2 - y0;
    if (h2<0) h2=0;
    else if (h2>h) h2=h;
   
    if (h1>0 and h1<h and h2>0 and h2<h) {
      double xx0 = (x-dx)/R;
      double xx1 = x/R;
      area += (areapart(xx1) - areapart(xx0))*Rsq - y0*dx;
    }
    else area += (h1+h2)/2*dx;

    if (area != area) {
      cerr << "Buff!!" << endl;
    }
  }
  return area;
}

int main() {
  cout << setprecision(12);
  cout.setf(ios::fixed);
  //  int x0, y0, w, h, R;
  //  while (cin >> x0 >> y0 >> w >> h >> R) {
  //    cout << intersec(x0, y0, w, h, R) << endl;
  //  }

  int N;
  cin >> N;
  For(c, N) {
    double f, R, t, r, g;
    cin >> f >> R >> t >> r >> g;

    double Rin = R-t-f;
    double flyarea = 0;
    double gtf = g-2*f; 
    double trg = 2*r+g;
    double sq = gtf*gtf;
    if (sq>0) {
      double x = r+g-f;
      while (x-gtf<Rin) {

	double yc = possqrt(Rin*Rin - x*x);
	int k = int(yc / trg);
	flyarea += sq*k;
	while(1) {
	  double ar = intersec(x-gtf, k*trg+r+f, gtf, gtf, Rin);
	  if (ar==0) break;
	  flyarea += ar;
	  ++k;
	  //	  cerr << x << " " << ar << " " << k << endl;
	}
	x+=trg;
      }
    }
    flyarea *= 4;
    
    double totalarea = R*R*acos(0)*2;

    cout << "Case #" << (c+1) << ": " << (1-flyarea/totalarea) << endl;
  }
}
