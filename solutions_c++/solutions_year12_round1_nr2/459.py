#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int const MAXN = 1001;
int const INF = 1<<29;

pair<int,int> v[MAXN];
int n;

int solve()
{
  int   k       = 0;
  int   rv      = 0;
  int   s       = 0;

  vector<int> done(n);
  
  while( true )
  {
    for( int i = k; i != n; ++i )
    {
      if( s >= v[i].first )
      {
        s += 2 - done[i];
        done[i] = 2;
        k += 1;
        rv += 1;
      }
      else
        break;
    }
    if( k == n )
      break;
      
    int mx = -1;
    int mxi = -1;
    
    for( int i = n-1; i >= k; --i )
    {
      if( done[i] >= 1 )
        continue;
        
      if( s >= v[i].second )
      {
        //if( v[i].first > mx )
        {
          mx = v[i].first;
          mxi = i;
          break;
        }
      }
    }
    if( mxi == -1 )
      break;
    
    done[mxi] = 1;
    rv += 1;
    s += 1;
  }
  
  if( k != n )
    return INF;
  return rv;
}

int main()
{
  int T;
  cin >> T;
  for( int C = 1; C <= T; C++ )
  {
    cin >> n;
    for( int i = 0; i != n; ++i )
      cin >> v[i].second >> v[i].first;
    sort(v, v+n);
    
    int rv = solve();
      
    cout << "Case #" << C << ": ";
    if( rv != INF )
      cout << rv;
    else
      cout << "Too Bad";
    cout << '\n';
  }
  
  return 0;
}