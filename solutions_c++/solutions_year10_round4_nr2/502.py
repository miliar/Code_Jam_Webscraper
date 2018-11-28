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
    int64 inf = 1000000000;
    inf *= inf; 
    int t;
    cin >> t;
    for (int l = 0; l < t; ++l) {
       int p;
       cin >> p;
       vector <int64> m (1 << p, 0);
       for (int i = 0; i < (1 << p); ++i)
           cin >> m[i];
           
       vector <vector <int64> > price (p + 1, vector <int64> (1 << p, 0));
       for (int i = 1; i <= p; ++i)
           for (int j = 0; j < (1 << (p - i)); ++j)
               cin >> price[i][j];
       vector <vector <vector <int64> > > res (p + 1, vector <vector <int64> > (p + 1, vector <int64> (1 << p, inf)));
       
       
       
       for (int i = 0; i < (1 << p); ++i)
           for (int j = 0; j <= p; ++j)
               if ((p - m[i]) <= j)
                  res[j][0][i] = 0;
        
       
       for (int i = 1; i <= p; ++i)
           for (int j = 0; j < (1 << (p - i)); ++j)
                for (int k = 0; k <= p; ++k) {
                    int left = 2 * j;
                    int right = 2 * j + 1;
                    res[k][i][j] = min (res[k][i][j], res[k][i-1][left] + res[k][i-1][right]);
                    if (k < p)
                       res[k][i][j] = min (res[k][i][j], res[k+1][i-1][left] + res[k+1][i-1][right] + price[i][j]);
                 }
           
       
        
       
       
       
         cout << "Case #" << l + 1 << ": " << res[0][p][0] << endl;
    }
      
    return 0;
} 
