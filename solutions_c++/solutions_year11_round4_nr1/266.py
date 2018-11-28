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
double x, s, r;
int n;
double t;
int b[N], e[N], w[N], o[N];

bool cmp(int i, int j)
{
  return (s+w[j])*(r+w[i]) > (s+w[i])*(r+w[j]);
}

int main()
{
  cin.sync_with_stdio(false);
  
  int T;
  cin >> T;
  for( int C = 1; C <= T; C++ )
  {
    cin >> x >> s >> r >> t >> n;
    double rv = 0;
    for( int i = 0; i != n; ++i )
    {
      cin >> b[i] >> e[i] >> w[i];
      o[i] = i;
      rv += double(e[i] - b[i]) / (w[i] + s);
      x -= e[i] - b[i];
      //cout << "In tunnel " << i << ": " << double(e[i] - b[i]) / (w[i] + s) << endl;
    }
    sort(o, o+n, cmp);
    double q = min(t, double(x) / r);
    rv += q;
    t -= q;
    x -= q * r;
    rv += x / s;
    //cout << "Started tunneling with " << t << " secs of running left and " << rv << " total time" << endl;
    int ii = 0;
    while( ii < n && t > 1e-9 )
    {
      int i = o[ii++];
      double d = e[i] - b[i];
      int ws = w[i] + s;
      int rs = w[i] + r;
      
      rv -= d / ws;
      q = min(d / rs, t);
      //cout << "running in tunnel " << i << " for " << q << " secs" << endl;
      t -= q;
      rv += q;
      rv += (d - rs*q) / ws;
    }
    printf("Case #%d: %.10f\n", C, rv);
  }
  return 0;
}