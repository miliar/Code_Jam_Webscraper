#include <iostream>
#include <string>
#include <map>
using namespace std ;

#define FILEIO

int main( void )
{
#ifdef FILEIO
  freopen( "A-large.in", "r", stdin ) ;
  freopen( "A-l.out", "w", stdout ) ;
#endif

  int N, S, Q ;
  cin >> N ;

  string searchengine[101] ;
  map<string, int> searchmap ;
  bool used[101] ;
  int casenum = 1 ;
  int re = 0 ;
  while ( N-- ){
    re = 0 ;
    cin >> S ;
    getline( cin, searchengine[0]) ;
    for ( int i = 0 ; i < S ; ++i ){
      getline(cin, searchengine[i]) ;
      //cout << searchengine[i] << endl ; // debug
      searchmap[searchengine[i]] = i ;
    }
    string query ;
    int usednum = 0 ;
    memset( used, 0, S ) ;
    //cout << sizeof(used) << endl ;
    cin >> Q ;
    getline( cin, query ) ;
    for ( int i = 0 ; i < Q ; ++i ){
      getline(cin, query) ;
      //cout << query << endl ; //debug
      int pos = searchmap[query] ;
      if ( used[pos] == false ){
	used[pos ] = true ;
	++usednum ;
      }
      if ( usednum == S ){
	++re ;
	memset(used, 0, S) ;
	used[pos] = true ;
	usednum = 1 ;
      }
    }
    cout << "Case #" << casenum++ << ": " << re << endl ;
  }

  return 0 ;
}
