#include <iostream>
#include <algorithm>
#include <string.h>
#include <vector>
#include <sstream>
#include <fstream>
#include <set>
#include <cmath>

using namespace std;

#define FR(i, n) for (int i=0; i<n; i++)
#define Rep(i, n) for (int _lll=(n), i=0; i<_lll; i++)
#define FOR(i, a, b) for (int i=a; i<=b; i++)
#define myabs(a) ((a)>0? (a) : (-(a)))
#define For(i, a, b) for (int _lll=(b), i=a; i<=_lll; i++)
#define Size(a) ((int)a.size())
#define All(a) a.begin(), a.end()
#define Sort(a) sort(All(a))
#define PB push_back
#define MP make_pair
#define LL long long



#define MAXN 100000

inline double tmax(double x, double y) {
       if (x<y) return y;
       return x;
}
inline double tmin(double x, double y) {
       if (x>y) return y;
       return x;
}

int n;
double x[100], y[100], r[100];
double ret;

double go(int i, int j) {
       double d =  sqrt((x[i]-x[j])*(x[i]-x[j]) + (y[i]-y[j])*(y[i]-y[j]));
       return (d + r[i] + r[j])/2;
}

void process() {
     ret = 1e20;
     if (n==1) ret = r[0];
     if (n==2) ret = tmax(r[0], r[1]);
     if (n==3) {
        ret = tmax( go(0, 1), r[2]);
        ret = tmin( ret, tmax( go(0, 2), r[1]));
        ret = tmin( ret, tmax( go(2, 1), r[0]));
     }
}

int main() {
    freopen("d.in", "rt", stdin);
    freopen("d.out", "wt", stdout);
    
    int ntest;
    cin >> ntest;
    
    string temp, st;
    getline(cin, temp);    
    FR(u, ntest) {      
          cout << "Case #" << u+1<<": ";  
          cin >> n;
          FR(i, n) {                
                cin >> x[i] >> y[i] >> r[i];
          }         
          
          process();
          printf("%.7lf\n", ret);
    }    
    
    return 0;
}

