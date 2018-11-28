#include<iostream>
#include<algorithm>
using namespace std;
char str[510][510];
long long x[510][510],y[510][510],z[510][510],sumx[510][510],sumy[510][510],sumz[510][510];
long long summx(long long x1,long long y1)
{
     if(x1<0||y1<0)
     return 0;
     return sumx[x1][y1];
     }
long long qsumx(long long x1,long long y1,long long x2,long long y2)
{
     long long qsum=summx(x2,y2)-summx(x2,y1-1)-summx(x1-1,y2)+summx(x1-1,y1-1);
     return qsum-x[x1][y1]-x[x1][y2]-x[x2][y1]-x[x2][y2];
     }
long long summy(long long x1,long long y1)
{
     if(x1<0||y1<0)
     return 0;
     return sumy[x1][y1];
     }
long long qsumy(long long x1,long long y1,long long x2,long long y2)
{
     long long qsum=summy(x2,y2)-summy(x2,y1-1)-summy(x1-1,y2)+summy(x1-1,y1-1);
     return qsum-y[x1][y1]-y[x1][y2]-y[x2][y1]-y[x2][y2];
     }
long long summz(long long x1,long long y1)
{
     if(x1<0||y1<0)
     return 0;
     return sumz[x1][y1];
     }
long long qsumz(long long x1,long long y1,long long x2,long long y2)
{
     long long qsum=summz(x2,y2)-summz(x2,y1-1)-summz(x1-1,y2)+summz(x1-1,y1-1);
     return qsum-z[x1][y1]-z[x1][y2]-z[x2][y1]-z[x2][y2];
     }
bool check(long long x1,long long y1,long long x2,long long y2)
{
     if(2*qsumx(x1,y1,x2,y2)!=qsumz(x1,y1,x2,y2)*(x1+x2))
     return false;
     if(2*qsumy(x1,y1,x2,y2)!=qsumz(x1,y1,x2,y2)*(y1+y2))
     return false;
     return true;
     }
int main()
{
     freopen("B-large.in","r",stdin);
     freopen("B-large.out","w",stdout);

     long long T,r,c,d;
     long long t,i,j,k;

     scanf("%I64d",&T);
     for(t=1;t<=T;t++)
     {
          scanf("%I64d%I64d%I64d",&r,&c,&d);
          for(i=0;i<r;i++)
          {
               scanf("%s",str[i]);
               for(j=0;j<c;j++)
               {
                    x[i][j]=i*(str[i][j]-'0');
                    y[i][j]=j*(str[i][j]-'0');
                    z[i][j]=str[i][j]-'0';
                    }
               }

          /*for(i=0;i<r;i++)
          {
               for(j=0;j<c;j++)
               printf("%I64d ",x[i][j]);
               printf("\n");
               }
          printf("\n");
          for(i=0;i<r;i++)
          {
               for(j=0;j<c;j++)
               printf("%I64d ",y[i][j]);
               printf("\n");
               }
          printf("\n");*/

          sumx[0][0]=x[0][0];
          for(j=1;j<c;j++)
          sumx[0][j]=sumx[0][j-1]+x[0][j];
          for(i=1;i<r;i++)
          {
               sumx[i][0]=sumx[i-1][0]+x[i][0];
               for(j=1;j<c;j++)
               sumx[i][j]=sumx[i][j-1]+sumx[i-1][j]-sumx[i-1][j-1]+x[i][j];
               }

          sumy[0][0]=y[0][0];
          for(j=1;j<c;j++)
          sumy[0][j]=sumy[0][j-1]+y[0][j];
          for(i=1;i<r;i++)
          {
               sumy[i][0]=sumy[i-1][0]+y[i][0];
               for(j=1;j<c;j++)
               sumy[i][j]=sumy[i][j-1]+sumy[i-1][j]-sumy[i-1][j-1]+y[i][j];
               }

          sumz[0][0]=z[0][0];
          for(j=1;j<c;j++)
          sumz[0][j]=sumz[0][j-1]+z[0][j];
          for(i=1;i<r;i++)
          {
               sumz[i][0]=sumz[i-1][0]+z[i][0];
               for(j=1;j<c;j++)
               sumz[i][j]=sumz[i][j-1]+sumz[i-1][j]-sumz[i-1][j-1]+z[i][j];
               }

          /*for(i=0;i<r;i++)
          {
               for(j=0;j<c;j++)
               printf("%I64d ",sumx[i][j]);
               printf("\n");
               }
          printf("\n");
          for(i=0;i<r;i++)
          {
               for(j=0;j<c;j++)
               printf("%I64d ",sumy[i][j]);
               printf("\n");
               }
          printf("\n");*/

          //printf("%I64d %I64d %I64d",check(1,1,5,5),check(1,1,4,4),check(1,1,3,3));

          long long maxx=-1;
          for(i=0;i<r;i++)
          {
               for(j=0;j<c;j++)
               {
                    for(k=2;k<min(r-i,c-j);k++)
                    {
                         if(check(i,j,i+k,j+k))
                         maxx=max(maxx,k);
                         }
                    }
               }
          printf("Case #%I64d: ",t);
          if(maxx!=-1)
          printf("%I64d\n",maxx+1);
          else
          printf("IMPOSSIBLE\n");
          }

     return 0;
     }
