#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <algorithm>
using namespace std;

#define MAX 100002

int M,V,A[MAX];
bool C[MAX];
int v[MAX][2];

int menor(int n, int p)
{
    //printf("%d %d %d\n",n,p,C[n]);
    int m=MAX;
    if(n>M) return MAX;
    if(v[n][p]!=-1) return v[n][p];
    if(n>(M-1)/2)
                   return (A[n]==p?0:MAX);
    
    if(p==1)
    {
            if(A[n]==1)
            {
                //printf("%d %d %d\n",n,p,m);
                m <?= menor(2*n,1) + menor(2*n+1,1);
                //printf("%d %d %d\n",n,p,m);
                if(C[n])
                {
                        m <?= menor(2*n,1) +1;
                        m <?= menor(2*n+1,1) +1;
                }
                //printf("%d %d %d\n",n,p,m);
            }
            else
            {
                m <?= menor(2*n,1);
                m <?= menor(2*n+1,1);
            }
    }
    if(p==0)
    {
            if(A[n]==0)
            {
                m <?= menor(2*n,0) + menor(2*n+1,0);
                if(C[n])
                {
                        m <?= menor(2*n,0) +1;
                        m <?= menor(2*n+1,0) +1;
                }
            }
            else
            {
                        m <?= menor(2*n,0);
                        m <?= menor(2*n+1,0);
            }
    }
    //printf("%d %d %d\n",n,p,m);
    return v[n][p]=m;
}

main()
{
      int n,T,nc=1;
      int a,b;
      //FILE *in = fopen("A-small-attempt2.in","r");
      //FILE *out = fopen("A-small.out","w");
      FILE *in = fopen("A-large.in","r");
      FILE *out = fopen("A-large.out","w");
      fscanf(in,"%d",&T);
      while(T--)
      {
             fscanf(in,"%d %d",&M,&V);
             for(int i=1;i<=(M-1)/2;i++)
                    fscanf(in,"%d %d",&A[i],&C[i]);
             for(int i=1+(M-1)/2;i<=M;i++)
                     fscanf(in,"%d",&A[i]);
             memset(v,-1,sizeof(v));
             int m = menor(1,V);
             fprintf(out,"Case #%d: ",nc++);
             if(m<MAX)
                      fprintf(out,"%d\n",m);
             else
                      fprintf(out,"IMPOSSIBLE\n");
      }
      fclose(out);
      system("PAUSE");
      return 0;
}
