using namespace std;
#include <cstdio>
#include <cstring>
#include <algorithm>

#define Lmax 1024

int N,nn;
int P,K,L;
int i;
int A[Lmax],nr;

int main()
{
 freopen("a.in","r",stdin);
 freopen("a.out","w",stdout);
 scanf("%d",&N);
 for (nn=1; nn<=N; ++nn)
     {
      scanf("%d %d %d",&P,&K,&L);
      for (i=1;i<=L;++i)
          scanf("%d",&A[i]);
          
      sort(A+1,A+L+1);
      for (i=L,nr=0; i>=1; --i)
          nr+=A[i] * ((L-i)/K + 1);
      printf("Case #%d: %d\n",nn,nr);
     }
 return 0;
}
