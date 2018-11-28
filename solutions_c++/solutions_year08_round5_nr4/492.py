using namespace std;

#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>

int N,nn;
int A[200][200];
int H,V,R,i,j,r,c;

int main()
{
 freopen("d.in","r",stdin);
 freopen("d.out","w",stdout);
 
 scanf("%d\n",&N);
 
 for (nn=1; nn<=N; ++nn)
     {
      scanf("%d %d %d",&H,&V,&R);
      memset(A,0,sizeof(A));
      for (i=1;i<=R;++i)
          {
           scanf("%d %d",&r,&c);
           A[r][c] = -1;
          }
      A[1][1] = 1;
      for (i=1;i<=H;++i)
          for (j=1;j<=V;++j)
           if (A[i][j] != -1)
              {
              if (A[i+1][j+2] != -1)
               A[i+1][j+2] = (A[i+1][j+2] + A[i][j]) % 10007;
              if (A[i+2][j+1] != -1) 
               A[i+2][j+1] = (A[i+2][j+1] + A[i][j]) % 10007;
              }
      if (A[H][V] == -1) A[H][V] = 0;
      printf("Case #%d: %d\n",nn,A[H][V]);
     }
 
 return 0;
}
