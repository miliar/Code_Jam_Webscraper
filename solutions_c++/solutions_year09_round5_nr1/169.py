#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <complex>
#include <cstdio>
#include <cassert>
#include <cmath>

using namespace std;

#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;i++)
#define REP(i,n) FOR(i,0,(n)-1)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define sz size()
template<class T> inline int size(const T& c) { return c.sz; }
#define FORA(i,c) REP(i,size(c))

#define itype(c) __typeof((c).begin())
#define FORE(e,c) for(itype(c) e=(c).begin();e!=(c).end();e++)
#define pb push_back
#define X first
#define Y second
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define SORT(x) sort(all(x))
#define REVERSE(x) reverse(all(x))
#define CLEAR(x,c) memset(x,c,sizeof(x)) 

typedef unsigned 
long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
LL s2i(string s) { istringstream i(s); LL x; i>>x; return x; }
template<class T> string i2s(T x) { ostringstream o; o << x; return o.str(); }

#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define MAX(a, b) ((a) > (b) ? (a) : (b))

#define eps 1e-9
#define gr(a, b) ((a) > (b) + eps)
#define ge(a, b) ((a) > (b) - eps)
#define le(a, b) ((a) < (b) + eps)
#define ls(a, b) ((a) < (b) - eps)
#define eq(a, b) ((a) > (b) - eps && (a) < (b) + eps) 


string FILE_IN, FILE_OUT ;

void setName() {
  string comm ;
  cin >> comm ;
  FILE_IN = "A-small.in" ;
  FILE_OUT = "A-small.out" ;
  if (comm [0] == 'l' || comm [0] == 'L') {
    FILE_IN = "A-large.in" ;
    FILE_OUT = "A-large.out" ; 
  }
}

int dr [4] = {0, 1, 0, -1} ;
int dc [4] = {1, 0, -1, 0} ;

#define is_box(ch) ((ch) == 'o' || (ch) == 'w')
#define is_empty(ch) ((ch) == '.' || (ch) == 'x')

typedef pair<int, int> pint ;

string row [14] ;
int numRow, numCol, cnt ;
map<VS, int> d ;
map<VS, bool> danger ;

bool final(VS f) {
  for (int r = 0 ; r < numRow ; r ++) {
    for (int c = 0 ; c < numCol ; c ++) {
      if (f [r] [c] == 'o') return false ;
    }
  }
  return true ;
}

bool can(int way, int r, int c, int &nr, int &nc) {
  nr = r + dr [way] ;
  nc = c + dc [way] ;
  return (nr >= 0 && nr < numRow && nc >= 0 && nc < numCol) ;  
}

bool dangerous(VS f) {
  bool found = false ;
  int nr, nc ;
  vector<pint> v ;
  for (int r = 0 ; r < numRow && !found ; r ++) {
    for (int c = 0 ; c < numCol && !found ; c ++) {
      if (is_box(f [r] [c])) {
        v.push_back(pint(r, c)) ;
        found = true ;
      }
    }
  }
  int i = 0 ;
  while (i < v.size()) {
    int r = v [i].first, c = v [i].second ;
    for (int way = 0 ; way < 4 ; way ++)
      if (can(way, r, c, nr, nc) && is_box(f [nr] [nc])) {
        pint next(nr, nc) ;
        bool ok = true ;
        for (int j = 0 ; j < v.size() && ok ; j ++)
          if (v [j] == next) ok = false ;
        if (ok) v.push_back(next) ;
      }
    i ++ ;
  }
  //cout << "dangerous(): " << v.size() << ", " << cnt << endl ;
  return v.size() < cnt ;
}

bool move(int way, int r, int c, VS &f) {
  if (is_box(f [r] [c])) {
    int fwr, fwc, bwr, bwc ;
    if (can(way, r, c, fwr, fwc)) {
      if (is_empty(f [fwr] [fwc])) {
        if (can((way + 2) % 4, r, c, bwr, bwc)) {
          if (is_empty(f [bwr] [bwc])) {
            if (f [r] [c] == 'o') f [r] [c] = '.' ;
            if (f [r] [c] == 'w') f [r] [c] = 'x' ;
            if (f [fwr] [fwc] == '.') f [fwr] [fwc] = 'o' ;
            if (f [fwr] [fwc] == 'x') f [fwr] [fwc] = 'w' ;
            return true ;
          }
        }
      }
    }
  }
  return false ;
}

void undo(int way, int r, int c, VS &f) {
  int fwr, fwc, bwr, bwc ;
  if (can(way, r, c, fwr, fwc)) {
    if (f [r] [c] == '.') f [r] [c] = 'o' ;
    if (f [r] [c] == 'x') f [r] [c] = 'w' ;
    if (f [fwr] [fwc] == 'o') f [fwr] [fwc] = '.' ;
    if (f [fwr] [fwc] == 'w') f [fwr] [fwc] = 'x' ;
  }   
}

int main(int argc, char **argv) {
  setName() ;     
  ifstream in(FILE_IN.c_str()) ;
  ofstream out(FILE_OUT.c_str()) ;
  
  string line ;
  istringstream is ;

  int numTest ;
  in >> numTest ;
  
  for (int test = 1 ; test <= numTest ; test ++) {
    in >> numRow >> numCol ;    
    VS f ;
    string curRow ;
    for (int r = 0 ; r < numRow ; r ++) {
      in >> curRow ;
      f.push_back(curRow) ;
    }
    cnt = 0 ; 
    for (int r = 0 ; r < numRow ; r ++)
      for (int c = 0 ; c < numCol ; c ++)
        if (f [r] [c] == 'o' || f [r] [c] == 'w')
          cnt ++ ;
    queue<VS> q ;
    d [f] = 0 ;
    danger [f] = dangerous(f) ;
    
    q.push(f) ;
    int bestDis = -1 ;
    bool ok = false;
    while (!q.empty() && !ok) {
      VS curMap = q.front() ; q.pop() ;
      bool isDanger = danger [curMap] ;
      int curDis = d [curMap] ;
      //out << "CURRENT DISTANCE " << curDis << ", " << isDanger << ", " << final(curMap) << endl ;
      //for (int r = 0 ; r < numRow ; r ++) out << curMap [r] << endl ;
      if (final(curMap)) { bestDis = curDis ; ok = true ; }
      else {        
        for (int r = 0 ; r < numRow ; r ++) {
          for (int c = 0 ; c < numCol ; c ++) {
            if (is_box(curMap [r] [c])) {              
              for (int way = 0 ; way < 4 ; way ++) {
                if (move(way, r, c, curMap)) {
                  //out << "moving from: " << r << ", " << c << ", " << way << ", danger = " << dangerous(curMap) << ", map = " << d.count(curMap) << endl ;
                  //for (int ir = 0 ; ir < numRow ; ir ++) out << curMap [ir] << endl ;
                  if (d.count(curMap) == 0) {
                    danger [curMap] = dangerous(curMap) ;
                    d [curMap] = curDis + 1 ;
                    if (!isDanger || !danger [curMap]) {
                      //out << "PUSHING!" << endl ;
                      q.push(curMap) ;
                    }
                  }                                    
                  undo(way, r, c, curMap) ;                  
                  //out << "undo: " << r << ", " << c << endl ;
                  //for (int ir = 0 ; ir < numRow ; ir ++) out << curMap [ir] << endl ;
                }
              }
            }
          }
        }        
      }
    }
    
    out << "Case #" << test << ": " << bestDis << endl ;
  }
  
  in.close() ;
  out.close() ;
}
