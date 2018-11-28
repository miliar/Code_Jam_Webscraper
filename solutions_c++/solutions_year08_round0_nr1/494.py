#include "debug.h"
#include <iostream>
#include <cstdio>

using namespace std;

vector< string > trazilice;
vector <string> queries;

map < pair<int,int>, int > memo;

int rek( int tren, int tq) {
  if ( trazilice[tren] == queries[tq]) return INF;
  if (tq == 0) return 0;
  
  if ( memo.count( make_pair(tren, tq) ) != 0)
     return memo[ make_pair(tren, tq) ];
  
  //inace u prethodnom koraku stavi bilo koji
  int rj = INF;
  for(int i=0; i<trazilice.size(); i++) {
    if (tren != i) rj <?= rek( i, tq - 1 ) + 1;
    else           rj <?= rek( i, tq - 1 );    
  }  
  
  memo[ make_pair(tren, tq) ] = rj;
  return rj;
}  

int solve(void) {
  memo.clear();
  trazilice.clear();
  queries.clear();
  int q, t; string tmp;
  
  scanf("%d\n", &t);
//  debug( t );
  
  for(int i=0; i<t; i++) {
    getline( cin, tmp );
    trazilice.push_back( tmp ) ;
  }  
  
  scanf("%d\n", &q);
  if (q == 0) return 0;
//  debug(q);
  
  for(int i=0; i<q; i++) {
     getline( cin, tmp );
     queries.push_back( tmp );
  }  
  
  //debug( trazilice );
  //debug( queries );
  
  int rj = INF;
  for(int i=0; i<trazilice.size(); i++) 
    rj <?= rek( i, queries.size() - 1 );
    
  return rj;
}  

int main(void) {
  int n;
  cin >> n;

  for(int i=0; i<n; i++)  
    cout << "Case #" << (i + 1) << ": " << solve() << endl;
  return 0;
}

