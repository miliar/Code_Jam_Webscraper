
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <iostream>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <queue>
#include <stack>
#include <deque>
#include <complex>

using namespace std;

#define x1 fiwgiunb
#define x2 viosjosk
#define y1 fnwnfwgw
#define y2 jfowjgon
#define ws osgsogsg
#define free fnibfn


#define dbg(x) cerr << #x << " = " << x << endl
#define deb(x) cerr << #x << " = " << x << endl


#define all(c) (c).begin(),(c).end()
#define pb push_back
#define sz(c) (int)(c).size()          
#define mp make_pair
#define forn(i,n) for(int i=0;i<(int)n;++i)
#define ford(i,n) for(int i=(int)n;i>=0;--i)
#define X first
#define Y second
#define bits(x) __builtin_popcount(x)



typedef long long int64;
typedef long long ll;
typedef long double ld;


char a[100][100];

int main()
{
  int t;
  cin>>t;
  forn(T,t)
  {
    printf("Case #%d:\n",T+1);
    int r,c;
    scanf("%d%d",&r,&c);
    forn(i,r)
      scanf(" %s",a[i]);

    bool ok=true;
    forn(i,r)
      forn(j,c)
      {
        if (a[i][j]=='#')
        {
          a[i][j]='/';
          if(j+1>=c || a[i][j+1] !='#')
            ok=false;
          a[i][j+1]='\\';

          if(i+1>=r || a[i+1][j]!='#')
            ok=false;
          a[i+1][j]='\\';

          if(a[i+1][j+1]!='#')
            ok=false;
          a[i+1][j+1]='/';
        }
      }

    if(!ok)
      puts("Impossible");
    else
    {
     forn(i,r)
     {
       forn(j,c)
         printf("%c",a[i][j]);
       puts("");
     }
    }
  }
   
  return 0;
}
