#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <cassert>
using namespace std;
#define p(x) cout<<#x<<":"<<x<<"\n"
#define lim 4

int cs,c,i,j;
char A[lim][lim],B[lim][lim];

bool f(char c)
{
  int i,j,s=0;

  for(i=0;i<lim;i++)
    for(j=0;j<lim;j++)
      if(A[i][j]=='T')
      {
        A[i][j]=c;
        s++;
      }
  assert(s<=1);
  for(i=0;i<lim;i++)
  {
    for(j=0;j<lim && A[i][j]==c;j++);
    if(j==lim)
      return 1;
  }
  for(i=0;i<lim;i++)
  {
    for(j=0;j<lim && A[j][i]==c;j++);
    if(j==lim)
      return 1;
  }
  for(i=0;i<lim && A[i][i]==c;i++);
  if(i==lim)
    return 1;
  for(i=0;i<lim && A[3-i][i]==c;i++);
  if(i==lim)
    return 1;
  return 0;
}
int main()
{
  scanf("%d",&cs);
  for(c=1;c<=cs;c++)
  {
    for(i=0;i<lim;i++)
      scanf("%s",A[i]);
    printf("Case #%d: ",c);
    memcpy(B,A,sizeof A);
    if(f('X'))
    {
      assert(!f('O'));
      printf("X won\n");
    }
    else 
    {
      memcpy(A,B,sizeof A);
      if(f('O'))
        printf("O won\n");
      else
      {
        for(i=0;i<lim;i++)
        {
          for(j=0;j<lim;j++)
            if(A[i][j]=='.')
              break;
          if(j<lim)
            break;
        }
        if(i<lim)
          printf("Game has not completed\n");
        else
          printf("Draw\n");
      }
    }
  }
  return 0;
}
