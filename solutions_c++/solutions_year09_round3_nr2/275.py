
#include <cstdio>
#include <string>
#include <cmath>
#include <iostream>

using namespace std;

#define EPS 1e-8

int T, N;
int pos[1<<10][3], v[1<<10][3];

inline double f(double t) {
  double co[3] = {0.0, 0.0, 0.0};
  
  for ( int i = 1; i <= N; ++i ) {
    for ( int j = 0; j < 3; ++j )
      co[j] += 1.0 * pos[i][j] + t * v[i][j];
  }
  
  for ( int j = 0; j < 3; ++j )
    co[j] /= N;
    
  return co[0]*co[0] + co[1]*co[1] + co[2]*co[2];
}

pair<double, double> solve() {
  long double left = 0.0, right = 1e200;
  long double p, o;
  
  int steps = 0;
  
  while ( left + EPS <= right ) {
    ++steps;
    
    if ( steps > 100000 )
      break;
  
    p = (2 * left + right) / 3;
    o = (left + 2 * right) / 3;

    if ( f(p) <= f(o) )
      right = o;
    else
      left = p; 
  } 
  
  cout << " ! " << f(0.000000) << " " << f(left) << endl;
  
  if ( f(0.000000) <= f(left) + EPS )
    left = 0.000000;
  
  return make_pair( sqrt(f(left)), left );
}

pair<double, double> solve_math() {
  // derivatives stuff
  // (sx + svx * tmin) * svx + (sy + svy * tmin) * svy + (sz + svz * tmin) * svz = 0
  // tmin * (svx * svx + svy * svy + svz * svz) = - svx * sx - svy * sy - svz * sz
  // tmin = - (svx * sx + svy * sy + svz * sz) / (svx * svx + svy * svy + svz * svz); 

  double sx(0.0), sy(0.0), sz(0.0), svx(0.0), svy(0.0), svz(0.0);
  
  for ( int i = 1; i <= N; ++i )
    sx += pos[i][0], sy += pos[i][1], sz += pos[i][2],
    svx += v[i][0], svy += v[i][1], svz += v[i][2];
    
  if ( svx * svx + svy * svy + svz * svz == 0 ) {
    return make_pair( sqrt(f(0.000000)), 0.000000 );
  }
    
  double tmin = - (svx * sx + svy * sy + svz * sz) / (svx * svx + svy * svy + svz * svz);
  
  if ( tmin <= 0.0 )
    tmin = 0.0;
  
  return make_pair( sqrt(f(tmin)), tmin );
}

int main() {
  freopen("B-large.in", "r", stdin);
  freopen("B-large.out", "w", stdout);

//  freopen("B.in", "r", stdin);
//  freopen("B.out", "w", stdout);

  cin >> T;
  
  for ( int i = 1; i <= T; ++i ) {
    cout << "Case #" << i << ": ";
    
    cin >> N;
    for ( int j = 1; j <= N; ++j ) {
      for ( int k = 0; k < 3; ++k )
        cin >> pos[j][k];
      for ( int k = 0; k < 3; ++k )
        cin >> v[j][k];
    }
    
    //pair<double, double> res = solve();
    pair<double, double> res = solve_math();

    printf("%.8lf %.8lf\n", res.first, res.second);
    //cout << res.first << " " << res.second << endl;
  }

  return 0;
}
