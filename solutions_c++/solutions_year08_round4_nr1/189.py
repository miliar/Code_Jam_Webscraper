#include <cstdio>
#include <cstring>

#define Mmax 10005
#define inf 0x3f3f3f3f

int N,nn;
int M,V,i,val;
int G[Mmax],C[Mmax];
int A[Mmax],B[Mmax];

inline int min(int a,int b) { return a<b?a:b; }

void dfs(int nod)
{
 if ((nod<<1)>M) return;
 
 dfs(nod<<1);
 dfs((nod<<1)+1);
 
 if (G[nod]==1)
    {
     A[nod] = A[nod<<1] + A[(nod<<1)+1];
     if (C[nod] == 1)
        A[nod] = min( A[nod], min ( A[nod<<1], A[(nod<<1)+1] ) + 1 );
     B[nod] = min( B[nod<<1], B[(nod<<1)+1] );     
    }
 if (G[nod]==0)
    {
     A[nod] = min( A[nod<<1] , A[(nod<<1)+1] );
     B[nod] = B[nod<<1] + B[(nod<<1)+1];
     if (C[nod] == 1)
        B[nod] = min( B[nod], min( B[nod<<1], B[(nod<<1)+1] ) + 1 );
    } 
}

int main()
{
 freopen("a.in","r",stdin);
 freopen("a.out","w",stdout);
 scanf("%d",&N);
 for (nn=1; nn<=N; ++nn)
     {            
      scanf("%d %d",&M,&V);
      for (i=1; i<=M; ++i)
          A[i]=B[i]=2*M;
      for (i=1; i<=(M-1)/2; ++i)
          scanf("%d %d",&G[i],&C[i]);
      for (i=(M-1)/2+1; i<=M; ++i)
          {
           scanf("%d",&val);    
           if (val==1) A[i] = 0;
              else B[i] = 0;
          }
      dfs(1);
      if (V==1)
         if (A[1] < M) printf("Case #%d: %d\n",nn,A[1]);
            else printf("Case #%d: IMPOSSIBLE\n",nn);
         else
          if (B[1] < M) printf("Case #%d: %d\n",nn,B[1]);
            else printf("Case #%d: IMPOSSIBLE\n",nn);
     }    
 return 0;
}
