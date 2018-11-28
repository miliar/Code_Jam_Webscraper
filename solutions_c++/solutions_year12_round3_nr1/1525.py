#include <iostream>
#include <stdio.h>
#include <cmath>
using namespace std;

const int MAXN=100;
typedef int matrix[MAXN+1][MAXN+1];//矩阵类型定义(int*int可能会超出int)

/************************************************
                   矩阵加法
A,B,C均可为同一矩阵
************************************************/
void Plus(matrix A,matrix B,matrix C,int n,int m)
{
  int i,j;

  for (i=1; i<=n; ++i)
    for (j=1; j<=m; ++j)
      C[i][j]=A[i][j]+B[i][j];
}
/*=============================================*/


/************************************************
                   矩阵乘法
A,B,C均可为同一矩阵
************************************************/
void Mul(matrix A,matrix B,matrix C,int n,int l,int m)
{
  matrix buffer;
  int i,j,k;

  for (i=1; i<=n; ++i)
    for (j=1; j<=m; ++j)
      {
        buffer[i][j]=0;
        for (k=1; k<=l; ++k)
          buffer[i][j]+=A[i][k]*B[k][j];
      }

  for (i=1; i<=n; ++i)
    for (j=1; j<=m; ++j)
      C[i][j]=buffer[i][j];
}
/*=============================================*/


/************************************************
                  矩阵快速幂
B=A^n，n>=0，矩阵是k*k的
矩阵buffer(简称b)要保证：
1、b*b=b
2、b*A=A，A*b=A
************************************************/
void fast_pow(matrix A,int k,long long int n,matrix B)
{
  matrix buffer;
  int i,j;

  for (i=1; i<=k; ++i)
    for (j=1; j<=k; ++j)
      buffer[i][j]=(i==j)?1:0;
  if (n>0)
    for (i=(int)(log(n)/log(2))+1; i>=0; --i)
      {
        Mul(buffer,buffer,buffer,k,k,k);//b=b*b
        if (n&((1LL)<<i)) Mul(buffer,A,buffer,k,k,k);//b=b*a
      }

  for (i=1; i<=k; ++i)
    for (j=1; j<=k; ++j)
      B[i][j]=buffer[i][j];
}
/*=============================================*/

int main()
{
  freopen("A-small-attempt0.in","r",stdin);
  freopen("A-small-attempt0.out","w",stdout);
  
  int T,i,j,k;

  scanf("%d",&T);
  for (i=1; i<=T; ++i)
    {
      matrix map={0},sum={0},t={0};
      int n;
      
      scanf("%d",&n);
      for (j=1; j<=n; ++j)
        {
          scanf("%d",&k);
          while (k--)
            {
              int t;
              
              scanf("%d",&t);
              map[j][t]=1;
            }
        }

      for (j=1; j<=n; ++j)
        {
          fast_pow(map,n,j,t);
          Plus(sum,t,sum,n,n);
        }
        
      bool find=false;
      for (j=1; j<=n; ++j)
        for (k=1; k<=n; ++k)
          if (j!=k&&sum[j][k]>1)
            find=true;
            
      if (find) printf("Case #%d: Yes\n",i);
      else printf("Case #%d: No\n",i);
    }

  fclose(stdin);
  fclose(stdout);
  
  return(0);
}
