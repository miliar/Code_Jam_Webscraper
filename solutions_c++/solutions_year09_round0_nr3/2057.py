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

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
LL s2i(string s) { istringstream i(s); LL x; i>>x; return x; }
template<class T> string i2s(T x) { ostringstream o; o << x; return o.str(); }

#define	MIN(a, b)	((a) < (b) ? (a) : (b))
#define MAX(a, b) ((a) > (b) ? (a) : (b))

#define small

#ifdef small
	#define	FILE_IN		"C-small.in"
	#define FILE_OUT	"C-small.out"
#endif
#ifndef small
	#define	FILE_IN		"C-large.in"
	#define FILE_OUT	"C-large.out"
#endif

string code = "welcome to code jam" ;
int d [505] [25], cur [25] ;

string form(int n) {
  ostringstream out ;
  if (n >= 1000) out << n ;
  if (n >= 100 && n < 1000) out << "0" << n ;
  if (n >= 10 && n < 100) out << "00" << n ;
  if (n >= 0 && n < 10) out << "000" << n ;
  return out.str() ;
}

int main(int argc, char **argv) {
	ifstream in(FILE_IN) ;
	ofstream out(FILE_OUT) ;

  int num_tests ;
	in >> num_tests ;
	string line ;
	getline(in, line) ;
	for (int test = 1 ; test <= num_tests ; test ++) {
    getline(in, line) ;
    memset(cur, 0, sizeof(cur)) ;
    for (int i = line.size() - 1 ; i >= 0 ; i --) {
      for (int j = 0 ; j < code.size() ; j ++)
        if (line [i] == code [j])
          if (j < code.size() - 1)
            cur [j] = (cur [j] + cur [j + 1]) % 10000 ;
          else
            cur [j] ++ ;
    }
    
		out << "Case #" << test << ": " << form(cur [0]) << endl ;
	}
		
	in.close() ;
	out.close() ;
}
