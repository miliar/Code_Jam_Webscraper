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
  /*double suma=0, d=1.0/3;
  Fori(100)
  { suma+=(i+1)*d;
    d*=2.0/3;
    cout<<suma<<endl;
  } */
  
  

  int NNN;
  cin>>NNN;
  for (int ca=1; ca<=NNN; ++ca)
  { int n, wyn=0;
    cin>>n;
    Fori(n)
    { int a;
      cin>>a;
      if (a!=i+1) ++wyn;
    }
    cout<<"Case #"<<ca<<": "<<wyn<<endl;
  }
  return 0;
}
