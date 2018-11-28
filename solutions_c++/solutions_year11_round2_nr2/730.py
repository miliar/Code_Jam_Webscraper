#include <iostream> 
#include <vector> 
#include <string> 
#include <math.h> 
#include <algorithm> 

#define sz(x) ((int)x.size()) 
#define all(x) (x).begin(), (x).end() 
#define pb(x) push_back(x) 
#define mp(x, y) make_pair(x, y) 

typedef long long int64; 

using namespace std;

void put_it(int test) {
     cout << "Case #" << test + 1 << ": ";
}


int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    int t;
    cin >> t;
    for (int test = 0; test < t; ++test) {
       int64 n;
       long double d;
       cin >> n >> d;
       vector<long double> a;
       for (int64 i = 0; i < n; ++i) {
           int64 x;
           cin >> x;
           int64 y;
           cin >> y;
           for (int64 j = 0; j < y; ++j)
              a.pb(x);
       }
       n = sz(a);
       long double left = 0;
       long double right = 100000.0;
       right *= right;
       right *= 10;
       for (int step = 0; step < 100; ++step) {
           bool ok = true;
           long double val = (left + right) / 2.0;
           vector<long double> pos = a;
           pos[0] = a[0] - val; 
           for (int i = 1; i < n; ++i) {
               if (pos[i] - pos[i - 1] >= d) {
                   pos[i] -= val;
                   if (pos[i] - pos[i - 1] < d)
                       pos[i] = pos[i - 1] + d;
               } else {
                   if (d - (pos[i] - pos[i - 1]) > val) {
                       ok = false;
                       break;
                   }
                   pos[i] = pos[i - 1] + d;
               }
           }
           if (ok)
               right = val;
           else
               left = val;
       }
       put_it(test);
       printf("%.10lf\n", (double)left);
    }
    return 0;
}
