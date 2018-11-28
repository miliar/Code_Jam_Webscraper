#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

#define MAX 10010L

#define AND 0L
#define OR  1L
#define INF 99999L

#define max(a,b) (((a)>(b))?(a):(b))
#define min(a,b) (((a)<(b))?(a):(b))

int main()
{
  int q,Q;
  int a,b,c,d,e,s,num;
  int nodo[MAX][2];
  int oper[MAX][2];

  scanf(" %d",&Q);
  for(q=1;q<=Q;q++)
  {
    scanf(" %d %d",&num,&s);
    for(a=1;a<=(num-1)/2;a++)
    {
      scanf(" %d %d",&b,&c);
      d=((b==1)?AND:OR);
      oper[a][d]=0;
      oper[a][1-d]=((c==1)?1:INF);
      nodo[a][0]=INF;
      nodo[a][1]=INF;
    }
    for(;a<=num;a++)
    {
      scanf(" %d",&b);
      nodo[a][b]=0;
      nodo[a][1-b]=INF;
    }

    for(a=(num-1)/2;a>=1;a--)
    {
      nodo[a][0]=min(nodo[a][0],nodo[2*a][0]+nodo[2*a+1][0]+oper[a][AND]);
      nodo[a][0]=min(nodo[a][0],nodo[2*a][0]+nodo[2*a+1][1]+oper[a][AND]);
      nodo[a][0]=min(nodo[a][0],nodo[2*a][1]+nodo[2*a+1][0]+oper[a][AND]);
      nodo[a][1]=min(nodo[a][1],nodo[2*a][1]+nodo[2*a+1][1]+oper[a][AND]);

      nodo[a][0]=min(nodo[a][0],nodo[2*a][0]+nodo[2*a+1][0]+oper[a][OR]);
      nodo[a][1]=min(nodo[a][1],nodo[2*a][0]+nodo[2*a+1][1]+oper[a][OR]);
      nodo[a][1]=min(nodo[a][1],nodo[2*a][1]+nodo[2*a+1][0]+oper[a][OR]);
      nodo[a][1]=min(nodo[a][1],nodo[2*a][1]+nodo[2*a+1][1]+oper[a][OR]);
    }

    printf("Case #%d: ",q);
    if(nodo[1][s]>1000)
      printf("IMPOSSIBLE");
    else
      printf("%d",nodo[1][s]);
    printf("\n");
  }

  return(0);
}
