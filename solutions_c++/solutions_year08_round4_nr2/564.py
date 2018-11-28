#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string> 
#include <vector>

using namespace std;

int n,m,a;

bool test (int x1, int y1, int x2, int y2) {
  int dx = -min (min (x1,x2),0);
  int dy = -min (min (y1,y2),0);
  if (dx >=0 && dx <= n &&
      dy >= 0 && dy <= m &&
      x1+dx >=0 && x1+dx <=n &&
      y1+dy >=0 && y1+dy <=m&&
      x2+dx >=0 && x2+dx <=n &&
      y2+dy >=0 && y2+dy <=m) {
    cout << dx << " " << dy << " " << x1 + dx << " " << y1 +dy
         << " " <<  x2 + dx << " " << y2 + dy << "\n";
    return true;
  }
  return false;
}

      
      

int main() {
  int num_cases ;
  cin >> num_cases;
  for (int case_num = 1; case_num <= num_cases; ++case_num) {
    cout << "Case #" << case_num << ": ";
    cin >>  n >> m >> a;
    if (n*m < a) {
      cout << "IMPOSSIBLE\n";
      continue;
    }
    
    bool found = false;
    for (int x1 = 0; x1 <= n && !found; ++x1 ) {
      for (int y2 = 0; y2 <= m && !found; ++y2 ) {
        int x2y1 = x1*y2-a;
        // cerr << "testing " << x1 << " " << y2 << " " << x2y1 << " " << a << " " << x1*y2<< "\n";
        if (x2y1==0) {
          cout << "0 0 " << x1 << " 0 0 " << y2 << "\n";
          found = true;
          break;
        }
        for (int x2 = 1; x2  <= n; ++x2) {
          if (x2y1 % x2 == 0) {
            // cerr << x1 << " " << x2y1/x2 << " " << x2 << " "  << y2 << "\n";
            if (test (x1,x2y1/x2,x2,y2)) {
              found = true;
              break;
            }
            if (test (x1,-x2y1/x2,-x2,y2)) {
              found = true;
              break;
            }
          }
        }
      }
    }
    
    if (!found) cout << "IMPOSSIBLE\n";
  }
}
