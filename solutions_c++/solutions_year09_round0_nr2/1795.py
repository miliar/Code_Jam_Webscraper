#include<fstream>
using namespace std;
bool u[100][100];
int a[100][100],next[100][100][2];
void dg(int i,int j,int& p,bool& change)
{
     if(!u[i][j])
     {
         change=true;
         p=a[i][j];
     }
     else
     {
         u[i][j]=false;
         a[i][j]=p;
         if(next[i][j][0]!=i || next[i][j][1]!=j)
         {
              dg(next[i][j][0],next[i][j][1],p,change);
              if(change)a[i][j]=p;
         }
         else p++;
     }
}
main()
{
      ifstream fcin("b.in");
      ofstream fcout("b.out");
      int mv[4][2]={{-1,0},{0,-1},{0,1},{1,0}};
      int m,mpx,mpy,i,j,k,t,h,w,te,ch;
      char c[27];
      bool y[27];
      fcin>>t;
      for(te=1;te<=t;te++)
      {
          fcin>>h>>w;
          for(i=0;i<h;i++)
          {
              for(j=0;j<w;j++)
              {
                  fcin>>a[i][j];next[i][j][0]=-1;next[i][j][1]=-1;
              }
          }
          for(i=0;i<h;i++)
          {
              for(j=0;j<w;j++)
              {
                  m=a[i][j];mpx=i;mpy=j;
                  for(k=0;k<4;k++)
                  {
                      if(!(i+mv[k][0]<0 || i+mv[k][0]>=h || j+mv[k][1]<0 || j+mv[k][1]>=w))
                      {
                          if(a[i+mv[k][0]][j+mv[k][1]]<m)m=a[i+mv[k][0]][j+mv[k][1]],mpx=i+mv[k][0],mpy=j+mv[k][1];
                      }
                  }
                  next[i][j][0]=mpx;next[i][j][1]=mpy;
              }
          }
          for(i=0;i<h;i++)for(j=0;j<w;j++)u[i][j]=true,a[i][j]=-1;
          ch=0;
          for(i=0;i<h;i++)for(j=0;j<w;j++)
              if(u[i][j])
              {
                   bool f=false;
                   int tem=ch;
                   dg(i,j,ch,f);
                   if(f)ch=tem;                  
              }
          for(i=0;i<ch;i++)y[i]=true;
          ch='a';          
          for(i=0;i<h;i++)for(j=0;j<w;j++)
          {
               if(a[i][j]<'a')
               {
                    if(y[a[i][j]])
                    {
                        c[a[i][j]]=ch++;
                        y[a[i][j]]=false;
                    }
               }
          }

          fcout<<"Case #"<<te<<":"<<endl;
          for(i=0;i<h;i++)
          {
               for(j=0;j<w;j++)fcout<<c[a[i][j]]<<' ';
               fcout<<endl;
          }
                    
      }
}
