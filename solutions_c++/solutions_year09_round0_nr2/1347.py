#include <stdio.h>

class point{
      public:
             long i,j,min;
};

long n,m,tab[150][150];
bool fix[150][150];
char ans[150][150];

char DFS(long i,long j,char ch)
{
  if(fix[i][j])
    return ans[i][j];
    
  fix[i][j]=true;
  ans[i][j] = ch;
  point next;
  next.min = 200000000;
  
  // South
  if(i+1<n)
    if(next.min >= tab[i+1][j])
    {
      next.i = i+1;
      next.j = j;
      next.min = tab[i+1][j];
    }
    
  // East
  if(j+1<m)
    if(next.min >= tab[i][j+1])
    {
      next.i = i;
      next.j = j+1;
      next.min = tab[i][j+1];
    }
    
  // West
  if(j-1>=0)
    if(next.min >= tab[i][j-1])
    {
      next.i = i;
      next.j = j-1;
      next.min = tab[i][j-1];
    }
    
  // North
  if(i-1>=0)
    if(next.min >= tab[i-1][j])
    {
      next.i = i-1;
      next.j = j;
      next.min = tab[i-1][j];
    }
  char c;
  if(next.min<tab[i][j])
  {
    c = DFS(next.i,next.j,ch);
    if(c!=0)
      ans[i][j] = c;
    return c;
  }
  else return 0;
}
main()
{
  freopen("file.in","r",stdin);
  freopen("file.out","w",stdout);
  long i,j,tc,t; char let,c;
  scanf("%d",&t);
  for(tc=1;tc<=t;tc++)
  {
    scanf("%d %d",&n,&m);
    for(i=0;i<n;i++)
      for(j=0;j<m;j++)
      {
        scanf("%d",&tab[i][j]);
        fix[i][j]=false;
        ans[i][j]=0;
      }
    
    let = 'a';    
    for(i=0;i<n;i++)
      for(j=0;j<m;j++)
        if(!fix[i][j])
        {
          c = DFS(i,j,let);
          if(c==0) let++;
        }
    printf("Case #%d:\n",tc);
    for(i=0;i<n;i++)
    {
      printf("%c",ans[i][0]);
      for(j=1;j<m;j++)
        printf(" %c",ans[i][j]);
      printf("\n");
    }
    
  }
}
