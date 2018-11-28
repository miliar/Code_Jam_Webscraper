#include <algorithm>
#include <limits>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

const int MaxInt=numeric_limits<int>::max();
typedef vector<int> VI;
typedef vector<string> VS;
#define For(i,a,n) for (int i=a; i<n; ++i)
#define Fori(n) For(i,0,n)

int main()
{
  int NNN;
  cin>>NNN;
  for (int ca=1; ca<=NNN; ++ca)
  { int lp, mo, p[200], v[200];
    long long szer[200];
    cin>>lp>>mo;
    Fori(lp)
    { cin>>p[i]>>v[i];
      szer[i]=((long long)v[i]-1)*mo;
    }
    double mi=0, ma=1e12;

    for (int x=0; x<200; ++x)
    { double poprz=-2e12, sr=(mi+ma)/2;
      bool ok=true;
      Fori(lp)
      { double pozL=max(poprz+mo, p[i]-sr), pozP=pozL+szer[i];
        if (pozP-p[i]>sr)
        { mi=sr;
          ok=false;
          break;
        }
        poprz=pozP;      
      }
      if (ok) ma=sr;
    }
    cout<<endl<<"Case #"<<ca<<": "<<setiosflags(ios::fixed)<<setprecision(8)<<(floor(mi*2+0.2)/2)<<endl;
  }
  return 0;
}
