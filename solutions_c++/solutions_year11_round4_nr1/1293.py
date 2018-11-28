#include <algorithm>
#include <limits>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include <iomanip>

using namespace std;

const int MaxInt=numeric_limits<int>::max();
typedef vector<int> VI;
typedef vector<string> VS;
#define For(i,a,n) for (int i=a; i<n; ++i)
#define Fori(n) For(i,0,n)

struct S
{ int dl, pred;
  bool operator<(const S &s) const
  { return pred<s.pred;
  }
} ss[10000];
int main()
{
  int NNN;
  cin>>NNN;
  for (int ca=1; ca<=NNN; ++ca)
  { int x, s, r, n, b[1000], e[1000], w[1000];
    double t;
    cin>>x>>s>>r>>t>>n;
    int iles=0, poz=0;
    Fori(n)
    { cin>>b[i]>>e[i]>>w[i];
      ss[iles].dl=e[i]-b[i];
      ss[iles++].pred=s+w[i];
      ss[iles].dl=b[i]-poz;
      ss[iles++].pred=s;
      poz=e[i];
    }
    ss[iles].dl=x-poz;
    ss[iles++].pred=s;
    sort(ss, ss+iles);
    double wyn=0;
    Fori(iles)
    { double odl=(ss[i].pred+r-s)*t;
      if (odl<=ss[i].dl)
      { wyn+=t+(ss[i].dl-odl)/ss[i].pred;
        t=0;
        continue;
      }
      double tt=ss[i].dl/double(ss[i].pred+r-s);
      wyn+=tt;
      t-=tt;    
    }
    cout<<"Case #"<<ca<<": "<<fixed<<setprecision(9)<<wyn<<endl;
  }

 

  return 0;
}
