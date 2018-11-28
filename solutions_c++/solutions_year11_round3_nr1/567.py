#include <iostream>
#include <string>
#include <cstdio>
#include <map>
#include <vector>
using namespace std;

#define PB push_back
#define MP make_pair
#define PII pair<int, int>

#define SZ(x) ((int)((x).size()))
#define OUT(x) printf(#x" %d\n", x)

#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define rep(i, a, b) for((i)=(a); (i)<(int)(b); (i)++)
#define foreach(c,itr) \
for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
int i;

struct point{
   int x, y;
   point(){}
   point(int _x, int _y):x(_x),y(_y){}
   bool operator < (point p)
   {
      if(x!=p.x)
        return x<p.x;
      else
        return y<p.y;
   }
};
vector<point> vc[500];
int mat[55][55];
int main()
{
    int cas;
    freopen("in.txt","r", stdin);
    freopen("out.txt","w", stdout);
    cin >> cas;
    int T=0;
    while(cas--)
    {
       int r, c;
       cin>>r>>c;
       char ch;
       point mx(55,55);
       int cnt=0;
       for(int i=1; i<=r; ++i)
       {
           for(int j=1; j<=c; ++j)
           {
              scanf(" %c", &ch);
              if(ch=='#')
              {
                mat[i][j] = 1;
                cnt ++;
                if(point(i,j)<mx)
                  mx = point(i,j);
              }
              else
                mat[i][j] = 0;
           }
       }
       bool flag = false;
       printf("Case #%d:\n", ++T);
       while(cnt>0)
       {
          mat[mx.x][mx.y] = 2;
          if(mx.x+1>r || mx.y+1>c)
            goto kirk;
          int tx = mx.x, ty=mx.y;
          if(!mat[tx+1][ty]||!mat[tx][ty+1]||!mat[tx+1][ty+1])
            goto kirk;
          mat[tx+1][ty] = 3;
          mat[tx][ty+1] = 4;
          mat[tx+1][ty+1] = 5;
          cnt = 0;
          mx = point(55,55);
          for(int i=1; i<=r; ++i)
          {
           for(int j=1; j<=c; ++j)
           {
              if(mat[i][j] == 1)
              {
                cnt ++;
                if(point(i,j)<mx)
                  mx = point(i,j);
              }
           }
          }
       }
       for(int i=1; i<=r; ++i)
          {
           for(int j=1; j<=c; ++j)
           {
              if(mat[i][j] == 0)
              {
                cout<<'.';
              }
              else if(mat[i][j]==2)
                cout<<'/';
              else if(mat[i][j]==3)
                cout<<'\\';
              else if(mat[i][j]==4)
                cout<<'\\';
              else
                cout<<'/';
           }
           cout<<endl;
          }
       continue;
kirk:
      cout<<"Impossible\n";
}
    clog<<"\n\nend\n";
    while(1);
    return 0;
}
