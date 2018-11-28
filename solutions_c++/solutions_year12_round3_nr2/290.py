#include <iostream>
#include <vector>
#include <math.h>
#include <iomanip>

using namespace std;

int
main() {
  int T;
  
  cin >> T;
  
  for(int i = 1; i <= T; i++) {
    int N, A;
    double D;
    vector<double> t;
    vector<double> x;
    
    cin >> D >> N >> A;
        
    for(int j = 0; j < N; j++) {
      double tn, xn;
      
      cin >> tn >> xn;
      
      t.push_back(tn);
      x.push_back(xn);
    }
    
    cout << "Case #" << i << ':' << endl;
    for(int j = 0; j < A; j++) {
      double a;
      
      cin >> a;
      
      double tc = 0;
      double dt = (t[1] - t[0]);
      double v = 0.0; //min((x[1]-x[0])/dt, a*dt);
      double d = 0.0; //min(x[0], a*dt*dt/2);
      
      int n = 0;
      while(x[n] < D) {
        double dt = (t[n] - t[n-1]);
        d += min(x[n]-x[n-1], v*dt+a*dt*dt/2);
        v = min((x[n]-x[n-1])/dt, a*dt);

        n++;
      }
      
      if(n == 0) {
        tc = (sqrt(v*v + 2*a*(D-d)) - v)/a;
      } else if(n == 1) {
        tc = max((D-x[0])*(t[n] - t[n-1])/(x[n] - x[n-1]), (sqrt(2*a*D)/a));
      } else {
        tc = max((D-d)*(t[n] - t[n-1])/(x[n] - x[n-1]), (sqrt(v*v + 2*a*(D-d)) - v)/a);
      }
      
      cout << fixed << setprecision(6) << (t[n-1]+tc) << endl;
    }
  }
  
  return 0;
}
