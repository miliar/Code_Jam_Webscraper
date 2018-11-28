// ============================================================================
//   [ Filename    ]  pdsmall.cpp
//   [ Description ]  
//   [ Created     ]  西元2010年06月05日 23時06分43秒 CST
//   [ Author      ]  Jiunru Yang, yangjiunru[at]gmail.com, LaDS3, GIEE, NTU
// ============================================================================

#include <iostream>
#include <cmath>
#include <vector>
#include <iomanip>

using namespace std;

class Sol
{
public:
   long double cal(int idx) {
      long double l2 = (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2);
      long double l = sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2));
      long double qx = _q[idx].first;
      long double qy = _q[idx].second;
      long double r12 = ((x1-qx)*(x1-qx) + (y1-qy)*(y1-qy));
      long double r22 = ((x2-qx)*(x2-qx) + (y2-qy)*(y2-qy));
      long double r1 = sqrt((x1-qx)*(x1-qx) + (y1-qy)*(y1-qy));
      long double r2 = sqrt((x2-qx)*(x2-qx) + (y2-qy)*(y2-qy));
      // long double m = sqrt(r22 - (((l2+r22-r12)/l2/4.0)*((l2+r22-r1))));
      // long double m2 = (r22 - (((l2+r22-r12)/l2/4.0)*((l2+r22-r1))));
      long double m = sqrt(r22 - (l2+r22-r12)*(l2+r22-r12)/4.0/l2);
      long double m2 = (r22 - (l2+r22-r12)*(l2+r22-r12)/4.0/l2);
      long double ans = 0.0;
      long double h12 = (r12-m2);
      long double h22 = (r22-m2);
      long double h1 = sqrt(r12-m2);
      long double h2 = sqrt(r22-m2);
      if (h12 < l2 && h22 < l2)
         ans = bow(r12, m2) + bow(r22, m2);
      else if (h12 > h22)
         ans = invbow(r22, m2) + bow(r12, m2);
      else
         ans = invbow(r12, m2) + bow(r22, m2);
      /*if (h12 > l2) ans += invbow(r22, m2);
      else ans += bow(r22, m2);
      if (h22 > l2) ans += invbow(r12, m2);
      else ans += bow(r12, m2);*/
      return ans;
      // return bow(r1, m) + bow(r2, m);
   }
   long double bow(long double r2, long double m2)
   {
      long double h = sqrt(r2-m2);
      long double ang = asin(sqrt(m2/r2));
      return r2*ang - sqrt(r2*m2 - m2*m2);
      // return r2*ang - h*sqrt(m2);
   }
   long double invbow(long double r2, long double m2)
   {
      return r2 * 4 * atan(1.0) - bow(r2, m2);
   }
   void read()
   {
      int n, m;
      cin >> n>> m;
      _q.resize(m);
      cin >> x1 >> y1 >> x2 >> y2;
      for (int i = 0; i < m; ++i)
         cin >> _q[i].first >> _q[i].second;
   }
   void solve(int caseNo) {
      read();
      cout << fixed << setprecision(8);
      cout << "Case #" << caseNo << ":";
      for (int i = 0; i < _q.size(); ++i)
         cout << " " << cal(i);
      cout << endl;
   }
   long double x1, y1, x2, y2;
   vector<pair<long double,long double> > _q;
};

int main()
{
   int T;
   cin >> T;
   for (int t =1 ; t <= T; ++t) {
      Sol s;
      s.solve(t);
   }
   return 0;
}
