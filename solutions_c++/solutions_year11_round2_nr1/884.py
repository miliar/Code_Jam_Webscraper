#include <iostream>
#include <vector>
#include <cstdio>
using namespace std;
int T,t,i,j,k,n;
int a[101][101];
char c;
int wined,played,tmp;
double wp[101],owp[101],oowp[101],s;
vector < double > v;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>T;
    for (t=1; t<=T; t++)
    {
        cin>>n;
        for (i=1; i<=n; i++)
         for (j=1; j<=n; j++)
         {
          cin>>c;
          if (c=='.') a[i][j]=2;
          if (c=='1') a[i][j]=1;
          if (c=='0') a[i][j]=0;
         }
         //calculate wps
         for (i=1;i<=n;i++)
          {
              wined=played=0;
              for (j=1; j<=n;j++)
              {
               if (a[i][j]!=2) played++;
               if (a[i][j]==1) wined++;
              }
              wp[i]=wined/double(played);
          }
         for (i=1; i<=n; i++)
         {
             v.clear();
             for (j=1; j<=n; j++)
              if (a[i][j]!=2)
              {
                 tmp=a[j][i];
                 a[j][i]=2;
                 wined=played=0;
                 for (k=1; k<=n;k++)
                  {
                    if (a[j][k]!=2) played++;
                    if (a[j][k]==1) wined++;
                  }
                v.push_back(wined/double(played));
                a[j][i]=tmp;
              }
              s=0;
              for (j=0; j<v.size();j++)
               s+=v[j];
              owp[i]=s/v.size();
         }
         for (i=1; i<=n; i++)
         {
             v.clear();
          for (j=1; j<=n;j++)
           if (a[i][j]!=2)
            v.push_back(owp[j]);
            s=0;
            for (j=0; j<v.size();j++)
              s+=v[j];
            oowp[i]=s/v.size();
         }
         cout<<"Case #"<<t<<":"<<endl;
         for (i=1; i<=n; i++)
          printf("%.7f\n",0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
    }


    return 0;
}
