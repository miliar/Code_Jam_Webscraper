#include <algorithm>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <deque>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define DEBUG1
#define DEBUG2

#ifdef DEBUG1
#endif
#ifdef DEBUG2
#endif

#define MAX 600

char * readLine(char *s, int sz) {
  fgets(s, sz, stdin);
  int len = strlen(s);
  if(s[len-1] == '\n') {
    s[len-1] = 0;
  }
  return s;
}

int main() {

  int number_of_cases;
  cin >> number_of_cases;

  for(int icase = 0; icase < number_of_cases; icase++) {
    int N;
    cin >> N;
    int x[MAX], y[MAX], z[MAX], vx[MAX], vy[MAX], vz[MAX];
    long double a, b, c, f, g, h;
    long double sumx, sumy, sumz, sumvx, sumvy, sumvz;

    a = b = c = f = g = h = 0;
    sumx = sumy = sumz = sumvx = sumvy = sumvz = 0;

    for(int n=0; n < N; n++) {
      int tx, ty, tz, tvx, tvy, tvz;
      cin >> tx >> ty >> tz >> tvx >> tvy >> tvz;
      x[n]  = tx;
      y[n]  = ty;
      z[n]  = tz;
      vx[n] = tvx;
      vy[n] = tvy;
      vz[n] = tvz;

      sumx += x[n];
      sumy += y[n];
      sumz += z[n];
      sumvx += vx[n];
      sumvy += vy[n];
      sumvz += vz[n];
      
    }

    a = sumx / N;
    b = sumy / N;
    c = sumz / N;

    f = sumvx / N;
    g = sumvy / N;
    h = sumvz / N;
//     cout << "sumx, sumy, sumz, sumvx, sumvy, sumvz" << endl;
//     printf("%Lf %Lf %Lf %Lf %Lf %Lf \n", sumx, sumy, sumz, sumvx, sumvy, sumvz);
//     cout << "a, b, c, f, g, h" << endl;
//     printf("%Lf %Lf %Lf %Lf %Lf %Lf \n", a, b, c, f, g, h );

    long double denom = f*f + g*g + h*h;
    long double numer = a*f + b*g + c*h;
//     cout << "numer: " << numer << ", denom: " << denom << endl;
    long double tmin = - numer / denom;

    if(isnan(tmin) || tmin <= 0) {
      // in case of nan just assume 0 as the minimum time
//       cout << " NAN:: tmin is nan " << endl;
      tmin = 0;
    }
    long double dmin = sqrt(
                    a * a + b * b + c * c
                    + 2 * tmin * numer
                    + tmin * tmin * denom
                    );
    if(isnan(dmin)) {
      dmin = 0;
    }
//     int row, col;
//     cin >> row >> col;

//     cout << "Case #" << icase+1 << ": " ;
//     cout << "tmin: " << tmin << ", dmin: " << dmin << endl;
    printf("Case #%d: %.8Lf %.8Lf\n", icase+1, dmin, tmin);
//     cout << "Case #" << icase+1 << ": " << dmin << " " << tmin << endl;
    
  }
  return 0;
}

