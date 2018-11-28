#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cctype>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <numeric>
#include <cmath>
using namespace std;

typedef long long LL;
typedef vector< LL > VLL;
typedef pair< LL, LL > PLL;
typedef vector< PLL > VPLL;
typedef vector< bool > VB;
typedef vector< int > VI;
typedef vector< double > VD;
typedef vector< string > VS;
#define PUSH push_back
#define POP pop_back

LL P, K, L;
VLL press;
LL result;

void read ()
{
  int i, j;
  cin >> P >> K >> L;
  
  LL n;
  for ( i = 0; i < L; i++ )
  {
    cin >> n;
    press.PUSH( n );
  }
}

void solve ()
{
  LL i, j, k, max = 0, col = 1, row = 1;
  for ( i = 0; i < L; i++ )
  {
    for ( j = 0; j < L; j++ )
      if ( press[j] > max )
      {
        k   = j;
        max = press[j];
      }
    
    result += press[k] * col;
    press[k] = 0;
    max = 0;
    
    if ( ++row > K )
    {
      col++;
      row = 1;
    }
  }
}

int main ()
{
  freopen( "A-large.in",  "r", stdin );
  freopen( "A-large.out", "w", stdout );

  int N;
  cin >> N;
  for ( int i = 0; ++i <= N; )
  {
    press.clear();
    result = 0;
    
    read();
	solve();
 	cout << "Case #" << i << ": " << result << "\n";
  }

  exit(0);
}
