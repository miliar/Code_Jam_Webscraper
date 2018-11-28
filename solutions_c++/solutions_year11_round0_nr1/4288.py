#include<iostream>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T,N,M[101],O[101],B[101],i,j;
    char s[101];
    scanf("%d",&T);
    for (i=0; i<T; i++)
    {
        int Time = 0;
        int ol = 0, bl = 0;
        scanf("%d",&N);
        for (j=0; j<N; j++)
        {
            scanf(" %c %d",&s[j],&M[j]);
            if (s[j]=='O')
               O[ol++] = M[j];
            else
                B[bl++] = M[j];
        }
        int xO = 1, xB = 1;
        int lO = 0, lB = 0;
        for (j=0; j<N; j++)
        {
            if (s[j]=='O')
            {
               while (xO != M[j])
               {
                     if (xO < M[j])
                        xO++;
                     else
                         xO--;
                     Time++;
                     if (lB<bl && xB!=B[lB])
                        if (xB<B[lB])
                           xB++;
                        else
                            xB--;
               }
               //Push Button
               Time++;
               if (lB<bl && xB!=B[lB])
                  if (xB<B[lB])
                     xB++;
                  else
                      xB--;
               lO++;
            }
            else
            {
               while (xB != M[j])
               {
                     if (xB < M[j])
                        xB++;
                     else
                         xB--;
                     Time++;
                     if (lO<ol && xO!=O[lO])
                        if (xO<O[lO])
                           xO++;
                        else
                            xO--;
               }
               //Push Button
               Time++;
               if (lO<ol && xO!=O[lO])
                  if (xO<O[lO])
                     xO++;
                  else
                      xO--;  
               lB++;
            }
        }
        printf("Case #%d: %d\n",i+1,Time);
    }
}
