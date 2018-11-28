using namespace std;

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>

inline int min(int a,int b) { return a<b?a:b; }
inline int max(int a,int b) { return a>b?a:b; }
int cmp(const int &a, const int &b) { return a<b; }

int N, T, t, i, j, k, aux, best, nr;
int P[60], C[60], L[60];
char S[60][60];

int main()
{
 freopen("a.in","r",stdin);
 freopen("a.out","w",stdout);
 
 scanf("%d",&T);
 for (t=1; t<=T; ++t)
     {
      scanf("%d\n",&N);
      for (i=1; i<=N; ++i)
          {
           scanf("%s\n",&S[i]);
           for (j=N-1; j>0 && S[i][j]=='0'; --j);
           L[i] = j + 1;
           //printf("%s %d\n",S[i],L[i]);
          }
          
      for (i=1; i<=N; ++i) P[i] = i;    
      best = N*N;
      do 
      {
       for (i=1; i<=N; ++i) C[i]=i;
       nr=0;
       for (i=N; i>=1; --i)
           {
            for (j=1; j<=i; ++j)
                if (P[i]==C[j])
                   {                    
                    k=j;
                    while (k!=i)
                          {
                           aux = C[k+1];
                           C[k+1] = C[k];
                           C[k] = aux;
                           ++k;
                           ++nr;
                          }
                    break;
                   }
           }
       //verifica
       for (i=1; i<=N; ++i)
           if (L[C[i]]>i) break;
       if (i>N && nr<best) best=nr;    
      }
      while (next_permutation(P+1, P+N+1));
      printf("Case #%d: %d\n",t,best);
     }
 
 return 0;
}
