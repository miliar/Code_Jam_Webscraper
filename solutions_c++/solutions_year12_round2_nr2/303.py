#include <cstdio>
#include <cmath>
#include <utility>
#include <algorithm>
using namespace std;

#define x first
#define y second
const long long oo=19930309;

long long H,N,M;
long long C[100+2][100+2];
long long F[100+2][100+2];
long long T[100+2][100+2];
bool reach[100+2][100+2];

double calc()
{
       for (long long i=1;i<=N;i++)
           for (long long j=1;j<=M;j++)
               T[i][j]=oo,
               reach[i][j]=false;
       T[1][1]=0;
       for (;;)
       {
           long long mt=oo,mtx,mty;
           for (long long i=1;i<=N;i++)
               for (long long j=1;j<=M;j++)
                   if (mt>T[i][j]&&!reach[i][j])
                      mt=T[mtx=i][mty=j];
           if (mtx==N&&mty==M) return double(mt)/double(10);
           else
           {
               long long gx,gy,h;
               
               gx=mtx+1,gy=mty;
               h=H-mt;
               do
               {
                 if (C[gx][gy]-F[gx][gy]>=50&&min(C[gx][gy]-F[mtx][mty],C[mtx][mty]-F[gx][gy])>=50&&min(C[gx][gy]-h,C[mtx][mty]-h)>=50)
                 {
                    long long need;
                    if (h==H) need=0;
                    else
                    {
                        if (h-F[mtx][mty]>=20)
                        {
                           need=H-mt-h+10;
                           h=F[mtx][mty]+20;
                        }
                        else
                        {
                            need=H-mt-h+100;
                            h=0;
                        }
                    }
                    if (T[gx][gy]>mt+need)
                       T[gx][gy]=mt+need;
                 }
                 h--;
               }
               while (h>=0);
               
               gx=mtx-1,gy=mty;
               h=H-mt;
               do
               {
                 if (C[gx][gy]-F[gx][gy]>=50&&min(C[gx][gy]-F[mtx][mty],C[mtx][mty]-F[gx][gy])>=50&&min(C[gx][gy]-h,C[mtx][mty]-h)>=50)
                 {
                    long long need;
                    if (h==H) need=0;
                    else
                    {
                        if (h-F[mtx][mty]>=20)
                        {
                           need=H-mt-h+10;
                           h=F[mtx][mty]+20;
                        }
                        else
                        {
                            need=H-mt-h+100;
                            h=0;
                        }
                    }
                    if (T[gx][gy]>mt+need)
                       T[gx][gy]=mt+need;
                 }
                 h--;
               }
               while (h>=0);
               
               gx=mtx,gy=mty+1;
               h=H-mt;
               do
               {
                 if (C[gx][gy]-F[gx][gy]>=50&&min(C[gx][gy]-F[mtx][mty],C[mtx][mty]-F[gx][gy])>=50&&min(C[gx][gy]-h,C[mtx][mty]-h)>=50)
                 {
                    long long need;
                    if (h==H) need=0;
                    else
                    {
                        if (h-F[mtx][mty]>=20)
                        {
                           need=H-mt-h+10;
                           h=F[mtx][mty]+20;
                        }
                        else
                        {
                            need=H-mt-h+100;
                            h=0;
                        }
                    }
                    if (T[gx][gy]>mt+need)
                       T[gx][gy]=mt+need;
                 }
                 h--;
               }
               while (h>=0);
               
               gx=mtx,gy=mty-1;
               h=H-mt;
               do
               {
                 if (C[gx][gy]-F[gx][gy]>=50&&min(C[gx][gy]-F[mtx][mty],C[mtx][mty]-F[gx][gy])>=50&&min(C[gx][gy]-h,C[mtx][mty]-h)>=50)
                 {
                    long long need;
                    if (h==H) need=0;
                    else
                    {
                        if (h-F[mtx][mty]>=20)
                        {
                           need=H-mt-h+10;
                           h=F[mtx][mty]+20;
                        }
                        else
                        {
                            need=H-mt-h+100;
                            h=0;
                        }
                    }
                    if (T[gx][gy]>mt+need)
                       T[gx][gy]=mt+need;
                 }
                 h--;
               }
               while (h>=0);
               
               reach[mtx][mty]=true;
           }
       }
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    long long T;
    scanf("%I64d",&T);
    for (long long t=1;t<=T;t++)
    {
        scanf("%I64d%I64d%I64d",&H,&N,&M);
        for (long long i=0;i<=N+1;i++)
            for (long long j=0;j<=M+1;j++)
                C[i][j]=F[i][j]=0;
        for (long long i=1;i<=N;i++)
            for (long long j=1;j<=M;j++)
                scanf("%I64d",&C[i][j]);
        for (long long i=1;i<=N;i++)
            for (long long j=1;j<=M;j++)
                scanf("%I64d",&F[i][j]);
        printf("Case #%I64d: %.8f\n",t,calc());
    }
}
