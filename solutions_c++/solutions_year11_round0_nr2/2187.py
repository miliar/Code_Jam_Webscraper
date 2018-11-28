//---------------------------------------------------------------------------

#include <stdio.h>
#include <mem.h>
#pragma hdrstop

//---------------------------------------------------------------------------

#pragma argsused


int main(int argc, char* argv[])
{
  int T;
  scanf("%d\n",&T);
  for (int t=1;t<=T;t++)
  {
    char replace[256][256];
    char del[256][256];
    memset(replace,0,sizeof(replace));
    memset(del,0,sizeof(del));
    int C,D,N;
    char trash;
    scanf("%d%c",&C,&trash);
    for (int c=0;c<C;c++)
    {
      char cA,cB,cN;
      scanf("%c%c%c%c",&cA,&cB,&cN,&trash);
      replace[cA][cB]=replace[cB][cA]=cN;
    }
    scanf("%d%c",&D,&trash);
    for (int d=0;d<D;d++)
    {
      char cA,cB;
      scanf("%c%c%c",&cA,&cB,&trash);
      del[cA][cB]=del[cB][cA]=1;
    }
    scanf("%d%c",&N,&trash);
    int pos=0;
    char current[1000];
    for (int n=0;n<N;n++)
    {
      scanf("%c",&current[pos]);
      //replace
      while (pos>0)
      {
        if (replace[current[pos]][current[pos-1]]!='\0')
        {
          current[pos-1]=replace[current[pos]][current[pos-1]];
          pos--;
        }
        else
        {
          break;
        }
      }
      //delete
      bool empty=false;
      for (int p=0;p<pos;p++)
      {
        if(del[current[pos]][current[p]]!='\0')
        {
          empty=true;
          break;
        }
      }
      if (empty)
      {
        pos=0;
      }
      else
      {
        pos++;
      }
    }
    printf("Case #%d: [",t);
    if (pos>0)
    {
      printf("%c",current[0]);
    }
    for (int p=1;p<pos;p++)
    {
      printf(", %c",current[p]);
    }
    printf("]\n");
  }
  return 0;
}
//---------------------------------------------------------------------------

