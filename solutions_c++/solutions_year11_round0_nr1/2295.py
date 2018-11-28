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

#pragma argsused
int main(int argc, char* argv[])
{
  int T;
  scanf("%d\n",&T);
  for (int t=1;t<=T;t++)
  {
    int last=0;
    int robpos[2];
    int robt[2];
    robpos[0]=robpos[1]=1;
    robt[0]=robt[1]=0;
    int pushes;
    scanf("%d ",&pushes);
    for (int p=0;p<pushes;p++)
    {
      char color,trash;
      int pos,id;
      scanf("%c %d%c",&color,&pos,&trash);
      if (color=='O')
      {
        id=0;
      }
      else
      {
        id=1;
      }
      //move
      int newtime=robt[id]+abs(robpos[id]-pos);
      if (newtime<last)
      {
        newtime=last;
      }
      //push
      newtime++;
      //update
      last=newtime;
      robt[id]=last;
      robpos[id]=pos;
    }
    printf("Case #%d: %d\n",t,last);
  }
  return 0;
}
//---------------------------------------------------------------------------
 