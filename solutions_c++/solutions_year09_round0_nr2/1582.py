#include <stdio.h>
#include <math.h>
int hts[200][200];
int basin[200][200];
int findit(int x,int y)
{
  if(basin[x][y]!=-1)
    return basin[x][y];
  
  int minn=100000;
  int xopt,yopt;
  if(hts[x-1][y]<minn)
    {
      minn=hts[x-1][y];
      xopt=x-1;
      yopt=y;
    }
  if(hts[x][y-1]<minn)
    {
      minn=hts[x][y-1];
      xopt=x;
      yopt=y-1;
    }
  if(hts[x][y+1]<minn)
    {
    minn=hts[x][y+1];
    xopt=x;
    yopt=y+1;
    }
  if(hts[x+1][y]<minn)
    {
    minn=hts[x+1][y];
    xopt=x+1;
    yopt=y;
    }


  if(minn<hts[x][y])
    {
      return findit(xopt,yopt);
    }
  
  
}

int main()
{
  int tc;
  scanf("%d",&tc);
 
  for(int t=1;t<=tc;t++)
    {
      int m,n;
      for(int i=0;i<=150;i++)
	for(int j=0;j<=150;j++)
	  hts[i][j]=100000;
      scanf("%d %d",&m,&n);
      for(int i=1;i<=m;i++)
	for(int j=1;j<=n;j++)
	  {
	    scanf("%d",&hts[i][j]);
	  }

    
      for(int i=1;i<=m;i++)
	for(int j=1;j<=n;j++)
	  basin[i][j]=-1;
      int numsinks=0;
      for(int i=1;i<=m;i++)
	for(int j=1;j<=n;j++)
	  {
	    if(hts[i-1][j]>=hts[i][j] && hts[i+1][j]>=hts[i][j] && hts[i][j-1]>=hts[i][j] && hts[i][j+1]>=hts[i][j])
	      {
		basin[i][j]=numsinks;
		numsinks++;
		//printf("dsfsd\n");
	      }
	  }

      for(int i=1;i<=m;i++)
	for(int j=1;j<=n;j++)
	  {
	    basin[i][j]=findit(i,j);
	  }

      printf("Case #%d:\n",t);
      bool occ[40];
      int map[40];
      int numbasins=0;
      for(int i=0;i<30;i++)
	occ[i]=0;
      for(int i=1;i<=m;i++)
	for(int j=1;j<=n;j++)
	  {
	    if(!occ[basin[i][j]])
	      {
		map[basin[i][j]]=numbasins;
		numbasins++;
		occ[basin[i][j]]=1;
	      }
	      
	  }
      for(int i=1;i<=m;i++)
	for(int j=1;j<=n;j++)
	  basin[i][j]=map[basin[i][j]];



      for(int i=1;i<=m;i++)
	{
	  for(int j=1;j<=n;j++)
	    printf("%c ",'a'+basin[i][j]);
	  printf("\n");
	}

      
    }
}
