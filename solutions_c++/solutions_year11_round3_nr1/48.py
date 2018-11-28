#include"stdio.h"
int main()
{
  int T;
  scanf("%d\n",&T);
  for(int t=1;t<=T;t++)
  {
    int R,C;
    scanf("%d%d\n",&R,&C);
    char inp[R][C+10];
    for(int x=0;x<R;x++)
    {
      gets(inp[x]);
    }
    bool cont=true;
    for(int x=0;x<R&&cont;x++)
    {
      for(int y=0;y<C&&cont;y++)
      {
	if(inp[x][y]=='#')
	{
	  if(inp[x][y+1]!='#' || x+1>=R || inp[x+1][y]!='#' || inp[x+1][y+1]!='#')
	    cont=false;
	  else
	  {
	    inp[x][y]=inp[x+1][y+1]='/';
	    inp[x+1][y]=inp[x][y+1]='\\';
	  }
	}
      }
    }
    printf("Case #%d:\n",t);
    if(cont)
      for(int x=0;x<R;x++)
	printf("%s\n",inp[x]);
    else
      printf("Impossible\n");
  }
}