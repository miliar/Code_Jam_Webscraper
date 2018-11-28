using namespace std;
#include <algorithm>
#include <iostream>
#include <iterator>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <map>
#include <set>

template <class T> string toStr(const T &x)
{ stringstream s; s << x; return s.str(); }
template <class T> int toInt(const T &x)
{ stringstream s; s << x; int r; s >> r; return r; }

#define For(i, a, b) for (int i=(a); i<(b); ++i)
#define foreach(x, v) for (typeof (v).begin() x = (v).begin(); \
                           x != (v).end(); ++x)
#define D(x) cout << #x " = " << (x) << endl

const double EPS = 1e-9;
int cmp(double x, double y = 0, double tol = EPS){
    return( x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}

bool can(const vector<int> & h, int d, double mov)
{
  double start = h[0] - mov;
  for(int i = 1; i < h.size() ; ++i)
    {
      double start1 = start + d;
      double start2 = h[i] - mov;
      start = max(start1, start2);
      if(fabs(start - h[i]) > mov)
        return false;
    }
  return true;
}
int main(){
  int casos ;
  cin >> casos;
  for(int c = 1; c <= casos; ++c)
    {
      int n, d;
      cin >> n >> d;
      vector<int> car;
      for(int i = 0; i < n ; ++i)
        {
          int pos, k;
          cin >> pos >> k;
          while(k--)
            car.push_back(pos);
        }
      sort(car.begin(), car.end());
      double max = 1e12;
      double min = 0;
      double mid = (max+min)/2;
      int it = 1000;
      while(it--)
        {
          if(can(car, d, mid))
            {
              max = mid;
            }
          else
            {
              min = mid;
            }
          mid = (max+min)/2;
        }
      printf("Case #%d: %.1lf\n", c, mid);
    }
  return 0;
}
