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

int main()
{
  int NNN;
  cin>>NNN;
  for (int ca=1; ca<=NNN; ++ca)
  {
    int n, odl[10000], dl[10000], kon, pocz[10000];
    cin>>n;
    Fori(n)
    { cin>>odl[i]>>dl[i];
      pocz[i]=MaxInt;
    }
    cin>>kon;
    pocz[0]=0;
    bool byl=false;
    Fori(n)
    {
      if (pocz[i]==MaxInt) continue;
      int zas=odl[i]+odl[i]-pocz[i];
      if (zas>=kon)
      { byl=true;
        break;
      }
      for (int j=i+1; j<n && odl[j]<=zas; ++j)
        pocz[j]=min(pocz[j], max(odl[j]-dl[j], odl[i]));
    }
    cout<<"Case #"<<ca<<": "<<(byl ? "YES" : "NO")<<endl;
  }

  return 0;
}
