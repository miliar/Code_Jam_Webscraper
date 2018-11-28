#include<iostream>
using namespace std;
const int maxl=20;
int dx[]={0,1,0,-1};
int dy[]={1,0,-1,0};
int l1,l2,test,tt,v[maxl][maxl],sx,sy,ex,ey,tot[maxl][maxl],xx[maxl][maxl][5],yy[maxl][maxl][5],d[maxl][maxl],qx[maxl*maxl],qy[maxl*maxl];
void init()
{
     scanf("%d%d\n",&l1,&l2);
     int i,j;
     char ch;
     for (i=0;i<l1;i++)
     {
         for (j=0;j<l2;j++)
         {
             scanf("%c",&ch);
             if (ch=='#') v[i][j]=0;
             else v[i][j]=1;
             if (ch=='O')
             {
                sx=i;
                sy=j;
             }
             if (ch=='X')
             {
                ex=i;
                ey=j;
             }
         }
         scanf("\n");
     }        
}

int check(int x,int y)
{
    if (x<0) return 0;
    if (y<0) return 0;
    if (x>=l1) return 0;
    if (y>=l2) return 0;
    return v[x][y];
}

void print(int ans)
{
     printf("Case #%d: ",tt);
     if (ans==-1) printf("THE CAKE IS A LIE\n");
     else printf("%d\n",ans-1);
}

void work()
{
     memset(tot,0,sizeof(tot));
     int h,t,i,j,k,x1,y1,ok;
     for (i=0;i<l1;i++)
         for (j=0;j<l2;j++)     
         {
             ok=0;
             for (k=0;k<4;k++)
             if (!check(i+dx[k],j+dy[k])) ok=1;
             if (ok)
             {
                for (k=0;k<4;k++)
                {
                    x1=i;
                    y1=j;
                    for (;check(x1+dx[k],y1+dy[k]);)
                    {
                        x1+=dx[k];
                        y1+=dy[k];
                    }
                       tot[i][j]++;
                       xx[i][j][tot[i][j]]=x1;
                       yy[i][j][tot[i][j]]=y1;
                }
             }
             
         }
     memset(d,0,sizeof(d));
     d[sx][sy]=1;
     h=0;
     t=1;
     qx[1]=sx;
     qy[1]=sy;
     for (;h<t;)
     {
         h++;
         for (i=0;i<4;i++)
         {
             x1=qx[h]+dx[i];
             y1=qy[h]+dy[i];
             if (check(x1,y1))
                if (d[x1][y1]==0)
                {
                   t++;
                   qx[t]=x1;
                   qy[t]=y1;
                   d[x1][y1]=d[qx[h]][qy[h]]+1;
                   if ((x1==ex)&&(y1==ey))
                   {
                      print(d[x1][y1]);
                      return;
                   }
                }
         }
         for (i=1;i<=tot[qx[h]][qy[h]];i++)
         {
             x1=xx[qx[h]][qy[h]][i];
             y1=yy[qx[h]][qy[h]][i];
                if (d[x1][y1]==0)
                {
                   t++;
                   qx[t]=x1;
                   qy[t]=y1;
                   d[x1][y1]=d[qx[h]][qy[h]]+1;
                   if ((x1==ex)&&(y1==ey))
                   {
                      print(d[x1][y1]);
                      return;
                   }
                }
         }
     }
     print(-1);
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    for (scanf("%d",&test),tt=1;tt<=test;tt++)
    {
        init();
        work();
    }
    return 0;
}
