#include <cstdio>
#include <string>
#include <vector>
#include <memory.h>
#include <cstring>
#include <ctime>
#include <cmath>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

#define forn( i,n ) for ( int i=0; i<(int)(n); i++ )
#define pb push_back
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;

const int N = (int)1e6 + 5;

bool u[N+5];
ll n;
vector<int> pp;

void solve() {
  scanf( "%I64d", &n );

  if ( n == 1 ) {
    printf( "0\n" );
    return;
  }

  int res = 1;
  forn( i, pp.size() ) {
    ll x = pp[i];
    while ( true ) {
      x *= pp[i];
      if ( x <= n ) res++;
      else break;
    }
  }

  printf( "%d\n", res );
}

void primes() {
  for ( int i=2; i<=N; i++ )
    if ( !u[i] ) {
      pp.pb( i );
      for ( ll j=(ll)i*i; j <= N; j += i )
        u[j] = 1;
    }
  fprintf( stderr, "pp.size() = %d\n", pp.size() );
}

int main()
{
  primes();
  int tc;
  scanf( "%d", &tc );
  for ( int q=1; q<=tc; q++ ) {
    fprintf( stderr, "test %d\n", q );
    printf( "Case #%d: ", q );
    solve();
  }
  return 0;
}