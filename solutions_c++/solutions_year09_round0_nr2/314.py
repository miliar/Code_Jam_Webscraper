#include <iostream>

using namespace std;

const int d[4][2]={-1,0,0,-1,0,1,1,0};

int h,w,i,j,k,t,map[111][111],len,q[10011][2];
char a[111][111],c,cc;
bool b[111][111];

void floodfill(int x,int y)
{
     if (!b[x][y])
     {
                 cc=a[x][y];
                 return;
     }
     len++;
     q[len][0]=x;
     q[len][1]=y;
     b[x][y]=false;
     int px,py,pp=30000;
     for (int i=0;i<4;i++)
     {
         int xx=x+d[i][0],yy=y+d[i][1];
         if (xx>0&&xx<=h&&yy>0&&yy<=w&&pp>map[xx][yy])
         {
                                          pp=map[xx][yy];
                                          px=xx;
                                          py=yy;
         }
     }
     if (pp<map[x][y]) floodfill(px,py);
}

int main()
{
    freopen("gcj2.in","r",stdin);
    freopen("gcj2.out","w",stdout);
    cin>>t;
    int tt=1;
    while (tt<=t)
    {
          scanf("%d%d",&h,&w);
          for (i=1;i<=h;i++)
              for (j=1;j<=w;j++)
                  scanf("%d",&map[i][j]);
          memset(b,true,sizeof(b));
          i=1;
          c='a';
          for (i=1;i<=h;i++)
              for (j=1;j<=w;j++)
                  if (b[i][j])
                  {
                     cc=c;
                     len=0;
                     floodfill(i,j);
                     for (k=1;k<=len;k++) a[q[k][0]][q[k][1]]=cc;
                     if (cc==c) c++;
                  }
          cout<<"Case #"<<tt<<":"<<endl;
          for (i=1;i<=h;i++)
          {
              for (j=1;j<w;j++)
                  cout<<a[i][j]<<' ';
              cout<<a[i][w]<<endl;
          }
          tt++;
    }
    return 0;
}
