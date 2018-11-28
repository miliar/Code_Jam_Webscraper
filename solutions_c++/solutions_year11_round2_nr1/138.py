#include<iostream>
#include<algorithm>
#include<cmath>
#include<iomanip>
using namespace std;
char mat[211][210];
long double a[210];
long double b[210];
long double c[210];
int x[210];
int main()
{
    freopen("b1.txt","r",stdin);
    freopen("b2.txt","w",stdout);
    
    int cas;
    scanf("%d",&cas);
    for(int ii=1;ii<=cas;ii++)
    {
      
      int m;
      scanf("%d",&m);
      for(int i=0;i<m;i++)
      {
             scanf("%s",mat[i]);
      }
      
      for(int i=0;i<m;i++){
              x[i]=0;
              int y =0;
              for(int j=0;j<m;j++){
                      if(mat[i][j]=='.')continue;
                      x[i]++;
                      if(mat[i][j]=='1')y++;
                      }
                      a[i]=y*1.0L/x[i];
              }
      for(int i=0;i<m;i++){
              b[i]=0;
              int y =0;
              for(int j=0;j<m;j++){
                      if(mat[i][j]=='.')continue;
                      int x1 =0,y1=0;
                      for(int k=0;k<m;k++){
                              if(mat[j][k]=='.')continue;
                              if(i==k)continue;
                              y1++;
                              if(mat[j][k]=='1')x1++;
                              }
                      b[i]+=x1*1.0L/y1;
                      }
                      b[i]=b[i]/x[i];
              }
      for(int i=0;i<m;i++){
              c[i]=0;
              int y =0;
              for(int j=0;j<m;j++){
                      if(mat[i][j]=='.')continue;
                      c[i]+=b[j];
                      }
                      c[i]=c[i]/x[i];
              }
     printf("Case #%d:\n",ii);
     for(int i=0;i<m;i++){
            // printf("%d %.6lf %.6lf %.6lf ",x[i],(double)a[i],(double)b[i],(double)c[i]);
             printf("%.12lf\n",(double)(a[i]/4+b[i]/2+c[i]/4));
             }
      
    }
    
    return 0;
}
