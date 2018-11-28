#include <cstdio>
#include <cstring>

int L, D, N, i, lung, j, k, p, nr;
char S[450], W[5005][20], B[5005];

void citire()
{
 freopen("a.in","r",stdin);
 scanf("%d %d %d\n",&L, &D, &N);
 for (i=0; i<D; ++i)
     scanf("%s\n",&W[i]);
}

int main()
{
 freopen("a.out","w",stdout);
 citire();
 
 for (i=1; i<=N; ++i)
     {
      scanf("%s\n", &S);
      lung = strlen(S);
      p=j=0; 
      memset(B, 0 ,sizeof(B));
      while (p<lung)
            {             
             if (S[p] == '(')
                {
                 ++p;
                 while (S[p] != ')' )
                      {
                       for (k=0; k<D; ++k)
                           if (W[k][j] == S[p])
                              ++B[k];
                       ++p;
                      }
                }
                else
                    for (k=0; k<D; ++k)
                        B[k] += (W[k][j] == S[p]);
             ++p;             
             ++j;   
            }
      for (k=0,nr=0; k<D; ++k)
          nr += (B[k] == L);
      printf("Case #%d: %d\n",i,nr);
     }
 
 return 0;
}
