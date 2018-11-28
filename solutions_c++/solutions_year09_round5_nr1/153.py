#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cassert>
#include<cmath>
#include<vector>
#include<set>
#include<map>
#include<list>
#include<deque>
#include<queue>
#include<stack>
#include<functional>
#include<sstream>
#include<iostream>
#include<ctime>
#include<algorithm>
using namespace std;

#define DEBUG(x...) printf(x)
#define all(v) (v).begin(),(v).end()
#define rall(v) (v).begin(),(v).rend()
#define _foreach(it,b,e) for(__typeof__(b) it=(b); it!=(e);++it)
#define foreach(x...)

typedef long long int huge;

const int inf = 0x3f3f3f3f;
const huge hugeinf = 0x3f3f3f3f3f3f3f3fll;//dois L's
const double eps = 1e-9;

int mov[4][2]={{0,1},{0,-1},{1,0},{-1,0}};
int n,m;
char mapa[55][55];

int fila[2985984*30][4];
int foi[56][56][56][56];
int dentro[33][33][33][33];
int st[2][2];
int ed[2][2];
int ret;


void solve()
{
    int dista,distb,px,py,bx,by;
    int ifila=0;
    int ffila=1;

    fila[0][0]=st[0][0];
     fila[0][1]=st[0][1];
     fila[0][2]=st[1][0];
     fila[0][3]=st[1][1];


    foi[st[0][0]][st[0][1]][st[1][0]][st[1][1]]=0;


    while (ifila<ffila)
    {
        bool dang=false;

        px=fila[ifila][0];
        py=fila[ifila][1];
        bx=fila[ifila][2];
        by=fila[ifila][3];

        distb=foi[px][py][bx][by];

       // if(ffila>1000000)printf("%d %d %d %d %d %d %d %d\n",px,py,bx,by,ed[0][0],ed[0][1],ed[1][0],ed[1][1]);

        if (px==ed[0][0] && py==ed[0][1] && bx==ed[1][0] && by==ed[1][1])
            if (ret>distb)
                ret=distb;
        if (bx==ed[0][0] && by==ed[0][1] && px==ed[1][0] && py==ed[1][1])
            if (ret>distb)
                ret=distb;



        if(abs(bx-px)==1 && abs(by-py)==1)
            dang=true;


        for (int i=0;i<4;i++)
        {
            int x=px+mov[i][0];
            int y=py+mov[i][1];
            int flag=0;

            if(dang)
            {
                if(!(abs(bx-x)==1 && abs(by-y)==0) && !(abs(bx-x)==0 && abs(by-y)==1))continue;
            }
            if(x==bx && y==by)continue;


            if (mapa[px-mov[i][0]][py-mov[i][1]]=='#')continue;
            if (mapa[x][y]=='#')continue;
                if (bx==px-mov[i][0] && by==py-mov[i][1])continue;

            if (foi[x][y][bx][by]>distb)
                flag=1;

            if (flag)
            {
                if(dentro[x][y][bx][by]<55)
                {
                    fila[ffila][0]=x;
                    fila[ffila][1]=y;
                    fila[ffila][2]=bx;
                    fila[ffila][3]=by;
                    dentro[x][y][bx][by]++;
                    ffila++;
                }
                foi[x][y][bx][by]=distb+1;

            }
        }

        for (int i=0;i<4;i++)
        {

          //  if(px==3 && py==2 && bx==3 && by==3)printf("oi");
            int x=bx+mov[i][0];
            int y=by+mov[i][1];
            int flag=0;

           // if(px==3 && py==2 && x==3 && y==3)printf("oi");
           if(dang)
            {
                if(!(abs(x-px)==1 && abs(y-py)==0) && !(abs(x-px)==0 && abs(y-py)==1))continue;
            }
            if(x==px && y==py)continue;


            if (mapa[bx-mov[i][0]][by-mov[i][1]]=='#')continue;
              if (px==bx-mov[i][0] && py==by-mov[i][1])continue;

            if (mapa[x][y]=='#')continue;


            if (foi[px][py][x][y]>distb)
                flag=1;


            if (flag)
            {
                if(dentro[px][py][x][y]<55)
                {
                    fila[ffila][0]=px;
                    fila[ffila][1]=py;
                    fila[ffila][2]=x;
                    fila[ffila][3]=y;
                    ffila++;
                    dentro[px][py][x][y]++;
                }
                foi[px][py][x][y]=distb+1;

            }
        }



        ifila++;
      //  if(distb+1>50)printf("bug");
     // if(ffila>12*12*12*12*50)printf("bug\n");
    }
  //  printf("%d\n",ffila);
    return ;
}
int main ()
{
    int tt=1;
    scanf("%d",&tt);
    int pp=1;
    while (tt--)
    {
        scanf("%d %d",&n,&m);

        ret=inf;
        memset(foi,0x3f,sizeof(foi));
        memset(dentro,0,sizeof(dentro));

        for (int i=0;i<=3*n+2;i++)
            for (int j=0;j<=3*m+2;j++)
                mapa[i][j]='#';


        int ff[2]={0};
        for (int i=1;i<=n;i++)
            for (int j=1;j<=m;j++)
            {
                scanf(" %c",&mapa[i][j]);
                if (mapa[i][j]=='o')
                    mapa[i][j]='.',st[ff[0]][0]=i,st[ff[0]++][1]=j;
                if (mapa[i][j]=='x')
                    mapa[i][j]='.',ed[ff[1]][0]=i,ed[ff[1]++][1]=j;
                if (mapa[i][j]=='w')
                    mapa[i][j]='.',st[ff[0]][0]=i,st[ff[0]++][1]=j,ed[ff[1]][0]=i,ed[ff[1]++][1]=j;
            }


       //  printf("%d %d\n",ff[0],ff[1]);
        if(ff[0]==1)
        {
            st[1][0]=2*n+1;
            st[1][1]=2*m+1;
            ed[1][0]=2*n+1;
            ed[1][1]=2*m+1;

        }
       // printf("oi");
        solve();
        if (ret==inf)
            printf("Case #%d: -1\n",pp++);
        else
            printf("Case #%d: %d\n",pp++,ret);
    }
    return 0;
}

