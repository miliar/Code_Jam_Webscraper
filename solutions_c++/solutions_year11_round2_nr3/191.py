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

int u[10];
int v[10];
int r[10];
int q;
int inv[10];
int cover[1<<10];
int allq;
int const INF = 1<<29;

bool seen[1<<10];
int mem[1<<10];
int best[1<<10];

int solve(int a)
{
  if( a == 0 )
    return 0;
  
  int& rv = mem[a];
  if( seen[a] )
    return rv;
  seen[a] = true;
  rv = 0;
  
  for( int s = a; s; s = (s-1)&a )
  {
    //cerr << "Taking " << s << " from " << a << endl;
    if( cover[s] != allq )
      continue;
    int r = 1 + solve(a ^ s);
    if( r > rv )
    {
      rv = r;
      best[a] = s;
    }
  }
  return rv;
}

int sol[10];
void rebuild(int s)
{
  int c = 0;
  while( s )
  {
    ++c;
    int b = best[s];
    s ^= b;
    while( b )
    {
      int bi = __builtin_ctz(b);
      sol[bi] = c;
      b ^= (1<<bi);
    }
  }
}

int main()
{
  cin.sync_with_stdio(false);
  
  int T;
  cin >> T;
  for( int C = 1; C <= T; C++ )
  {
    int n, m;
    cin >> n >> m;
    for( int i = 0; i != m; ++i )
    {
      cin >> u[i];
      --u[i];
    }
    for( int i = 0; i != m; ++i )
    {
      cin >> v[i];
      --v[i];
    }
    q     = 1;
    r[0]  = (1<<n)-1;
    
    for( int i = 0; i != m; ++i )
    {
      int used = (1<<u[i])|(1<<v[i]);
      for( int j = 0; j != q; ++j )
      {
        if( (r[j] & used) == used )
        {
          int other = (1<<(v[i]-u[i]+1))-1;
          other <<= u[i];
          other &= r[j];
          r[q++] = other;
          r[j] &= ~other;
          r[j] |= used;
          break;
        }
      }
    }
    
    memset(inv, 0, sizeof(inv));
    for( int i = 0; i != q; ++i )
    {
      for( int s = r[i]; s; )
      {
        int b = __builtin_ctz(s);
        inv[b] |= (1<<i);
        s ^= (1<<b);
        //cout << "Region " << i << " has vertex " << b << endl;
      }
    }
    //for( int i = 0; i != n; ++i )
    //  cout << "Vertex " <<i << " covers " << inv[i] << endl;
    memset(cover, 0, sizeof(cover));
    for( int i = 1, t = (1<<n); i != t; ++i )
    {
      int b = __builtin_ctz(i);
      cover[i] = cover[i^(1<<b)] | inv[b];
      //cout << "Vertex set " << i << " covers " << cover[i] << " and inherits from " << (i^(1<<b)) << " " << cover[i^(1<<b)] << " " << inv[b] << endl;
    }
    
    allq = (1<<q)-1;
    memset(seen, 0, sizeof(seen));
    int rv = solve((1<<n)-1);
    rebuild((1<<n)-1);
    cout << "Case #" << C << ": " << rv << '\n';
    cout << sol[0];
    for( int i = 1; i != n; ++i )
      cout << ' ' << sol[i];
    cout << endl;
  }
  return 0;
}