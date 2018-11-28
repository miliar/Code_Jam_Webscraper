/**
* Template C++ source file for programming contests
* Author: Abraham Max Santos Ramos
*/

// header files
#include <algorithm>
#include <bitset>
//#include <complex>
#include <deque>
//#include <exception>
//#include <fstream>
#include <functional>
//#include <hash_map>
//#include <hash_set>
#include <iomanip>
//#include <ios>
//#include <iosfwd>
#include <iostream>
//#include <iso646.h>
//#include <istream>
#include <iterator>
#include <limits>
#include <list>
//#include <locale>
#include <map>
//#include <memory>
//#include <new>
#include <numeric>
//#include <ostream>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
//#include <stdexcept>
//#include <streambuf>
#include <string>
//#include <strstream>
#include <utility>
#include <valarray>
#include <vector>
#include <cassert>
#include <cctype>
//#include <cerrno>
//#include <cfloat>
//#include <ciso646>
//#include <climits>
//#include <clocale>
#include <cmath>
//#include <csetjmp>
//#include <csignal>
//#include <cstdarg>
//#include <cstddef>
#include <cstdio>
#include <cstdlib>
#include <cstring>
//#include <ctime>
//#include <cwchar>
//#include <cwctype>

using namespace std;

// macros, templates and inline functions
#define iter iterator
#define citer const_iterator
#define all(x) (x).begin(), (x).end()

#define REP(i,s,t) for ( int i = (s); i < (t); i++ )
#define DREP(i,s,t) for ( int i = (t)-1; i >= (s); i-- )
#define FOR(i,s,t) for ( int i = (s); i <= (t); i++ )
#define DFOR(i,s,t) for ( int i = (t); i >= (s); i-- )
#define FOREACH(it,A) for ( it = A.begin(); it != A.end(); it++ )

typedef int coord;

struct point {
   coord x, y;
   point(coord _x, coord _y) : x(_x), y(_y) {}
};

template<typename __T> inline
void setmin(__T &a, const __T &b) { if ( b < a ) a = b; }
template<typename __T> inline
void setmax(__T &a, const __T &b) { if ( b > a ) a = b; }

// typedefs
typedef pair<int,int> intpair;

typedef deque<int> deqint;
typedef deque<double> deqdbl;
typedef deque<string> deqstr;

typedef list<int> lstint;
typedef list<double> lstdbl;
typedef list<string> lststr;

typedef map<int,int> mapint;
typedef map<string, int> mapstr;

typedef queue<int> queint;
typedef queue<double> quedbl;
typedef queue<string> questr;

typedef set<int> setint;
typedef set<double> setdbl;
typedef set<string> setstr;

typedef stack<int> stkint;
typedef stack<double> stkdbl;
typedef stack<string> stkstr;

typedef valarray<int> arrint;
typedef valarray<double> arrdbl;
typedef valarray<string> arrstr;

typedef vector<int> vecint;
typedef vector<double> vecdbl;
typedef vector<string> vecstr;
typedef vector<vecint> matint;
typedef vector<vecdbl> matdbl;
typedef vector<string> matstr;

//constants
const char nl = '\n';
const int Inf = numeric_limits<int>::max();

#include <iostream>
#include <valarray>
#include <utility>
#include <cmath>

using namespace std;
typedef valarray<int> IntArray;
vecint prims;

class DisjointSet {
public:
   DisjointSet(int n)
      : rank(n), parent(n), size(n), maxset(n ? 1: 0), 
      nsets(n)
   {
      for ( int i = 0; i < n; i++ ) {
         rank[i] = 0;
         parent[i] = i;
         size[i] = 1;
      }
   }

   void link(int x, int y) {
      int newsize = size[x] + size[y];
      maxset = max(newsize, maxset);
      if ( rank[x] > rank[y] ) {
         parent[y] = x;
         size[x] = newsize;
      } else {
         parent[x] = y;
         size[y] = newsize;
         if ( rank[x] == rank[y] )
            ++rank[y];
      }
      --nsets;
   }

   int find_set(int x) {
      int stack[10];
      int count = 0;
      while ( x != parent[x] ) {
         stack[count++] = x;
         x = parent[x];
      }
      while ( count )
         parent[stack[--count]] = x;
      return x;
   }

   void union_set(int x, int y) {
      int parx = find_set(x);
      int pary = find_set(y);
      if ( parx != pary )
         link(parx, pary);
   }

   int max_size() const { return maxset; }
   int num_sets() const { return nsets; }

private:
   IntArray    rank;
   IntArray    parent;
   IntArray    size;
   int         maxset;
   int         nsets;
};

int GCD(int a, int b)
{
   while ( b != 0 ) {
      a %= b;
      swap(a, b);
   }
   return a;
}

void make_primes(vecint &primes, int lim)
{
   primes.push_back(2);
   for ( int i = 3; i < lim; i += 2 )
      for ( int j = 0; ; j++ ) {
         if ( i % primes[j] == 0 )
            break;
         if ( primes[j]*primes[j] > i ) {
            primes.push_back(i);
            break;
         }
      }
}

int max_factor(int n)
{
   if ( n == 1 ) return 1;
   int v = 2;
   for ( int i = 0; n != 1; i++ )
      while ( n % prims[i] == 0 ) {
         n /= prims[i];
         v = prims[i];
      }
   return v;
}

int main()
{
   int C;
   cin >> C;

   make_primes(prims, 1010);
   FOR(m,1,C) {
      int A, B, P;
      cin >> A >> B >> P;

      DisjointSet DS(B-A+1);
      //cerr << "Numsets: " << DS.num_sets() << nl;
      FOR(i,A,B)
         FOR(j,i+1,B) {
            int gcd = GCD(i,j);
            int x = max_factor(GCD(i,j));
            //cerr << "Max Factor GCD(" << i << ',' << j << ") = " << x << nl;
            if ( x >= P ) {
               //cerr << "Link between " << i << ' ' << j << nl;
               DS.union_set(i-A, j-A);
            }
         }
      cout << "Case #" << m << ": " << DS.num_sets() << nl;
   }
   return 0;
}
