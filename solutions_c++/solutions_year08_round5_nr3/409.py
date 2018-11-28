#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <algorithm>
using namespace std;

#define MAX 11
#define INF 100000

int T[MAX][(1<<MAX)];
char tt[MAX][MAX+1];
int W,H;

int mejor(int r, int c)
{
    int res=0, t;
    if(r==H) return 0;
    if(T[r][c]!=-1) return T[r][c];
    int *x;
    int x2[MAX+4];
    int d2[MAX+4];
    memset(x2,0,sizeof(x2));
    memset(d2,0,sizeof(d2));
    x = x2+2;
    int *d = d2+2;
    for(int i=0;i<W;i++)
            x[i] = (c>>i)&1;
    for(int i=0;i<(1<<W);i++)
    {
            t = 0;
            for(int j=0;j<W;j++)
            {
                    d[j] = (i>>j)&1;
                    t+=d[j];
            }
            for(int j=0;j<W;j++)
                    if(d[j]==1&&(d[j-1]==1||d[j+1]==1||x[j-1]==1||x[j+1]==1||tt[r][j]!='.'))
                         t = -INF;
            res >?= (t + mejor(r+1,i));           
    }
    return T[r][c] = res;
}


main()
{
      int t,nc=1;
      
      FILE *in = fopen("C-small-attempt2.in","r");
      FILE *out = fopen("C-small.out","w");
      
      fscanf(in,"%d",&t);
      while(t--)
      {
             printf("%d\n",t);
             fscanf(in,"%d %d",&H,&W);
             for(int i=0;i<H;i++)
                     fscanf(in,"%s",tt[i]); 
             fprintf(out,"Case #%d: ",nc++);
             memset(T,-1,sizeof(T));
             fprintf(out,"%d",mejor(0,0));            
             fprintf(out,"\n");
      }
      system("PAUSE");
      fclose(out);
      return 0;
}
