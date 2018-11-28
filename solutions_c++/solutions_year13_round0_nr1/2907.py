#include <stdio.h>
#include <stdlib.h>


char maze[10][10];

int dx[]={0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,0,1,2,3,0,1,2,3};
int dy[]={0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,3,2,1,0};
void solve(int count)
{
  //row
  for(int i=0;i<40;i+=4)
    {
      char chess=maze[dx[i]][dy[i]];
      if(chess=='.') continue;
      int j;
      for(j=1;j<4;j++)
	{
	  if(maze[dx[i+j]][dy[i+j]]=='.')
	    break;
	  else if(chess=='T')
	    chess=maze[dx[i+j]][dy[i+j]];
	  else if(maze[dx[i+j]][dy[i+j]]=='T')
	    continue;
	  else if(chess!=maze[dx[i+j]][dy[i+j]])
	    break;
	}
      if(j==4&&chess!='T')
	{
	  printf("Case #%d: %c won\n",count,chess);
	  return;
	}
    }
  bool fdraw = true;
  for(int i=0;i<4;i++)
    for(int j=0;j<4;j++)
      if(maze[i][j]=='.')
	fdraw=false;
  if(fdraw)
    printf("Case #%d: Draw\n",count);
  else
    printf("Case #%d: Game has not completed\n",count);
}
int main()
{
  int n;
  int count = 1;
  char str[20];
  scanf("%d",&n);
  while(count<=n)
    {
      gets(str);
      for(int i=0;i<4;i++)
	{
	  gets(maze[i]);
	}
      solve(count++);
    }
  return 0;
}
