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

int zaj[3000000];
int main()
{
  int NNN;
  cin>>NNN;
  const int D=9;
  int d[D], z=1;
  for (int i=0, dd=10; i<D; ++i, dd*=10)
    d[i]=dd;
  for (int ca=1; ca<=NNN; ++ca)
  {
    int a, b, wyn=0;
    cin>>a>>b;
    for (int n=a; n<b; ++n)
    {
      ++z;
      int dl=0;
      for (int x=n; x; x/=10) ++dl;
      Fori(dl-1)
      {
        int p=n/d[i], k=n%d[i], m=k*d[dl-i-2]+p;
        if (n<m && m<=b && zaj[m]!=z)
        {
          ++wyn;
          zaj[m]=z;
        }
      }
    }
    cout<<"Case #"<<ca<<": "<<wyn<<endl;
  }
  return 0;
}
