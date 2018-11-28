#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <set>
#include <map>
#include <vector>
#include <numeric>
#include <queue>
#include <string>
#include <algorithm>
using namespace std ;

#define FILEIO
#define DEBUG

#define _CRT_SECURE_NO_WARNINGS
#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define Repd(i,n) for (int i((n)-1); i >= 0; --i)
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))
#define All(v) (v).begin(), (v).end()


int main( void )
{
#ifdef FILEIO
  freopen( "in-l.in", "r", stdin ) ;
  freopen( "out-l.txt", "w", stdout ) ;
#endif

  int T ;
  cin >> T ;
  int case_counter = 1 ;
  while( T-- ){
    int n ;
    cin >> n ;
    vector<int> s1, s2 ;
    for ( int i = 0 ; i < n ; ++i ){
      int n1 ;
      cin >> n1 ;
      s1.push_back(n1) ;
    }
    for ( int i = 0 ; i < n ; ++i ){
      int n1 ;
      cin >> n1 ;
      s2.push_back(n1) ;
    }
    sort( s1.begin(), s1.end(), less<int>() ) ;
    sort( s2.begin(), s2.end(), greater<int>() ) ;
    long long re = 0 ;
    //int len = s1.size() ;
    for ( int i = 0 ; i < n ; ++i ){
#ifdef DEBUG1
      cout << s1[i] << " " << s2[i] << endl ;
#endif
      re += (long long)(s1[i])*(long long)(s2[i]) ;
    }
    cout << "Case #" << case_counter++ << ": " << re << endl ;
  }

  return 0 ;
}
