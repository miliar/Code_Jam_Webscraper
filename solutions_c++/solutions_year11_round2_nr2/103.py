#include <iostream>
#include <vector>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <set>
#include <string>
#include <map>

using namespace std;

int n;
vector< double > p;
vector< int > k;
double d;

inline bool cando(double t)
{
  double last = -1e100;
  
  for (int i=0; i<n; i++)
  {
    double needlen = d*(k[i]-1);
    double canstart = max(last + d, p[i] - t);
    
    if (canstart + needlen > p[i] + t)
      return false;
    
    last = canstart + needlen;
  }
  
  return true;
}

inline void solve(int testnum)
{
  cerr << testnum << endl;
  cin >> n >> d;
  p.resize(n);
  k.resize(n);
  for (int i=0; i<n; i++)
    cin >> p[i] >> k[i];
  
  double l = 0;
  double r = 1e13;
  double eps = 1e-7;
  int count = 0;;
  
  while (r-l>eps && count < 10000000)
  {
    count++;
    double m = (l+r)/2.0;
    
    if (cando(m))
      r=m;
    else
      l=m+eps;
  }
  
  cout.precision(30);
  cout.setf(ios::fixed);
  cout << "Case #" << testnum + 1 << ": ";
  if (cando(l))
    cout << l;
  else
    cout << r;
  cout << endl;
}

int main()
{
  int numoftests;
 scanf("%d", &numoftests);
 for (int i=0; i<numoftests; i++)
   solve(i);
}