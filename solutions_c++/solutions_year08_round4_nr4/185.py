using namespace std;
#include <cstdio>
#include <cstring>
#include <algorithm>

int N,nn;
int K,L;
char S[50005];
int S2[50005];
int P[20],i,j,nr,minim;

int main()
{
 freopen("d.in","r",stdin);
 freopen("d.out","w",stdout);
 scanf("%d\n",&N);
 for (nn=1; nn<=N; ++nn)
     {
      scanf("%d\n",&K);
      scanf("%s\n",&S);
      
      L=strlen(S);
      minim=L+1;
      
      for (i=0;i<K;++i)
          P[i]=i;
      do
            {
             i=0;
             while (K*(i+1)<=L)
                   {
                    for (j=0;j<K;++j)
                        S2[K*i+j] = S[K*i+P[j]];
                    ++i;
                   }
             nr=1;
             for (i=0; i<L-1; ++i)
                 if (S2[i]!=S2[i+1]) ++nr;
             if (nr<minim) minim=nr;
            }
      while ( next_permutation( P, P+K ) );
      printf("Case #%d: %d\n",nn,minim);      
     }
}
