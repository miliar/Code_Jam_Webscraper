#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
#include <set>
#include <algorithm>
#include <map>
#include <list>
#include <queue>
#include <deque>
#include <bitset>
#include <cstdlib>
#include <sstream>
#include <vector>

using namespace std;

const double pi = acos(-1.0);
const double eps = 1e-9;

int tc, D, C;
double P[1000005];
int V[1000005];

bool okay(double dis){
   double last = P[0] - dis;
   for (int d = 0; d < D; d++){
      for (int i = 0; i < V[d]; i++){
         if (last <= P[d]){
            if (last <= P[d] - dis) last = P[d] - dis;
         }else{
            //tricky case
            if (last > P[d] + dis) return false;
         }
         last += C;
      }
   }
   return true;
}

int main(){
   cin >> tc;
   for (int TC = 1; TC <= tc; TC++){
      printf("Case #%d: ", TC);
      cin >> D >> C;
      for (int i = 0; i < D; i++) scanf("%lf %d", &P[i], &V[i]); 
      //binary search
      double left = 0, right = 10e9;
      while (fabs(left-right) > 1e-8){
         double mid = (left+right)/2.0;
         if (okay(mid)) right = mid;
         else left = mid;
      }
      printf("%.9lf\n", (left+right)/2.0);
   }
   return 0;
}

