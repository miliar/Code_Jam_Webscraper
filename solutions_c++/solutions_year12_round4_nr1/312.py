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

#define FOR(i,a,b) for (int i=(a); i<(b); ++i)
#define FORZ(i,b) FOR(i,0,(b))
#define mp make_pair
#define pb push_back
#define all(v) (v).begin( ), (v).end( )
#define _(a,b) memset( a, b, sizeof( a ) )
using namespace std;

template <class T> void out( T a, T b ) { bool first = true; for( T i = a; i != b; ++ i ) { if( !first ) printf( " " ); first = false; cout << * i; } printf( "\n" ); }
template <class T> void outl( T a, T b ) { for( T i = a; i != b; ++ i ) { cout << * i << "\n"; } }
typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef map<string,int> msi;

enum{INF=1000000001};
int N,D;
int d[10000];
int l[10000];
int sl[10000];

int main() {
  int tt;
  cin >> tt;
  FOR(t,1,tt+1) {
    printf("Case #%d: ", t);
    cin >> N;
    FORZ(i,N) cin >> d[i] >> l[i];
    FORZ(i,N) sl[i] = INF;
    cin >> D;
    for (int i = N-1; i >= 0; --i) {
      if (D - d[i] <= l[i]) sl[i] = D - d[i];
      for (int j = N-1; j > i; --j) {
        if (d[j] - d[i] >= sl[j] && d[j] - d[i] <= l[i])
          sl[i] = min(sl[i], d[j] - d[i]);
      }
    }
    cout << ((d[0] >= sl[0]) ? "YES" : "NO") << endl;
  }
  return 0;
}
