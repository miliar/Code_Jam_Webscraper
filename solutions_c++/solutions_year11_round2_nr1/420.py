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

int n;
string g[101];

pair<int,int> wp(int i)
{
  string const& s = g[i];
  pair<int,int> rv;
  for( int i = 0; i != n; ++i )
  {
    if( s[i] != '.' )
    {
      ++rv.second;
      rv.first += (s[i] == '1');
    }
  }
  return rv;
}

pair<int,int> mem[101][101];

pair<int,int> owp(int i, int k)
{
  pair<int,int>& rv = mem[i][k];
  if( rv.first != -1 )
    return rv;
  rv = wp(i);
  if( g[i][k] != '.' )
  {
    --rv.second;
    rv.first -= (g[i][k] == '1');
  }
  return rv;
}

double calc(pair<int,int> const& p)
{ return p.second ? (double(p.first) / p.second) : 0; }

double oowp(int i)
{
  double rv = 0;
  string const& s = g[i];
  int o = 0;
  for( int j = 0; j != n; ++j )
  {
    if( s[j] != '.' )
    {
      rv += calc(owp(j, i));
      ++o;
    }
  }
  return rv/o;
}

double solve(int i)
{
  double rv = 0.25 * calc(wp(i));
  string const& s = g[i];
  
  double owp_ = 0, oowp_ = 0;
  int o = 0;
  for( int j = 0; j != n; ++j )
  {
    if( s[j] != '.' )
    {
      ++o;
      owp_ += calc(owp(j, i));
      oowp_+= oowp(j);
    }
  }
  //cout << rv << ' ' << owp_/o << ' ' << oowp_/o << endl;
  return rv + 0.5*owp_/o + 0.25*oowp_/o;
}

int main()
{
  cin.sync_with_stdio(false);
  
  int T;
  cin >> T;
  for( int C = 1; C <= T; C++ )
  {
    cin >> n;
    for( int i = 0; i != n; ++i )
      cin >> g[i];
    
    memset(mem, -1, sizeof(mem));
    printf("Case #%d:\n", C);
    for( int i = 0; i != n; ++i )
      printf("%.10f\n", solve(i));
  }
  return 0;
}