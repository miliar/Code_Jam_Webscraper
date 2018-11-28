#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <queue>
#include <map>

#define sz(x) ((int)x.size())
#define all(x) (x).begin(), (x).end()
#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)

typedef long long int64;

using namespace std;


int main () 
{
    freopen ("input.txt", "rt", stdin);
    freopen ("output.txt", "wt", stdout);
  
    int t;
    cin >> t;
    for (int l = 0; l < t; ++l) {
        vector <vector <int> > a (102, vector <int> (102, 0));
        int r;
        cin >> r;
        int minx = 100, maxx = 1, miny = 100, maxy = 1;
        for (int i = 0; i < r; ++i) {
            int x1, y1, x2, y2;
            cin >> x1 >> y1 >> x2 >> y2;
            minx = min (minx, x1);
            maxx = max (maxx, x2);
            miny = min (miny, y1);
            maxy = max (maxy, y2);
            for (int j = x1; j <= x2; ++j)
                for (int k = y1; k <= y2; ++k)
                    a[j][k] = 1;
        }
        int res = 0;
        while (true) {
              vector <vector <int> > b = a;
              bool ok = false;
              for (int i = minx; i <= maxx; ++i)
                  for (int j = miny; j <= maxy; ++j) {
                      if (a[i][j] == 1) {
                                  ok = true;
                                  if ((a[i - 1][j] == 0) && (a[i][j-1] == 0)) b[i][j] = 0;
                      } else {
                                  if ((a[i - 1][j] == 1) && (a[i][j-1] == 1)) b[i][j] = 1;
                      
                      }
                  }
              a = b;
              if (ok) res++;
              else break;
                  
              
              
        }
         cout << "Case #" << l + 1 << ": " << res << endl;
    }
      
    return 0;
} 
