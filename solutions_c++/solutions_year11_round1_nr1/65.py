#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>

#define fo(a,b,c) for (a=(b); a<(c); ++a)
#define fr(a,b) fo(a,0,(b))
#define fi(a) fr(i,(a))
#define fj(a) fr(j,(a))
#define fk(a) fr(k,(a))
#define mp make_pair
#define pb push_back
#define all(v) (v).begin( ), (v).end( )
#define _(a,b) memset( a, b, sizeof( a ) )
using namespace std;
int ni() { int a; scanf( "%d", &a ); return a; }
double nf() { double a; scanf( "%lf", &a ); return a; }
char sbuf[100005]; string ns() { scanf( "%s", sbuf ); return sbuf; }
long long nll() { long long a; scanf( "%lld", &a ); return a; }

template <class T> void out( T a, T b ) { bool first = true; for( T i = a; i != b; ++ i ) { if( !first ) printf( " " ); first = false; cout << * i; } printf( "\n" ); }
template <class T> void outl( T a, T b ) { for( T i = a; i != b; ++ i ) { cout << * i << "\n"; } }
typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef map<string,int> msi;

int n, m;

int main() {
  int i, j, k, t, tt;
  tt = ni();
  for (t = 1; t <= tt; ++t) {
    printf("Case #%d: ", t);
    
    long long N = nll(), Pd = nll(), Pg = nll();
    long long a = Pd, b = 100;
    long long c = Pg, d = 100;
    while (a % 5 == 0 && b % 5 == 0) {
      a /= 5;
      b /= 5;
    }
    while (a % 2 == 0 && b % 2 == 0) {
      a /= 2;
      b /= 2;
    }
    while (c % 5 == 0 && d % 5 == 0) {
      c /= 5;
      d /= 5;
    }
    while (c % 2 == 0 && d % 2 == 0) {
      c /= 2;
      d /= 2;
    }
    if (b > N || (c == 0 && a > 0) || (c == d && a < b)) {
      printf("Broken\n");
    } else {
      printf("Possible\n");
    }
  }
  return 0;
}
