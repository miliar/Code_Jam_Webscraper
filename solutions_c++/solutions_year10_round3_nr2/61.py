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
    long long l, p, c;
    cin>>l>>p>>c;
    int wyn=0;
    while (l*c<p)
    { ++wyn;
      p=(p+c-1)/c;
    }
    int w=wyn;
    wyn=0;
    while (w)
    { ++wyn;
      w/=2;
    }
    cout<<"Case #"<<ca<<": "<<wyn<<endl;
  }
  return 0;
}
