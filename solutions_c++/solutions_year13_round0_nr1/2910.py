#include <cstdio>

char a[6][6];
bool flag;

inline bool work()
{
  int i,j;
  char t;
  bool f;
  for (i=1;i<=4;i++)
  {
    f=true;
    t='0';
    for (j=1;j<=4;j++)
    {
      if (a[i][j]=='T') continue;
      if (a[i][j]=='.')
      {
        f=false;
        break;
      }
      if (t=='0')
      {
        t=a[i][j];
        continue;
      }
      if (a[i][j]!=t)
      {
        f=false;
        break;
      }
    }
    if (f)
    {
      printf("%c won\n",t);
      return false;
    }
  //-------------------
    f=true;
    t='0';
    for (j=1;j<=4;j++)
    {
      if (a[j][i]=='T') continue;
      if (a[j][i]=='.')
      {
        f=false;
        break;
      }
      if (t=='0')
      {
        t=a[j][i];
        continue;
      }
      if (a[j][i]!=t)
      {
        f=false;
        break;
      }
    }
    if (f)
    {
      printf("%c won\n",t);
      return false;
    }
  }
  //==========
  f=true;
  t='0';
  for (i=1;i<=4;i++)
  {
    if (a[i][i]=='T') continue;
    if (a[i][i]=='.')
    {
      f=false;
      break;
    }
    if (t=='0')
    {
      t=a[i][i];
      continue;
    }
    if (a[i][i]!=t)
    {
      f=false;
      break;
    }
  }
  if (f)
  {
    printf("%c won\n",t);
    return false;
  }
  //------
  f=true;
  t='0';
  for (i=1;i<=4;i++)
  {
    if (a[i][4-i+1]=='T') continue;
    if (a[i][4-i+1]=='.')
    {
      f=false;
      break;
    }
    if (t=='0')
    {
      t=a[i][4-i+1];
      continue;
    }
    if (a[i][4-i+1]!=t)
    {
      f=false;
      break;
    }
  }
  if (f)
  {
    printf("%c won\n",t);
    return false;
  }
  return true;
}

int main()
{
  int T,o,i,j;
  char temp[10];
  freopen("A-large.in","r",stdin);
  freopen("T2.txt","w+",stdout);
  scanf("%d",&T);
  for (o=1;o<=T;o++)
  {
    gets(temp);
    flag=false;
    for (i=1;i<=4;i++)
    {
      for (j=1;j<=4;j++)
      {
        scanf("%c",&a[i][j]);
        if (a[i][j]=='.') flag=true;
      }
      gets(temp);
    }
    printf("Case #%d: ",o);
    if (work())
      if (flag)
        puts("Game has not completed");
      else
        puts("Draw");
  }
  return 0;
}
