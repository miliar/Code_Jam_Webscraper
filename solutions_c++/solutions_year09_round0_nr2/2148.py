#include <stdio.h>
#include <stdlib.h>

char cur='a';
int h,w;
int map[102][102];
char charmap[102][102];
int nTestCase;

char process(int y,int x)
{
  int pivot = map[y][x];
  int min = pivot-1;
  char c;
  
  if (map[y-1][x]<=min)
  {
    min = map[y-1][x];
  }
  if (map[y+1][x]<=min)
  {
    min = map[y+1][x];
  }
  if (map[y][x-1]<=min)
  {
    min = map[y][x-1];
  }
  if (map[y][x+1]<=min)
  {
    min = map[y][x+1];
  }
  
  if (map[y-1][x]==min)
  {
    if (charmap[y-1][x]!=' ')
	{
	  charmap[y][x]=charmap[y-1][x];
	  return charmap[y-1][x];
	}
	else
	{
	  c = process (y-1,x);
	  charmap[y-1][x]=c;
	  return c;
	} 
  }
  else if (map[y][x-1]==min)
  {
    if (charmap[y][x-1]!=' ')
	{
	
	  charmap[y][x]=charmap[y][x-1];
	  return charmap[y][x-1];
	}
	else
	{
	  c = process(y,x-1);
	  charmap[y][x-1]=c;
	  return c;
	}
  }
  else if (map[y][x+1]==min)
  {
    if (charmap[y][x+1]!=' ')
	{
	  charmap[y][x]=charmap[y][x+1];
	  return charmap[y][x+1];
	}
	else
	{
	  c = process(y,x+1);
	  charmap[y][x+1]=c;
	  return c;
	}
  }
  else if (map[y+1][x]==min)
  {
    if (charmap[y+1][x]!=' ')
	{
	
	  charmap[y][x]=charmap[y+1][x];
	  return charmap[y+1][x];
	}
	else
	{
	  c = process(y+1,x);
	  charmap[y+1][x]=c;
	  return c;
	}
  }
  else
  {
    cur++;
	charmap[y][x]=cur;
    return cur;
  }
}

int main()
{
int i,ii,pp,k,m;

scanf("%d",&nTestCase);
for (pp=0;pp<nTestCase;pp++)
{
  printf("Case #%d:\n",pp+1);
  cur = 'a';cur--;
  scanf("%d%d",&h,&w);
  for (i=0;i<h;i++)
  {
    for (ii=0;ii<w;ii++)
	{
	  scanf("%d",&k);
	  map[i+1][ii+1]=k;
	  charmap[i+1][ii+1]=' ';
	}
  }
  for (i=0;i<=h+1;i++)
  {
    map[i][0]=10001;
	map[i][w+1]=10001;
  }
  for (i=0;i<=w+1;i++)
  {
	map[0][i]=10001;
	map[h+1][i]=10001;
  }

  for (i=0;i<h;i++)
  {
    for (ii=0;ii<w;ii++)
	{
	  if (charmap[i+1][ii+1]==' ')
      {
	    charmap[i+1][ii+1]=process(i+1,ii+1);
	  }
	}
  }
  for (i=1;i<=h;i++)
  {
    for (ii=1;ii<w;ii++)
	{
	  printf("%c ",charmap[i][ii]);
	}
	printf("%c\n",charmap[i][w]);
  }
  /*
  for (i=1;i<=h;i++)
  {
    for (ii=1;ii<=w;ii++)
	{
	  printf("%d",map[i][ii]);
	}
	printf("\n");
  }
  */
}

return 0;
}