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
  int n;
  cin>>n;
  for (int ca=1; ca<=n; ++ca)
  {
    int lw;
    set<string> wysz, kw;
    cin>>lw;
    string s;
    getline(cin, s);
    Fori(lw)
    { getline(cin, s);
      wysz.insert(s);
    }
    int lz, wyn=0;
    cin>>lz;
    getline(cin, s);
    kw=wysz;
    Fori(lz)
    { getline(cin, s);
      if (kw.find(s)!=kw.end()) kw.erase(kw.find(s));
      if (kw.empty())
      { ++wyn;
        kw=wysz;
        kw.erase(kw.find(s));
      }    
    }
    cout<<endl<<"Case #"<<ca<<": "<<wyn<<endl;
  }

  char ccccc;
  cin>>ccccc;

  return 0;
}
