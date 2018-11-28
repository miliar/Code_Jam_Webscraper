#include<fstream>
#include<iostream>
#include<cmath>
using namespace std;

const int maxn = 500+3;

int x[maxn], y[maxn], z[maxn], vx[maxn], vy[maxn], vz[maxn];
long long a, b, c, aa, bb;
double zz;

int cases, n;

int main()
{
    ifstream input("2.in");
    freopen("2.out", "w", stdout);    
    input >> cases;
    for (int k = 1; k <= cases; ++k){
      printf("Case #%d: ", k);
      input >> n; a = 0; b = 0; c = 0;
      for (int i = 1; i <= n; ++i) input >> x[i] >> y[i] >> z[i] >> vx[i] >> vy[i] >> vz[i];
      aa = 0; bb = 0;
      for (int i = 1; i <= n; ++i){
        aa += vx[i]; bb += x[i];     
      }
      a += aa*aa; b += 2*aa*bb; c += bb*bb;
      aa = 0; bb = 0;
      for (int i = 1; i <= n; ++i){
        aa += vy[i]; bb += y[i];     
      }
      a += aa*aa; b += 2*aa*bb; c += bb*bb;
      aa = 0; bb = 0;
      for (int i = 1; i <= n; ++i){
        aa += vz[i]; bb += z[i];     
      }
      a += aa*aa; b += 2*aa*bb; c += bb*bb;
      
      if (a == 0) printf("%.8lf 0.00000000\n", sqrt((c*c)/n/n));
      else {
           zz = -b/2;
           zz = zz/a;
           if (z < 0) printf("%.8lf 0.00000000\n", sqrt((c*c)/n/n));
           else
           printf("%.8lf %.8lf\n", sqrt((a*zz*zz+b*zz+c)/n/n), zz);
           }
      
    }
    
    return 0;    
}
