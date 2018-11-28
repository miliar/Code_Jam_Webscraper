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
  { int n, t[100];
    cin>>n;
    Fori(n)
    { string s;
      cin>>s;
      t[i]=0;
      for (int j=0; j<n; ++j)
        if (s[j]=='1') t[i]=j;
    }
    int wyn=0;
    Fori(n-1)
    { int kt=i;
      while (t[kt]>i) ++kt;
      while (kt>i)
      { swap(t[kt], t[kt-1]);
        --kt;
        ++wyn;      
      }
    } 
    cout<<"Case #"<<ca<<": "<<wyn<<endl;
  }


  return 0;
}
