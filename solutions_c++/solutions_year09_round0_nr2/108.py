#include<iostream>
#include<cstdio>
using namespace std;
#define val(x,y) (x>=1&&x<=m&&y>=1&&y<=n)
int m,n,ct;
int a[109][109];
int bas[109][109];

int drain(int x,int y)
{
  int md,mx,my;
  md=a[x][y];
  mx=x;
  my=y;
  if(bas[x][y]!=0)
    return bas[x][y];
  if(val(x-1,y))
  {
    if(a[x-1][y]<md)
    {
      md=a[x-1][y];
      mx=x-1;
      my=y;
    }
  }
  
  if(val(x,y-1))
  {
    if(a[x][y-1]<md)
    {
      md=a[x][y-1];
      mx=x;
      my=y-1;
    }
  }
  
  if(val(x,y+1))
  {
    if(a[x][y+1]<md)
    {
      md=a[x][y+1];
      mx=x;
      my=y+1;
    }
  }
    
  if(val(x+1,y))
  {
    if(a[x+1][y]<md)
    {
      md=a[x+1][y];
      mx=x+1;
      my=y;
    }
  }
  
  if(mx==x && my==y)
  {
    //i.e sink
    ct++;
    bas[x][y]=ct;
    return ct;
  }
  else
  {
    bas[x][y] = drain(mx,my);
    return bas[x][y];
  }
}
int main()
{

  int i,j,t,tc;
  char charmap[30];
  char cct;
  scanf("%d",&t);
  for(tc=1;tc<=t;tc++)
  {
    printf("Case #%d:\n",tc);
    scanf("%d",&m);
    scanf("%d",&n);
    ct=0;
    for(i=1;i<=m;i++)
    {
      for(j=1;j<=n;j++)
      {
	scanf("%d",&a[i][j]);
	bas[i][j]=0;
      }
    }
    for(i=1;i<=m;i++)
    {
      for(j=1;j<=n;j++)
      {
	if(bas[i][j]==0)
	{
	  drain(i,j);
	}
      }
    }
    for(i=1;i<30;i++)
      charmap[i]='\0';
    cct='a';
    for(i=1;i<=m;i++)
    {
      for(j=1;j<=n;j++)
      {
	if(charmap[bas[i][j]]=='\0')
	{
	  charmap[bas[i][j]]=cct;
	  cct++;
	}
      }
    }
    for(i=1;i<=m;i++)
    {
      for(j=1;j<=n;j++)
      {
	printf("%c ",charmap[bas[i][j]]);
      }
      printf("\n");
    }
    
  }
  
  
  return 0;
}