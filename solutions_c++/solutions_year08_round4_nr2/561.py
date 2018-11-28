#include <algorithm>
#include <limits>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <iostream>

using namespace std;

const int MaxInt=numeric_limits<int>::max();
typedef vector<int> VI;
typedef vector<string> VS;
#define For(i,a,n) for (int i=a; i<n; ++i)
#define Fori(n) For(i,0,n)

//int x3[100000100], y2[100000100];

int main()
{
 /* Fori(100000100) x3[i]=-1;
  for (int x=0; x<=10000; ++x)
    for (int y=0; y<=10000; ++y)
    { int u=x*y;
      x3[u]=x;
      y2[u]=y;
    }  */
  int nn;
  cin>>nn;
  for (int ca=1; ca<=nn; ++ca)
  { int n, m, a;
    cin>>n>>m>>a;
    bool jest=false;
    for (int x2=0; x2<=n; ++x2)
      for (int y3=0; y3<=m; ++y3)
        for (int x3=0; x3<=n; ++x3)
          for (int y2=0; y2<=m; ++y2)
    
      { if (x2*y3-x3*y2==a)
        
        { jest=true;
          cout<<endl<<"Case #"<<ca<<": 0 0 "<<x2<<" "<<y2<<' '<<x3<<' '<<y3<<endl;
          x2=y2=x3=y3=1000000;
          break;
        }
      }
    if (!jest) cout<<endl<<"Case #"<<ca<<": IMPOSSIBLE\n";
  }

  char ccccc;
  cin>>ccccc;

  return 0;
}
