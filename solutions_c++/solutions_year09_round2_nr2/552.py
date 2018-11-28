#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <utility>
#include <set>
#include <map>
#include <string>
#include <memory.h>
using namespace std;

#define god_mode on
#define mp make_pair
#define pb push_back

typedef pair<int,int> pii;
typedef long long ll;
typedef long double ld;

int main()
{
  int t;
  string s;
  cin >> t;
  for ( int tc=1; tc<=t; tc++ )
  {
    cin >> s;
    int n = (int)s.size();
    int fl = 1;
    for ( int i=n-1; i>0; i-- )
      if ( s[i] > s[i-1] )
      {
        int mi = i;
        for ( int q=i+1; q<n; q++ )
          if ( s[q] > s[i-1] && s[q] < s[mi] ) mi = q;

        swap( s[i-1], s[mi] ); 
        for ( int q=i; q<n; q++ )
          for ( int w=q+1; w<n; w++ )
            if ( s[q] > s[w] ) swap( s[q], s[w] );
        fl = 0;
        break;
      }

    if ( fl )
    {
      s = "0" + s;
      n++;
      for ( int i=n-1; i>0; i-- )
      if ( s[i] > s[i-1] )
      {
        int mi = i;
        for ( int q=i+1; q<n; q++ )
          if ( s[q] > s[i-1] && s[q] < s[mi] ) mi = q;

        swap( s[i-1], s[mi] ); 
        for ( int q=i; q<n; q++ )
          for ( int w=q+1; w<n; w++ )
            if ( s[q] > s[w] ) swap( s[q], s[w] );
        fl = 0;
        break;
      }

    }

    cout << "Case #" << tc << ": " << s << endl;
  }
}