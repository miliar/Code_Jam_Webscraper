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

vi L;
vi P;

bool l(int a, int b) {
  return L[a]*P[b] < L[b]*P[a];
}

int main() {
  int tt;
  cin >> tt;
  FOR(t,1,tt+1) {
    printf("Case #%d:", t);
    int N;
    cin >> N;
    L.resize(N);
    P.resize(N);
    FORZ(i,N) cin >> L[i];
    FORZ(i,N) cin >> P[i];
    vi idx(N);
    FORZ(i,N) idx[i] = i;
    stable_sort(idx.begin(),idx.end(),l);
    FORZ(i,N) cout << " " << idx[i];
    cout << endl;
  }
  return 0;
}
