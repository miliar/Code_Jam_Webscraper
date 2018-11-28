// another fine solution by misof
// #includes {{{
#include <algorithm>
#include <numeric>

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cassert>

#include <cmath>
#include <complex>
using namespace std;
// }}}

/////////////////// PRE-WRITTEN CODE FOLLOWS, LOOK DOWN FOR THE SOLUTION ////////////////////////////////

// pre-written code {{{
#define FOR(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
#define FOREACH(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define SIZE(t) ((int)((t).size()))
// }}}

/////////////////// CODE WRITTEN DURING THE COMPETITION FOLLOWS ////////////////////////////////

typedef complex<double> point;
typedef vector<point> poly; // if used to store a polygon, don't repeat the first vertex 
#define EPSILON (1e-9) // epsilon used for computations involving doubles ; dec to 1e-9 for %Lf 

bool is_negative(double x) { return x < -EPSILON; } 
bool is_zero(double x) { return abs(x) <= EPSILON; } 
bool is_positive(double x) { return x > EPSILON; }

template<class T> bool are_equal(const complex<T> &A, const complex<T> &B) { 
  return is_zero(real(B)-real(A)) && is_zero(imag(B)-imag(A)); 
}

template<class T> T square_size(const complex<T> &A) { return real(A)*real(A) + imag(A)*imag(A); }
template<class T> T size(const complex<T> &A) { return sqrt(real(A)*real(A) + imag(A)*imag(A)); }

// intersect circles (C1,r1) and (C2,r2), 3 pts returned if \equiv:
template<class T> vector< complex<T> > intersect_circle_circle(
                  const complex<T> &C1, T r1, const complex<T> &C2, T r2) {
  vector< complex<T> > res;

  if (are_equal(C1,C2)) {
    // 2x the same point
    if (is_zero(r1) && is_zero(r2)) { res.push_back(C1); return res; } 
    // identical circles -- return 3 points
    if (is_zero(r1-r2)) { res.push_back(C1); res.push_back(C1); res.push_back(C1); return res; }
    // no intersection
    return res;
  }
    
  T d = sqrt(square_size(C2-C1));
  // check for no intersection
  if (is_positive(d-r1-r2) || is_positive(r1-r2-d) || is_positive(r2-r1-d)) return res; 
  // check for a single intersection
  if (is_zero(d-r1-r2)) { res.push_back( (1.0/d) * ( r2*C1 + r1*C2 ) ); return res; }
  if (is_zero(r1-r2-d)) { res.push_back( C1 + (r1/d) * (C2-C1) ); return res; }
  if (is_zero(r2-r1-d)) { res.push_back( C2 + (r2/d) * (C1-C2) ); return res; }
  // general case: compute x and y offset of the intersections    
  T x = ( d*d - r2*r2 + r1*r1 ) / (2*d);
  T y = sqrt( 4*d*d*r1*r1 - ( d*d - r2*r2 + r1*r1 )*( d*d - r2*r2 + r1*r1 ) ) / (2*d);
  // I = (C1,C2) \cap chord, N = normal vector
  complex<T> I = (1.0/d) * ( (d-x)*C1 + x*C2 );
  complex<T> N( imag(C2-C1), -real(C2-C1) );
  T Nsize = sqrt(square_size(N));
  N = N * (1/Nsize);
  // compute and return the points in lexicographic order
  complex<T> I1 = I + y*N, I2 = I - y*N;
  if (is_positive(real(I1)-real(I2))) swap(I1,I2);
  if (is_zero(real(I1)-real(I2))) if (is_positive(imag(I1)-imag(I2))) swap(I1,I2);
  res.push_back(I1);
  res.push_back(I2);
  return res;
}



int N;
vector<double> X, Y, R;

/*
bool can_cover_single(double radius, long long which) {
  // if at most one remains, we are done
  if (which == 0) return true;
  REP(n,N) if (which == (1LL << n)) return true;
  // general case: the second circle covers at least two
  REP(n1,N) if (which & 1LL << n1) REP(n2,n1) if (which & 1LL << n2) {
    // construct at most 2 circles that have n1 and n2 on the boundary
    vector<point> centers = intersect_circle_circle( point( X[n1], Y[n1] ), radius - R[n1], point( X[n2], Y[n2] ), radius - R[n2] );
    FOREACH(cit,centers) {
      point C = *cit;
      bool good = true;
      REP(n,N) if (which & 1LL << n) if ( ! ( size( C - point( X[n], Y[n] ) ) + R[n] < radius + EPSILON ) ) { good = false; break; }
      if (good) return true;
    }
  }
  return false;
}
*/

bool can_cover_single(double radius, long long which) {
  vector<int> Z;
  REP(n,N) if (which & 1LL << n) Z.push_back(n);

  // if at most one remains, we are done
  if (SIZE(Z) <= 1) return true;
  // general case: the second circle covers at least two
  REP(x1,SIZE(Z)) REP(y1,x1) {
    int n1 = Z[x1], n2 = Z[y1];
    // construct at most 2 circles that have n1 and n2 on the boundary
    vector<point> centers = intersect_circle_circle( point( X[n1], Y[n1] ), radius - R[n1], point( X[n2], Y[n2] ), radius - R[n2] );
    FOREACH(cit,centers) {
      point C = *cit;
      bool good = true;
      REP(z1,SIZE(Z)) {
        int n = Z[z1];
        if ( ! ( size( C - point( X[n], Y[n] ) ) + R[n] < radius + EPSILON ) ) { good = false; break; }
      }
      if (good) return true;
    }
  }
  return false;
}

bool can_cover_all(double radius) {
  // basic check
  REP(n,N) if (R[n] > radius) return false;
  // special case: the first circle covers only one circle
  REP(n,N) {
    long long rest = (1LL << N) - 1;
    rest ^= 1LL << n;
    if (can_cover_single(radius,rest)) return true;
  }
  // general case: the first circle covers at least two
  REP(n1,N) REP(n2,n1) {
    // construct at most 2 circles that have n1 and n2 on the boundary
    vector<point> centers = intersect_circle_circle( point( X[n1], Y[n1] ), radius - R[n1], point( X[n2], Y[n2] ), radius - R[n2] );
    FOREACH(cit,centers) {
      point C = *cit;
      long long rest = (1LL << N) - 1;
      REP(n,N) if ( size( C - point( X[n], Y[n] ) ) + R[n] < radius + EPSILON ) rest ^= 1LL << n;
      if (can_cover_single(radius,rest)) return true;
    }
  }
  return false;
}

int main() {
  int T;
  cin >> T;
  FOR(t,1,T) {
    cin >> N;
    X.clear(); X.resize(N);
    Y.clear(); Y.resize(N);
    R.clear(); R.resize(N);
    REP(n,N) cin >> X[n] >> Y[n] >> R[n];

    if (N==1) {
      double best = R[0];
      printf("Case #%d: %.10f\n",t,best);
      continue;
    }
    if (N==2) {
      double best = max( R[0], R[1] );
      printf("Case #%d: %.10f\n",t,best);
      continue;
    }
    /*
    if (N==3) {
      double best = max( R[0], solve(1,2) );
      best = min( best, max( R[1], solve(0,2) ) );
      best = min( best, max( R[2], solve(0,1) ) );
      printf("Case #%d: %.10f\n",t,best);
      continue;
    }
    */
    
    double lo = 0, hi = 2000;
    REP(loop,70) {
      double mid = (lo + hi) / 2;
      if (can_cover_all(mid)) hi = mid; else lo = mid;
    }
    printf("Case #%d: %.10f\n",t,lo);
  }
  return 0;
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
