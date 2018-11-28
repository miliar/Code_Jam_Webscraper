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
  { int n, x=0, mi=MaxInt, suma=0;
    cin>>n;
    Fori(n)
    { int a;
      cin>>a;
      x^=a;
      mi=min(mi, a);
      suma+=a;
    }
    cout<<"Case #"<<ca<<": ";
    if (x) cout<<"NO\n";
    else cout<<suma-mi<<endl;
  }
  return 0;
}
