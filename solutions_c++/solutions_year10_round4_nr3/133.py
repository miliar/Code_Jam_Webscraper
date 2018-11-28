#include<iostream>
#include<fstream>
using namespace std;

int t,r;
int a[101][101],b[101][101];

int main()
{
    ifstream fin("c.in");
    ofstream fout("c.out");
    fin>>t;
    int z=1;
    while (z<=t)
    {
          for (int i=0;i<=100;i++)
          for (int j=0;j<=100;j++)
          {a[i][j]=0;b[i][j]=0;}
          fin>>r;
          int time=0;
          int x1,x2,y1,y2;
          for (int k=0;k<r;k++)
          {
           fin>>x1>>y1>>x2>>y2;
           for (int i=x1;i<=x2;i++)
            for (int j=y1;j<=y2;j++)
             a[i][j]=1;
          }
         
             int num=1;
          while (num>0)
          {
                num=0;
                time++;
                
           for (int i=1;i<=100;i++)
            for (int j=1;j<=100;j++)
            {
                
            //if (a[i][j]==1) 
            b[i][j]=a[i][j];
            if (a[i-1][j]!=1 && a[i][j-1]!=1) b[i][j]=0;
            if (a[i-1][j]==1 && a[i][j-1]==1) b[i][j]=1;
            if (b[i][j]==1) num++;
            }
            for (int i=1;i<=100;i++)
            for (int j=1;j<=100;j++)
            {a[i][j]=b[i][j];
            b[i][j]=0;
            }
            }
            fout<<"Case #"<<z<<": "<<time<<endl;  
           
 
          z++;
    }
    system("pause");
    return 0;
}
    
