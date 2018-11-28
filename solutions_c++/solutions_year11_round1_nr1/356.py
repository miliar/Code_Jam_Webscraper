//---------------------------------------------------------------------------

#include <stdio.h>
#pragma hdrstop

//---------------------------------------------------------------------------
int abs(int a)
{
  if (a<0)
    return -a;
  return a;
}

__int64 GCD(__int64 A,__int64 B)
{
  if (A==0)
  {
    return B;
  }
  return GCD(B%A,A);
}

__int64 nextint64(void)
{
  char aux[1024];
  scanf("%s",aux);
  __int64 res=0;
  int pos=0;
  while (aux[pos]!='\0')
  {
    res*=10LL;
    res+=__int64(aux[pos]-'0');
    pos++;
  }
  return res;
}

#pragma argsused
int main(int argc, char* argv[])
{
  int T;
  scanf("%d\n",&T);
  for (int t=1;t<=T;t++)
  {
    __int64 Pd,Pg,N,minD;
    N=nextint64();
    Pd=nextint64();
    Pg=nextint64();
    __int64 aux=GCD(Pd,100L);
    minD=100L/aux;
    if (Pd==0L)
    {
      minD=1;
    }
    if (minD>N)
    {
      printf("Case #%d: Broken\n",t);
      continue;
    }
    if (Pg==100LL)
    {
      //allways won
      if (Pd==100L)
      {
        //all games won today too
        printf("Case #%d: Possible\n",t);
        continue;
      }
      //can not win always and lose today
      printf("Case #%d: Broken\n",t);
      continue;
    }
    if (Pg==0L)
    {
      if (Pd==0L)
      {
        //all games lost
        printf("Case #%d: Possible\n",t);
        continue;
      }
      //can not lose always and win today
      printf("Case #%d: Broken\n",t);
      continue;
    }
    //general case
    printf("Case #%d: Possible\n",t);
  }
  return 0;
}
//---------------------------------------------------------------------------

