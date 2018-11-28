#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;
typedef long long ll;

int const MAXN = 2012;
int const MX = 1000000000;

int n;
int v[MAXN];
int h[MAXN];

bool solve()
{
  memset(h, 0, sizeof(h));
  bool rv = true;
  bool changed;
  do
  {
    changed = false;
    
    for( int i = 0; i+1 != n; ++i )
    {
      ll mn = 0;
      ll md = 1;
      int mxj = -1;
      
      // Find
      for( int j = n-1; j > i; --j )
      {
        if( md * h[j] >= md * h[i] + mn * (j - i) )
        {
          mn = h[j] - h[i];
          md = j - i;
          mxj = j;
        }
      }
      //cout << i << ' ' << mn << ' ' << md << endl;
      int j = v[i];
      if( j != mxj )
      {
        ll dx = j - i;
        ll hj = 1 + h[i] + (mn * dx + md - 1) / md;
        if( hj > MX )
          return false;
        
        if( hj > h[j] )
        {
          h[j] = hj;
          changed = true;
          break;
        }
      }
      // Fix v
      // Verify
    }
  } while( changed );
  return rv;
}

int main()
{
  int T;
  scanf("%d", &T);
  for( int C = 1; C <= T; C++ )
  {
    scanf("%d", &n);
    for( int i = 0; i != n-1; ++i )
    {
      scanf("%d", &v[i]);
      --v[i];
    }
    
    bool ok = solve();
    
    printf("Case #%d:", C);
    if( ok )
      for( int i = 0; i != n; ++i )
        printf(" %d", h[i]);
    else
      printf(" Impossible");
    printf("\n");
  }
  return 0;  
}