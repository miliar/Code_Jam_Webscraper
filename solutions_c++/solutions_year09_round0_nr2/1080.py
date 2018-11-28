/*
OS: Microsoft Windows XP Professional
Compiler: Bloodshed Dev-C++ 4.9.9.2
*/
#include <iostream>
#include <cstring>
using namespace std;
int t;
int h, w;
int m[102][102]={0};
struct {bool n, w, e, s;}c[102][102]={0};
char a[102][102]={0};
int num_color=0;
void Link(int x, int y)
{
     if (m[x-1][y]<m[x][y]
      && m[x-1][y]<=m[x][y-1]
      && m[x-1][y]<=m[x][y+1]
      && m[x-1][y]<=m[x+1][y])
     {
         c[x][y].n=true;
         c[x-1][y].s=true;
         return;
     }
     if (m[x][y-1]<m[x][y]
      && m[x][y-1]<=m[x-1][y]
      && m[x][y-1]<=m[x][y+1]
      && m[x][y-1]<=m[x+1][y])
     {
         c[x][y].w=true;
         c[x][y-1].e=true;
         return;
     }
     if (m[x][y+1]<m[x][y]
      && m[x][y+1]<=m[x-1][y]
      && m[x][y+1]<=m[x][y-1]
      && m[x][y+1]<=m[x+1][y])
     {
         c[x][y].e=true;
         c[x][y+1].w=true;
         return;
     }
     if (m[x+1][y]<m[x][y]
      && m[x+1][y]<=m[x-1][y]
      && m[x+1][y]<=m[x][y-1]
      && m[x+1][y]<=m[x][y+1])
     {
         c[x][y].s=true;
         c[x+1][y].n=true;
         return;
     }
}
void Mark(int x, int y)
{
     if (a[x][y]!=0)
         return;
     a[x][y]='a'+num_color;
     if (c[x][y].n)
         Mark(x-1, y);
     if (c[x][y].w)
         Mark(x, y-1);
     if (c[x][y].e)
         Mark(x, y+1);
     if (c[x][y].s)
         Mark(x+1, y);
}
int main()
{
    freopen("ws.in", "r", stdin);
    freopen("ws.out", "w", stdout);
    int k, i, j;
    cin>>t;
    for (k=1; k<=t; k++)
    {
        memset(m, 0, sizeof(m));
        memset(c, 0, sizeof(c));
        memset(a, 0, sizeof(a));
        num_color=0;
        cin>>h>>w;
        for (i=1; i<=h; i++)
            for (j=1; j<=w; j++)
                cin>>m[i][j];
        for (i=1; i<=h; i++)
            m[i][0]=m[i][w+1]=100000000;
        for (j=1; j<=w; j++)
            m[0][j]=m[h+1][j]=100000000;
        for (i=1; i<=h; i++)
            for (j=1; j<=w; j++)
                Link(i, j);
        for (i=1; i<=h; i++)
            for (j=1; j<=w; j++)
                if (a[i][j]==0)
                {
                    Mark(i, j);
                    num_color++;
                }
        cout<<"Case #"<<k<<":\n";
        for (i=1; i<=h; i++)
        {
            for (j=1; j<w; j++)
                cout<<a[i][j]<<' ';
            cout<<a[i][w];
            cout<<endl;
        }
    }
    return 0;
}
