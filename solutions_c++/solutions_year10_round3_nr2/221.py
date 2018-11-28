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
    for (int k = 0; k < t; ++k) {
        int64 l, p, c;
        cin >> l >> p >> c;
        int n = 0;
        int64 x = 1;
        while (true) {
              if (l * x >= p) break;
              x *= c;
              n++;
        }
        int res = 0;
        int64 y = 1;
        while (true) {
              if (y >= n) break;
              y *= 2;
              res++;
        }
        cout << "Case #" << k + 1 << ": " << res << endl; 
     
           
    }
      
 
    
    return 0;
} 
