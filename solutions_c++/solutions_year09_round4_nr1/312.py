#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
using namespace std;

#define MAXN (60)

long long G[MAXN];
char s[MAXN];

main()
{
      int T, N, nc=1, r, remp;
      long long temp;
      FILE *in = fopen("A-small-attempt0.in","r");
      FILE *out = fopen("a.out","w");
      fscanf(in,"%d",&T);
      while(T--)
      {
                fscanf(in,"%d",&N);
                for(int i=0;i<N;i++)
                {
                       fscanf(in,"%s",s);
                       G[i]=0;
                       for(int j=N-1;j>=0;j--)
                               G[i] = G[i]*2 + (s[j]-'0'); 
                }
                r=0;
                for(int i=0;i<N;i++)
                {
                        if(G[i]>(1<<(i+1))-1)
                        {
                               for(int j=i;j<N;j++)
                               {
                                       if(G[j]<=(1<<(i+1))-1)
                                       {
                                           remp=j;
                                           break;
                                       }
                               }   
                               //printf("remp %d con %d\n",i,remp);
                               r+= (remp-i);
                               for(int j=remp;j>i;j--)
                               {
                                      temp = G[j];
                                      G[j] = G[j-1];
                                      G[j-1] = temp; 
                               }           
                        }
                }
                fprintf(stdout,"Case #%d: %d\n",nc,r);
                fprintf(out,"Case #%d: %d\n",nc++,r);
    }
  system("PAUSE");
  return 0;
}
