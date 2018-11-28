// {{{ Boilerplate Code <--------------------------------------------------

#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

#define   FOR(i, a, b)    for ( typeof(a) i = (a) ; i < (b) ; ++i )
#define   REP(i, n)       FOR(i, 0, n)
#define   ALL(a)          (a).begin(), (a).end()

using namespace std;

typedef pair< int, int >  ii;
typedef long long         ll;

// }}}

int countDigits(int n)
{
  int ndigits = 0;

  while ( n > 0 )
  {
    n /= 10;
    ++ndigits;
  }

  return ndigits;
}

// @param i digits to put in front
int putInFront(int n, int i)
{
  int tmp = 0, digit;

  //cout << ">>>> putInFront(" << n << ", " << i << ") = ";
  REP(j, i)
  {
    digit = n % 10;
    n    /= 10;
    REP(k, j) digit *= 10;
    tmp += digit;
  }

  REP(j, countDigits(n))
    tmp *= 10;

  //cout << tmp+n << endl;

  return tmp + n;
}

bool isRecycled(int n, int m)
{
  //cout << ">>>> isRecycled(" << n << ", " << m << ")" << endl;

  if ( n == m )
    return false;

  int nd = countDigits(n), md = countDigits(m);

  //cout << ">>>> nd = " << nd << " md = " << md << endl;

  if ( nd != md )
    return false;

  for ( int i = 1 ; i <= nd-1 ; ++i )
    if ( putInFront(n, i) == m )
      return true;

  return false;
}

int main()
{
  int T, A, B, n, m;
  ll ret;

  scanf("%d\n", &T);

  REP(t, T)
  {
    scanf("%d %d\n", &A, &B);

    ret = 0;
    for ( n = A ; n <= B ; ++n )
      for ( m = n+1 ; m <= B ; ++m )
	if ( isRecycled(n, m) )
	  ++ret;
    
    printf("Case #%d: %lld\n", t+1, ret);
  }

  return 0;
}
