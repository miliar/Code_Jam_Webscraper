#include <stdio.h>
#include <stdlib.h>

int pos[5001];
int r[5001];
int cola[100000000];

main()
{
      int n, li, ls, j,N,t,a,nc=1;
      FILE *in = fopen("C-small-attempt0.in","r");
      FILE *out = fopen("C-small.out","w");
      //FILE *in = fopen("A-large.in","r");
      //FILE *out = fopen("A-large.out","w");
      fscanf(in,"%d",&n);
      while(n--)
      {
                printf("%d\n",n);
                fscanf(in,"%d",&N);
                for(int i=0;i<N;i++)
                {
                        cola[i] = i;
                }
                li = 0;
                ls = N;
                j = 0;
                while(j<N)
                {
                            for(int i=0;i<j;i++)
                            {
                                    cola[ls++] = cola[li++];
                            }
                            pos[j] = cola[li++];
                            j++;
                }
                for(int i=0;i<N;i++)
                {
                        r[pos[i]] = i+1;
                }
                fscanf(in,"%d",&t);
                fprintf(out,"Case #%d: ",(nc++));
                for(int i=0;i<t;i++)
                {
                        fscanf(in,"%d",&a);
                        if(i) fprintf(out," ");
                        fprintf(out,"%d",r[a-1]);
                }
                fprintf(out,"\n");
      }
      return 0;
}
