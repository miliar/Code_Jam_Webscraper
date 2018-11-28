#include <stdio.h>

int main()
{
  int I,N;
  scanf("%d",&N);
  for(I=0; I<N; ++I)
  {
    int n,pd,pg;
    scanf("%d%d%d",&n,&pd,&pg);
    bool possible=true;
    // check n & pd possibility
    if( pd!=100 )
    {
      if( n<100 ) // if n>=100, always possible(?)
      {
        bool any=false;
        for(int i=1; i<=n; ++i)
        {
          if( (i*pd) % 100 == 0 )
          {
            any = true;
            break;
          }
        }
        if( !any ) possible = false;
      }
    }

    // check pd & pg
    if( pg == 0 && pd!=0)
        possible = false;
    if( pg == 100 && pd!=100)
        possible = false;
    if( pd == 0 && pg == 100 )
        possible = false;

    printf("Case #%d: ",I+1);
    if(possible) printf("Possible\n");
     else printf("Broken\n");
  }
  return 1;
}
