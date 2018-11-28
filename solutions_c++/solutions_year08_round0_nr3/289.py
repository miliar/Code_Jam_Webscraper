#include<iostream>
#include<iomanip>
#include<cmath>
#include<cassert>

#define x first
#define y second

using namespace std;

typedef pair<double, double> pdd;

const double pi = 2.*acos(0.);

double formula(double r, double h) {
   if (h>r) h=r;
   return abs((r*r*(pi/2.-acos(h/r)) + sqrt(r*r-h*h)*h) / 2.);
}

double area_cilindre(double r, double y1, double y2) {
   if (y1*y2 >= 0) return abs(formula(r,abs(y1)) - formula(r,abs(y2)));
   else            return abs(formula(r,abs(y1)) + formula(r,abs(y2)));
}

bool inside(pdd A, double R) {
   return (A.x*A.x + A.y*A.y <= R*R);
}

double area(pdd A, pdd D, double R) {
   pdd B(D.x, A.y);
   pdd C(A.x, D.y);
   if (inside(D,R)) {
     return abs((A.x - B.x)*(A.y - C.y));
   }
   else if(inside(B,R) and inside(C,R)) {
     double x0 = sqrt(R*R - C.y*C.y);
     double y0 = sqrt(R*R - B.x*B.x);
     return abs((A.y-y0)*(A.x-B.x)) + area_cilindre(R, y0, C.y) - abs(y0-C.y)*A.x;
   }
   else if(inside(C,R)) {
     return area_cilindre(R, A.y, C.y) - abs(A.y-C.y)*A.x;
   }
   else if(inside(B,R)) {
     return area_cilindre(R, A.x, B.x) - abs(A.x-B.x)*A.y; 
   }
   else if(inside(A,R)){
     double y0 = sqrt(R*R - A.x*A.x);
     double x0 = sqrt(R*R - A.y*A.y);
     return area_cilindre(R, A.y, y0) - abs(A.y-y0)*A.x;      
   }
   return 0;
}

int main() {
   int n;
   cin >> n;
   for (int cas = 1; cas <= n; cas++) {
      double f, R, t, r, g;
      cin >> f >> R >> t >> r >> g;
      g += 2*r;
      r += f;  // faig mes amples les cordes
      t += f;  // faig mes ample el marge
      double Rp = R-t;
      double buida = 0;
      if (Rp > 0 and g - 2*r > 0) {
         for (int i = 0; i*g < Rp; i++) {
            for (int j = 0; j*g < Rp; j++) {
               buida += 4*area(pdd(i*g+r, j*g+r), pdd((i+1)*g-r,(j+1)*g-r), Rp);
            }
         }
      }
      cout.setf(ios::fixed);
      cout.precision(9);
      cout << "Case #" << cas << ": " << 1. - (buida/(pi*R*R)) << endl;
   }
}
