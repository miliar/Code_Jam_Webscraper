#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 101

int M[MAX][MAX],n,m;
char D[MAX][MAX];

void sucesor(int i, int j, int *ip, int *jp)
{
     int low = M[i][j];
     if(i>0) low <?= M[i-1][j];
     if(j>0) low <?= M[i][j-1];
     if(i!=n-1) low <?= M[i+1][j];
     if(j!=m-1) low <?= M[i][j+1];
     *ip = i;
     *jp = j;
     if(low==M[i][j])
                     *ip=-1;
     else if(i>0&&M[i-1][j]==low)
                     *ip=i-1;     
     else if(j>0&&M[i][j-1]==low)
                     *jp=j-1;     
     else if(j!=m-1&&M[i][j+1]==low)
                     *jp=j+1;     
     else if(i!=n-1&&M[i+1][j]==low)
                     *ip=i+1;      
}

char pintar(int i, int j, char c)
{
     int ip,jp;
     if(D[i][j]!='X') return D[i][j];
     D[i][j] = c;
     sucesor(i,j,&ip,&jp);
     if(ip==-1)
               return c;
     char nc = pintar(ip, jp, c);
     if(nc!=c)
              D[i][j] = nc;
     return D[i][j];
}

main()
{
      FILE *in = fopen("B-large.in","r");
      FILE *out = fopen("b.out.txt","w");
      int N, nc=1;
      char l;
      fscanf(in,"%d",&N);
      while(N--)
      {
                fscanf(in,"%d %d",&n,&m);
                for(int i=0;i<n;i++)
                        for(int j=0;j<m;j++)
                                fscanf(in,"%d",&M[i][j]);
                memset(D,'X',sizeof(D));
                l = 'a';
                for(int i=0;i<n;i++)
                        for(int j=0;j<m;j++)
                                if(pintar(i,j,l)==l)
                                                    l++;
                fprintf(out,"Case #%d:\n",nc++);
                for(int i=0;i<n;i++)
                {
                        for(int j=0;j<m;j++)
                                fprintf(out, "%c ",D[i][j]);
                        fprintf(out,"\n");
                }
      }
      fclose(out);
      system("PAUSE");
      return 0;
}
