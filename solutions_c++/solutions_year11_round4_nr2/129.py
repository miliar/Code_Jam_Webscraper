#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <cstring>
#include <string>
#include <cmath>
#include <utility>
#include <set>
#include <queue>
#include <sstream>
#define fr(a,b,c) for (a=b;a<=c;a++)
#define frr(a,b,c) for (a=b;a>=c;a--)
#define mp make_pair
#define pii pair<int,int>
#define pb push_back
#define F first
#define S second
#define oo 1000111222
#define lloo 1LL << 60
using namespace std;

int n,d,m,a[555][555],row[555][555],col[555][555];

int ok(int sx,int sy,int k)
{
    int cx=sx*2+k-1,cy=sy*2+k-1,i,j,X=0,Y=0;
    /*fr(i,sx,sx+k-1)
     fr(j,sy,sy+k-1)
     {         
       if ((i==sx || i==sx+k-1) && (j==sy || j==sy+k-1)) continue;
       X+=a[i][j]*(i*2-cx);
       Y+=a[i][j]*(j*2-cy);
     }
    return (!X && !Y);*/
    fr(i,sx,sx+k-1)
      if (i==sx || i==sx+k-1) X+=(row[i][sy+k-2]-row[i][sy])*(i*2-cx);
      else X+=(row[i][sy+k-1]-row[i][sy-1])*(i*2-cx);
    if (X) return 0;
    fr(j,sy,sy+k-1)
      if (j==sy || j==sy+k-1) Y+=(col[sx+k-2][j]-col[sx][j])*(j*2-cy);
      else Y+=(col[sx+k-1][j]-col[sx-1][j])*(j*2-cy);
    return (!Y);
}

int main()
{
    freopen("blarge.in","r",stdin); freopen("blarge.out","w",stdout);
    int test,it,i,j,k,I,J;
    char ch;
    cin >> test;
    fr(it,1,test)
    {
       cout << "Case #" << it << ": ";
       scanf("%d%d%d\n",&m,&n,&d);
       fr(i,1,m) fr(j,1,n) 
       {
          scanf("%c",&ch); 
          a[i][j]=int(ch)-48;
          scanf("\n");
       }
       fr(i,1,m) fr(j,1,n) row[i][j]=row[i][j-1]+a[i][j];
       fr(j,1,n) fr(i,1,m) col[i][j]=col[i-1][j]+a[i][j];
       frr(k,min(m,n),3)
       {
          int s=0,kt=0;
          fr(I,1,m-k+1)
          {
           fr(J,1,n-k+1)
            if (ok(I,J,k))
            {
               kt=1; break;
            }
           if (kt) break;
          }
          if (kt) break;
       }
       if (k>=3) cout << k << endl;
       else cout << "IMPOSSIBLE" << endl;
       cerr << it << endl;
    }
    //while (1);
    return 0;
}
