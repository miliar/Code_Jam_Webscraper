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

const int N=7000;
bool pion[N][N],//[x][y] po lewej
     poz[N][N],//pod
     jest[N][N];

int main()
{
  int nnn;
  cin>>nnn;
  for (int ca=1; ca<=nnn; ++ca)
  { memset(pion, 0, sizeof(pion));
    memset(poz, 0, sizeof(poz));
    memset(jest, 0, sizeof(jest));
    int p, x=N/2, y=N/2;
    int kier=0;// 0pn, 1wsch, 2pd, 3zach
    cin>>p;
    while (p-->0)
    { int t;
      string s;
      cin>>s>>t;
      while (t-->0)
      { for (int i=0; i<s.size(); ++i)
        { switch (s[i])
          {
            case 'L':
              kier=(kier+4-1)%4;
              break;
            case 'R':
              kier=(kier+1)%4;
              break;
            case 'F':
              switch (kier)
              {
                case 0:
                  pion[x][y]=true;
                  ++y;
                  break;
                case 1:
                  poz[x][y]=true;
                  ++x;
                  break;
                case 2:
                  --y;
                  pion[x][y]=true;
                  break;
                case 3:
                  --x;
                  poz[x][y]=true;
                  break;
              }
          }    
        }      
      }     
    }
 
    int wyn=0;
    for (int x=0; x<N; ++x)
    { bool je=false, byl=false;
      int u=0;
      for (int y=0; y<N; ++y)
      { if (poz[x][y])
        { if (!je && byl) 
          {
            wyn+=u;
            Fori(u) jest[x][y-i-1]=true;
          }
          je=!je;
          u=0;
          byl=true;
        }
        ++u;
      }
    }

    for (int y=0; y<N; ++y)
    { bool je=false, byl=false;
      int u=0;
      for (int x=0; x<N; ++x)
      { if (pion[x][y])
        { if (!je && byl) 
          {
           
            Fori(u) if (!jest[x-i-1][y]) ++wyn;
          }
          je=!je;
          u=0;
          byl=true;
        }
        ++u;
      }
    }
    
    cout<<endl<<"Case #"<<ca<<": "<<wyn<<endl;
    
  }

  char ccccc;
  cin>>ccccc;

  return 0;
}
