#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define MAX 1450L
#define A 0L
#define B 1L

int main()
{
  int N,T,num[2],qwer,a,q,sol[2];
  int sale[2][MAX],llega[2][MAX],hay[2][MAX];
  int h1,m1,h2,m2;

  scanf(" %d",&N);
  for(qwer=1;qwer<=N;qwer++)
  {
    scanf(" %d %d %d",&T,&num[A],&num[B]);
    
    memset(sale,0,sizeof(sale));
    memset(llega,0,sizeof(llega));
    memset(hay,0,sizeof(hay));

    for(q=0;q<2;q++)
    {
      sol[q]=0;
      for(a=0;a<num[q];a++)
      {
        scanf(" %d : %d %d : %d",&h1,&m1,&h2,&m2);
        m1+=h1*60;
        m2+=h2*60+T;
        sale[q][m1]++;
        llega[1-q][m2]++;
      }
    }

    for(a=0;a<MAX;a++)
    {
      for(q=0;q<2;q++)
      {
        if(a!=0)
          hay[q][a]=hay[q][a-1];
        else
          hay[q][a]=0;
        hay[q][a]+=llega[q][a];
        hay[q][a]-=sale[q][a];
        if(hay[q][a]<0)
        {
          sol[q]+=-hay[q][a];
          hay[q][a]=0;
        }
      }
    }
    
    printf("Case #%d: %d %d\n",qwer,sol[A],sol[B]);
  }

  return(0);
}
