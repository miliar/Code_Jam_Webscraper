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
    vector<int> mal(5000, 0), zad(5000, 0), ma(5000, -1);
    vector<pair<int, int> > lubi[2002];
    int nn, mm;
    cin>>nn>>mm;
    Fori(mm)
    { int t;
      cin>>t;
      for (int j=0; j<t; ++j)
      { int a, b;
        cin>>a>>b;
        --a;
        lubi[i].push_back(make_pair(a, b));
        if (b) ma[i]=a;
      }
    }
    int wyn=0;
    while (!wyn)
    { wyn=2;
      Fori(mm)
        if (!zad[i])
        { if (ma[i]!=-1 && mal[ma[i]])
          { zad[i]=true;
            continue;
          }
          int moze=0;
          for (int j=0; j<lubi[i].size(); ++j)
          { if (lubi[i][j].second==0 && !mal[lubi[i][j].first])
              ++moze;
          } 
          if (moze) continue;
          if (ma[i]==-1)
          { wyn=1;
            break;
          }
          mal[ma[i]]=1;
          wyn=0;
        }
    }
  
    cout<<endl<<"Case #"<<ca<<": ";
    if (wyn==1) cout<<"IMPOSSIBLE";
    else Fori(nn) cout<<mal[i]<<' ';
    cout<<endl;
  }

  char ccccc;
  cin>>ccccc;

  return 0;
}
