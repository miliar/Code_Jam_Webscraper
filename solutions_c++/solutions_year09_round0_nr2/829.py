#include <cstdio>

int m[100][100];
char label[100][100];

int flowsto(int i, int j, int H, int W)
{
  //  printf("$$ %d %d\n",i,j);
  if (i<0 || j<0 || i>=H || j>=W)
      return 100000;


  int min=100000;
  if (i>0)
    if (min>m[i-1][j])
      min=m[i-1][j];

  if (j>0)
    if (min>m[i][j-1])
      min=m[i][j-1];

  if (i<H-1)
    if (min>m[i+1][j])
      min=m[i+1][j];

  if (j<W-1)
    if (min>m[i][j+1])
      min=m[i][j+1];

  if (min>=m[i][j])
    return 100000;

  if (i>0)
    if (min==m[i-1][j])
      return (i-1)*W+j;

  if (j>0)
    if (min==m[i][j-1])
      return i*W+j-1;

  if (j<W-1)
    if (min==m[i][j+1])
      return i*W+j+1;

  if (i<H-1)
    if (min==m[i+1][j])
      return (i+1)*W+j;
}

void labelbasin(int i, int j, int H, int W, char l)
{
  //  printf("$ %d %d\n",i,j);
  if (label[i][j]==0)
    {
      label[i][j]=l;
      int f=flowsto(i,j,H,W);
      int a=f/W;
      int b=f%W;
      if (f<100000)
	labelbasin(a,b,H,W,l);

      f=flowsto(i-1,j,H,W);
      a=f/W;
      b=f%W;
      if (a==i && b==j)
	labelbasin(i-1,j,H,W,l);

      f=flowsto(i+1,j,H,W);
      a=f/W;
      b=f%W;
      if (a==i && b==j)
	labelbasin(i+1,j,H,W,l);

      f=flowsto(i,j-1,H,W);
      a=f/W;
      b=f%W;
      if (a==i && b==j)
	labelbasin(i,j-1,H,W,l);

      f=flowsto(i,j+1,H,W);
      a=f/W;
      b=f%W;
      if (a==i && b==j)
	labelbasin(i,j+1,H,W,l);

    }
}

int main()
{
  int T,H,W;
  scanf("%d\n",&T);

  for (int t=0; t<T; t++)
    {
      scanf("%d %d\n",&H,&W);
      for (int i=0; i<H; i++)
	{
	  for (int j=0; j<W; j++)
	    {
	      scanf(" %d ",&(m[i][j]));
	      label[i][j]=0;
	    }
	}

      char l='a';
      for (int i=0; i<H; i++)
	{
	  for (int j=0; j<W; j++)
	    {
	      //	      printf("labing %d %d\n",i,j);
	      if (label[i][j]==0)
		{
		  labelbasin(i,j,H,W,l);
		  l++;
		}
	    }
	}

      printf("Case #%d:\n",t+1);
      for (int i=0; i<H; i++)
	{
	  for (int j=0; j<W; j++)
	    {
	      printf("%c",label[i][j]);
	      if (j<W-1)
		printf(" ");
	    }
	  printf("\n");
	}
    }

  return 0;
}
