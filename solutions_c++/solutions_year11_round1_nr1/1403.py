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

int tc, n, pd, pg;

int main(){
   cin >> tc;
   for (int TC = 1 ; TC <= tc; TC++){
      cin >> n >> pd >> pg;
      printf("Case #%d: ", TC);
      if (pg == 0){
         if (pd == 0) printf ("Possible\n");
         else printf("Broken\n");
         continue;
      }else if (pg == 100){
         if (pd == 100) printf("Possible\n");
         else printf("Broken\n");
         continue;
      }
      bool flag = false;
      for (int d = 1; d <= n; d++){
         if ((pd * d)% 100 == 0){
            int wd = pd * d / 100;
            if (wd <= d){
               flag = true;
               break;
            }
         }
      }
      if (flag) printf("Possible\n");
      else printf("Broken\n");
   }
   return 0;
}

