#include<stdio.h>

int main()
{
  int n,N,m,q,w;

  for(n=1,scanf(" %d",&N);n<=N;n++)
  {
    scanf(" %d %d",&m,&q);
    q=q%(1<<m);
    w=(1<<m)-1;
    printf("Case #%d: %s\n",n,(q==w)?"ON":"OFF");
  }

  return(0);
}

