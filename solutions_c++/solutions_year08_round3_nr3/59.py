#include <cstdio>
#include <cstring>

#define Nmax 500005
#define modulo 1000000007

int T,tt;
int N,M,X,Y,Z;
int i,j;
int A[Nmax],V[Nmax],nr[Nmax];
int s;

int main()
{
 freopen("c.in","r",stdin);
 freopen("c.out","w",stdout);
 scanf("%d",&T);
 
 for (tt=1; tt<=T; ++tt)
     {
      scanf("%d %d %d %d %d",&N,&M,&X,&Y,&Z);
      for (i=0; i<M; ++i)
          scanf("%d",&A[i]);
          
      s=0;    
      for (i=0; i<N; ++i)
          {
           V[i] = A[i % M];
           A[i % M] = ((long long)((long long)X * A[i % M]) +((long long)Y * (i + 1))) % Z;
          
           //dinamica n^2
           nr[i]=1;
           for (j=0;j<i;++j)
               if (V[j]<V[i]) nr[i]=(nr[i]+nr[j]) % modulo;
           s=(s+nr[i]) % modulo;
          }
      printf("Case #%d: %d\n",tt,s);
     }
 
 return 0;
}
