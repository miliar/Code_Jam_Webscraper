#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
using namespace std;

#define MAXNODES (500)

struct tnode
{
  int c,d,fromwho;
};

int fromwho[MAXNODES];
int nreach[MAXNODES];
int reachs[MAXNODES][MAXNODES];
int path[MAXNODES];
int vis[MAXNODES];
int G[MAXNODES][MAXNODES];

int augment(int who, int cnt)
{
  int i,rcnt;
  if (!vis[who])
  {
    vis[who]=1;
    for (i=0;i<nreach[who];i++)
    {
      int con=fromwho[reachs[who][i]];
      path[cnt]=reachs[who][i];
      if (con==-1) return cnt+1;  
      rcnt=augment(con,cnt+1);
      if (rcnt) return rcnt;
    }
  }  
  return 0;
}

int main(void)
{
    
  FILE *in = fopen("C-large.in","r");
  FILE *out = fopen("c.out","w");
  
  int N,T,K,k,temp,graphs,cur,nc=1;
  
  fscanf(in,"%d",&N);
  while (N--)
  {
        fscanf(in,"%d %d",&T, &K);
        for (int i=0;i<T;i++)
        {
            for(int j=0;j<K;j++)
            {
                    fscanf(in,"%d",&G[i][j]);
            }
            fromwho[i]=-1;
            nreach[i]=0;
        }
        for(int i=0;i<T;i++)
            for(int j=0;j<T;j++)
            {
                    int reachable = true;
                    for(k=0;k<K;k++)
                                    if(G[i][k]>=G[j][k]) 
                                                         reachable = false;
                    if(reachable) reachs[j][nreach[j]++]=i;
            }
    graphs=0;
    for (int i=0;i<T;i++)
    {
      for (int j=0;j<T;j++) vis[j]=0;
      k=augment(i,0);
      graphs+=(!k);
      cur=i;
      for (int j=0;j<k;j++)
      {
        temp=fromwho[path[j]];
        fromwho[path[j]] = cur;
        cur=temp;  
      }
    }
    fprintf(stdout,"Case #%d: %d\n",nc,graphs);
    fprintf(out,"Case #%d: %d\n",nc++,graphs);
  }
  system("PAUSE");
  return 0;
}
