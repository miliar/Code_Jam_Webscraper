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
  { int r, k, n, g[1000];
    cin>>r>>k>>n;
    Fori(n) cin>>g[i];
    
    int nast[1000], zysk[1000];
    for (int pocz=0, dl=0, zy=0; pocz<n; ++pocz)
    { for (; dl<n && zy+g[(pocz+dl)%n]<=k; ++dl)
        zy+=g[(pocz+dl)%n];
      zysk[pocz]=zy;
      nast[pocz]=(pocz+dl)%n;
      if (dl)
      {
        zy-=g[pocz];
        --dl;
      }      
    }
  
    long long wyn=0;
    int byloRr[1000];
    long long bylZy[1000];
    Fori(n) byloRr[i]=-1;
    for (int rr=0, poz=0; rr<r; ++rr)
    { if (byloRr[poz]!=-1)
      {
        int ruchow=rr-byloRr[poz];
        int cykli=(r-rr)/ruchow;
        rr+=cykli*ruchow;
        wyn+=cykli*(wyn-bylZy[poz]);
        if (rr==r) break;
      }
      byloRr[poz]=rr;
      bylZy[poz]=wyn;
      wyn+=zysk[poz];
      poz=nast[poz];
    }
  
    cout<<"Case #"<<ca<<": "<<wyn<<endl;
  }


  return 0;
}
