#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>
using namespace std;
#define p(x) cout<<#x<<":"<<x<<"\n"
#define lim 101

int cs,c,i,n,j;
double OWP[lim],OOWP[lim];
int S[lim],W[lim],P[lim][lim];
char A[lim][lim];

int main()
{
  scanf("%d",&cs);
  for(c=1;c<=cs;c++)
  {
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
      S[i]=W[i]=0;
      scanf("%s",A[i]);
      for(j=0;j<n;j++)
      {
        P[i][j]=-1;
        if(A[i][j]!='.')
        {
          P[i][j]=0;
          S[i]++;
          if(A[i][j]=='1')
          {
            W[i]++;
            P[i][j]=1;
          }
        }
      }
    }
    for(i=0;i<n;i++)
    {
      for(OWP[i]=j=0;j<n;j++)
        if(A[i][j]!='.')
          OWP[i]+=(double)(W[j]-P[j][i])/(S[j]-1);
      OWP[i]/=S[i];
    }
    for(i=0;i<n;i++)
    {
      for(OOWP[i]=j=0;j<n;j++)
        if(A[i][j]!='.')
          OOWP[i]+=OWP[j];
      OOWP[i]/=S[i];
    }
    printf("Case #%d:\n",c);
    for(i=0;i<n;i++)
      printf("%.10lf\n",.25*W[i]/S[i]+.5*OWP[i]+.25*OOWP[i]);
  }
  return 0;
}
