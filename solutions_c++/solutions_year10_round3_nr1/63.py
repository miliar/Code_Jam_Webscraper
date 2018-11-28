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
  { int n, a[1000], b[1000];
    cin>>n;
    Fori(n) cin>>a[i]>>b[i];
    int wyn=0;
    Fori(n)
      for (int j=i+1; j<n; ++j)
        if ((a[i]<a[j])!=(b[i]<b[j])) ++wyn;
        
    cout<<"Case #"<<ca<<": "<<wyn<<endl;
  }
  return 0;
}
