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

int czas()
{ string s;
  cin>>s;
  int godz=10*(s[0]-'0')+s[1]-'0';
  int min=10*(s[3]-'0')+s[4]-'0';
  return godz*60+min;
}

int main()
{
  int n;
  cin>>n;
  for (int ca=1; ca<=n; ++ca)
  {
    int t, na, nb;
    cin>>t>>na>>nb;
    multiset<pair<int, int> > a, b;
    Fori(na)
    { int x=czas(), y=czas();
      a.insert(make_pair(x, y+t));
    }
    Fori(nb)
    { int x=czas(), y=czas();
      b.insert(make_pair(x, y+t));
    }
    int wyna=0, wynb=0;
    while (!a.empty() || !b.empty())
    { bool jesta;
      multiset<pair<int, int> >::iterator ia=a.begin(), ib=b.begin();
      if (!a.empty() && !b.empty()) jesta=ia->first < ib->first;
      else jesta=b.empty();
      if (jesta) ++wyna;
      else ++wynb;
      for (;;)
      { int ter;
        if (jesta)
        { ter=ia->second;
          a.erase(ia);
        }
        else
        { ter=ib->second;
          b.erase(ib);
        }
        jesta=!jesta;
        if (jesta)
        { ia=a.upper_bound(make_pair(ter,-1));
          if (ia==a.end()) break;
        }
        else
        { ib=b.upper_bound(make_pair(ter,-1));
          if (ib==b.end()) break;
        }
      }    
    }
    cout<<endl<<"Case #"<<ca<<": "<<wyna<<' '<<wynb<<endl;
  }

  char ccccc;
  cin>>ccccc;

  return 0;
}
