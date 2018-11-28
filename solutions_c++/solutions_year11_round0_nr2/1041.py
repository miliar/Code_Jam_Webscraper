#include <cstdio>
#include <iostream>
#include <vector>
#include <memory.h>
#include <string.h>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <string>
using namespace std;

#define pb push_back
#define mp make_pair
#define sz(a) int((a).size())
#define forn(i, n) for (int i=0; i<(n); ++i)
#define foreach(it, a) for (__typeof((a).begin()) it=(a).begin(); it!=(a).end(); ++it)

typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;


string s;
char t[256];
char c[256][256], d[256][256];
int n, nc, nd, m;

int main()
{
  freopen("a.in", "r", stdin);
  freopen("a.out", "w", stdout);
  
  int tc; scanf("%d", &tc);
  for (int tt=1; tt<=tc; ++tt)
  {
    memset(c, 0, sizeof(c));
    memset(d, 0, sizeof(d));
    cin >> nc;
    forn (i, nc)
    {
      string s; cin >> s;
      c[s[0]][s[1]] = s[2];   
      c[s[1]][s[0]] = s[2];   
    }    
    cin >> nd;
    forn (i, nd)
    {
      string s; cin >> s;
      d[s[0]][s[1]] = 1;   
      d[s[1]][s[0]] = 1;   
    }
    cin >> n >> s;
    m = 0;
    forn (i, sz(s))
    {
      t[m++] = s[i];
      if (m >= 2 && c[t[m-2]][t[m-1]])
        t[m-2] = c[t[m-2]][t[m-1]], --m;
      forn (j, m-1) if (d[t[j]][t[m-1]])
      {
        m = 0;
        break;
      }  
    }
    printf("Case #%d: [", tt);
    forn (i, m) 
    {
      if (i) printf(", ");
      printf("%c", t[i]);
    }
    puts("]");
  }
  
  return 0;
}

