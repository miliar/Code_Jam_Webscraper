#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <math.h>
#include <algorithm>

using namespace std;

char a[4][5];

int ttt()
{
    int xwin = 0, owin = 0;
    bool full = true;
    for(int i=0;i<4;++i)
    {
      int numx, numo, numt, numd;
      numx = numo = numt = numd = 0;
      for(int ii=0; ii<4; ++ii)
      {
          if(a[i][ii] == 'X') ++numx; 
          else if(a[i][ii] == 'O') ++numo; 
          else if(a[i][ii] == 'T') ++numt; 
          else if(a[i][ii] == '.') ++numd; 
      }
      if ( numx == 4 || (numx == 3 && numt == 1) ) {
          return 0;
      } else if ( numo == 4 || (numo == 3 && numt == 1) ) {
          return 1;
      } else if ( numd > 0 ) {
          full = false;
      }
    }

    for(int j=0;j<4;++j)
    {
      int numx, numo, numt, numd;
      numx = numo = numt = numd = 0;
      for(int jj=0; jj<4; ++jj)
      {
          if(a[jj][j] == 'X') ++numx; 
          else if(a[jj][j] == 'O') ++numo; 
          else if(a[jj][j] == 'T') ++numt; 
          else if(a[jj][j] == '.') ++numd; 
      }
      if ( numx == 4 || (numx == 3 && numt == 1) ) {
          return 0;
      } else if ( numo == 4 || (numo == 3 && numt == 1) ) {
          return 1;
      }
    }

    int nx, no, nt, nd;
    nx = no = nt = nd = 0;
    for(int k=0;k<4;++k)
    {
        if(a[k][k] == 'X') ++nx;
        else if(a[k][k] == 'O') ++no;
        else if(a[k][k] == 'T') ++nt;
        else if(a[k][k] == '.') ++nd;
    }
    if ( nx == 4 || (nx == 3 && nt == 1) ) {
      return 0;
    } else if ( no == 4 || (no == 3 && nt == 1) ) {
      return 1;
    }

    int mx, mo, mt, md;
    mx = mo = mt = md = 0;
    for(int kk=0;kk<4;++kk)
    {
        if(a[kk][3-kk] == 'X') ++mx;
        else if(a[kk][3-kk] == 'O') ++mo;
        else if(a[kk][3-kk] == 'T') ++mt;
        else if(a[kk][3-kk] == '.') ++md;
    }
    if ( mx == 4 || (mx == 3 && mt == 1) ) {
      return 0;
    } else if ( mo == 4 || (mo == 3 && mt == 1) ) {
      return 1;
    }

    if(full) {
        return 2;   // draw
    } else {
        return 3;   // cont
    }
}

int main(int argc, char * argv[])
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int TT;
    scanf("%d", &TT);
    for(int T=1;T<=TT;++T)
    {
        for(int i=0;i<4;++i)
        {
            scanf("%s",a[i]);
//            cout << a[i] << endl;
        }
        int r = ttt();
        switch (r) {
            case 0:
                printf("Case #%d: X won\n",T);
                break;
            case 1:
                printf("Case #%d: O won\n",T);
                break;
            case 2:
                printf("Case #%d: Draw\n",T);
                break;
            case 3:
                printf("Case #%d: Game has not completed\n",T);
                break;
            default:
                break;
        } 
    }
    return 0;
}
