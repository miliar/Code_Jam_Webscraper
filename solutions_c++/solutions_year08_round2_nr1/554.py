#include <iostream>
#include <vector>
#include <list>
#include <map>
#include <algorithm>
#include <functional>

using namespace std;

class Point
{
public:
  long long x, y;

  Point ( long long i, long long j )
  {
    x = i;
    y = j;
  }
};

int main ()
{
  int num;
  cin >> num;
  int n;
  long long A, B, C, D, x, y, M;
  int i, j, k, l;
  long long count;
  for ( i = 0; i++ < num; )
  {
    cin >> n >> A >> B >> C >> D >> x >> y >> M;
    vector< Point > p;
    p.push_back( Point( x, y ) );
    for ( j = 1; j < n; j++ )
    {
      x = (A * x + B) % M;
      y = (C * y + D) % M;
      p.push_back( Point( x, y ) );
    }
    count = 0L;
    for ( j = 0; j < n-2; j++ )
      for ( k = j + 1; k < n-1; k++ )
      {
        long long sx = p[j].x + p[k].x;
        long long sy = p[j].y + p[k].y;
        for ( l = k + 1; l < n; l++ )
          if ( (sx + p[l].x) % 3 == 0 &&
               (sy + p[l].y) % 3 == 0 )
            count++;
      }               
    cout << "Case #" << i << ": " << count << endl;
  }

  return 0;
}
