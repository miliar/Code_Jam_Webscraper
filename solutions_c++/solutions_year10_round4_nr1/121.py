#include<iostream>
#include<fstream>
using namespace std;

int a[200][200];
int t,k;

bool can(int x,int y)
{
     bool can=true;
     for (int i=1;i<2*k;i++)
      for (int j=1;j<2*k;j++)
          if (a[i][j]!=-1)
          {
                  int xx=x+(x-i);
                  int yy=j;
                  if (xx>0 && xx<2*k)
                  if (a[xx][yy]!=-1 && a[xx][yy]!=a[i][j]) return false;
                  xx=i;
                  yy=y+(y-j);
                  if (yy>0 && yy<2*k)
                  if (a[xx][yy]!=-1 && a[xx][yy]!=a[i][j]) return false;
                  xx=x+(x-i);
                  yy=y+(y-j);
                  if (xx>0 && xx<2*k && yy>0 && yy<2*k )
                  if (a[xx][yy]!=-1 && a[xx][yy]!=a[i][j]) return false;
          
          }
      return true;
}
                  

int main()
{
    ifstream fin("a.in");
    ofstream fout("a.out");
    fin>>t;
    int z=1;
    while (z<=t)
    {
          
          for (int i=0;i<200;i++)
           for (int j=0;j<200;j++)
            a[i][j]=-1;
          fin>>k;
          for (int i=1;i<2*k;i++)
          {
              if (i<=k)
                 for (int j=k-i+1;j<=k+i-1;j+=2)
                     fin>>a[i][j];
              else
                  for (int j=i-k+1;j<=3*k-i-1;j+=2)
                      fin>>a[i][j];
          }
          
          /*for (int i=1;i<2*k;i++)
          {
           for (int j=1;j<2*k;j++)
            if (a[i][j]!=-1) cout<<a[i][j];else cout<<' ';
            cout<<endl;
           }*/
           int min=1000000;
          for (int i=1;i<2*k;i++)
           for (int j=1;j<2*k;j++)
               if (can(i,j))
               {
                  int w;
                  w=k+abs(i-k)+abs(j-k);
                  if (w<min) min=w;
               }
           fout<<"Case #"<<z<<": "<<min*min-k*k<<endl;
           z++;      
    }
    return 0;
}
