#include <cstdio>
#include <cstring>
#include <string>
#include <iostream>
#include <algorithm>
#include <vector>
#include <bitset>
#include <set>
#include <deque>
#include <boost/unordered_map.hpp>

using namespace std;
#define AUTO(a, b) typeof(b) a = (b)

typedef unsigned long long ull;
typedef unsigned uint;

int const N = 1000000;
int sieve [N+1];
int np    [N+1];
int pi    [N+1];
int pr    [N+1];
int tot   [N+1];

ull solve(ull n)
{
  if( n == 1 )
    return 0;
  
  memset(tot, 0, sizeof(tot));
  int m = np[N];
  for( int i = 0; i != m; ++i )
  {
    int p = pr[i];
    ull q = n;
    while( q /= p )
      ++tot[i];
  }
  ull mx = 1, mn = 0;

  for( int i = 0; i < m && tot[i] > 0; ++i )
    mx += tot[i];
  for( int i = 0; i < m && tot[i] > 0; )
  {
    ++mn;
    ull prod = 1;
    while( i < m && tot[i] > 0 )
    {
      ull cur = pow(ull(pr[i]), tot[i]);
      if( prod > n/cur )
        break;
      else
      {
        prod *= cur;
        ++i;
      }
    }
  }

  return mx - mn;
}

void init()
{
  sieve[1] = 1;
  int p = 2;
  for( ; p*p <= N; ++p )
  {
    np[p] = np[p-1];
    if( !sieve[p] )
    {
      pr[np[p]] = p;
      pi[p] = np[p]++;
      for( int q = p*p; q <= N; q += p )
        sieve[q] = p;
    }
  }
  for( ; p <= N; ++p )
  {
    np[p] = np[p-1];
    if( !sieve[p] )
    {
      pr[np[p]] = p;
      pi[p] = np[p]++;
    }
  }
}


int main()
{
  cin.sync_with_stdio(false);
  init();
  
  int T;
  cin >> T;
  for( int C = 1; C <= T; C++ )
  {
    ull n;
    cin >> n;    
    ull rv = solve(n);
    
    cout << "Case #" << C << ": " << rv << '\n';
  }
  return 0;
}