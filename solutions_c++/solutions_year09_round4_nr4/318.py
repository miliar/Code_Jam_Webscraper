// =====================================================================================
//   [ Filename    ]  pcsmall.cpp
//   [ Description ]  
//   [ Created     ]  09/27/2009 12:27:04 AM CST
//   [ Author      ]  Jiunru Yang , yangjiunru [at] gmail.com, NTUEE
// =====================================================================================

#include <iostream>
#include <cmath>
#include <vector>

using namespace std;



void solve(int caseNo)
{
   int N;
   vector<double> x;
   vector<double> y;
   vector<double> r;
   vector<vector<double> > dist;
   double ans;
   cin >> N;
   x.resize(N);
   y.resize(N);
   r.resize(N);
   dist.resize(N, vector<double>(N, 0.0));
   for (int i = 0; i < N; ++i)
      cin >> x[i] >> y[i] >> r[i];
   if (N == 1) {
      ans = r[0];
   }
   else if (N == 2) {
      ans = std::max(r[0], r[1]);
   }
   else {
      for (int i = 0; i < 3; ++i)
         for (int j = 0; j < 3; ++j)
            dist[i][j] = sqrt((x[i] - x[j]) * (x[i] - x[j]) + (y[i] - y[j]) * (y[i] - y[j]));
      ans = 2000;
      double tans;
      tans = std::max(r[0], (r[1]+r[2]+dist[1][2])/2);
      ans = std::min(tans, ans);
      tans = std::max(r[1], (r[0]+r[2]+dist[0][2])/2);
      ans = std::min(tans, ans);
      tans = std::max(r[2], (r[1]+r[0]+dist[1][0])/2);
      ans = std::min(tans, ans);
   }
   cout << "Case #" << caseNo << ": " << ans << endl;
}

int main()
{
   int T;
   cin >> T;
   for(int i =1; i <= T; ++i)
      solve(i);
   return 0;
}
