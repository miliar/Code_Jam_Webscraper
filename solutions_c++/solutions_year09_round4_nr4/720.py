#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <set>
#include <map>
#include <iomanip>
#include <algorithm>
#include <cmath>

using namespace std;

double d(double a, double b, double c, double d) {
   return sqrt((a-c)*(a-c) + (b-d)*(b-d));        
}

double go() {
   int n;
   cin >> n;
   vector<double> x(n);
   vector<double> y(n);
   vector<double> r(n);
   
   for (int i = 0; i < n; i++) {
       cin >> x[i] >> y[i] >> r[i];    
   }
   
   double dRes = 0;
   
   if (n == 1) {
      return r[0];      
   }
   if (n == 2) {
      return std::max(r[0], r[1]);      
   }
   if (n == 3) {
       dRes = 100000000000LL;
       // 01
       dRes = min(dRes, max(r[2], (r[1]+r[0]+d(x[0] , y[0], x[1], y[1])) / 2));       
       // 12
       dRes = min(dRes, max(r[0], (r[1]+r[2]+d(x[2] , y[2], x[1], y[1])) / 2));       
       // 02
       dRes = min(dRes, max(r[1], (r[2]+r[0]+d(x[0] , y[0], x[2], y[2])) / 2));
   }

   return dRes;
}

int main() {
    int N;
    cin >> N;
    cout.setf(ios::fixed);
    cout.precision(9);
    for (int i = 0; i < N; i++) {
        cout << "Case #" << i + 1 << ": " << go() << std::endl;       
    }
}
