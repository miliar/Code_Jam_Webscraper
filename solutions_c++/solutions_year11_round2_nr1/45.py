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

int n;
char s[110];
int a[110][110];
double wp[110], owp[110], oowp[110];

void solve() {
  scanf( "%d", &n );
  forn( i, n ) {
    scanf( "%s", s );
    forn( j, n )
      if ( s[j] != '.' ) a[i][j] = s[j] - '0';
      else a[i][j] = -1;
  }

  forn( i, n ) {
    wp[i] = 0;
    int cnt = 0;
    forn( j, n )
      if ( a[i][j] != -1 ) {
        cnt++;
        wp[i] += a[i][j];
      }
    if ( cnt != 0 ) wp[i] /= cnt;
  }

  forn( q, n ) {
    owp[q] = 0;
    int cq = 0;
    forn( i, n ) 
      if ( a[i][q] != -1 ) {
        double _wp = 0;
        int cnt = 0;
        forn( j, n )
          if ( a[i][j] != -1 && j != q ) {
            cnt++;
            _wp += a[i][j];
          }
        if ( cnt != 0 ) _wp /= cnt;
        cq++;
        owp[q] += _wp;
      }
    if ( cq != 0 ) owp[q] /= cq;
  }

  forn( i, n ) {
    oowp[i] = 0;
    int cnt = 0;
    forn( j, n )
      if ( j != i && a[i][j] != -1 ) {
        oowp[i] += owp[j];
        cnt++;
      }
    if ( cnt != 0 ) oowp[i] /= cnt;
  }

  forn( i, n ) {
//    printf( "> %.5f %.5f %.5f\n", wp[i], owp[i], oowp[i] );
    printf( "%.10f\n", 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i] );
  }
}

int main()
{
  int tc;
  scanf( "%d", &tc );
  for ( int q=1; q<=tc; q++ ) {
    printf( "Case #%d:\n", q );
    solve();
  }
  return 0;
}