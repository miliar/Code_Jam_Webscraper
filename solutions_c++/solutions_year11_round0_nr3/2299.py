//---------------------------------------------------------------------------

#include <stdio.h>
#pragma hdrstop

//---------------------------------------------------------------------------

#pragma argsused

int main(int argc, char* argv[])
{
  int T;
  scanf("%d\n",&T);
  for (int t=1;t<=T;t++)
  {
    int N;
    int parity=0;
    int sum=0;
    int lower=10000000;
    scanf("%d",&N);
    for (int n=0;n<N;n++)
    {
      int C;
      scanf("%d",&C);
      parity^=C;
      if (C<lower)
      {
        lower=C;
      }
      sum+=C;
    }
    if (parity!=0)
    {
      printf("Case #%d: NO\n",t);
    }
    else
    {
      printf("Case #%d: %d\n",t,sum-lower);
    }
  }
  return 0;
}
//---------------------------------------------------------------------------

