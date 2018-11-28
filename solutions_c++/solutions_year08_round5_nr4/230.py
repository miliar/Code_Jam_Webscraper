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
   int ro[10100][10100];
int main()
{
  int nnn;
  cin>>nnn;
  for (int ca=1; ca<=nnn; ++ca)
  {
    
    memset(ro, 0, sizeof(ro));
    int r, c, roo;
    cin>>r>>c>>roo;
    Fori(roo)
    { int a, b;
      cin>>a>>b;
      ro[a][b]=-1;
    }
    ro[1][1]=1;
    int y=1;
    for (int x=3; x<2000; x+=2)
    { y++;
      for (int a=0; a<y; ++a)
        if (ro[y+a][x-a]!=-1)
        { if (ro[y+a-1][x-a-2]!=-1) ro[y+a][x-a]=(ro[y+a][x-a]+ro[y+a-1][x-a-2])%10007;
          if (ro[y+a-2][x-a-1]!=-1) ro[y+a][x-a]=(ro[y+a][x-a]+ro[y+a-2][x-a-1])%10007;
        }
    
    }
    
    cout<<endl<<"Case #"<<ca<<": "<<ro[r][c]<<endl;
    



  }

  char ccccc;
  cin>>ccccc;

  return 0;
}
