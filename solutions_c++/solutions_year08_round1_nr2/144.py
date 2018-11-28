#include <stdio.h>

int ca, n, m, c[2000][2002][2], r[2000];

int main()
{
  scanf(" %d ", &ca);
  for(int cs=1; cs<=ca; cs++)
    {
      scanf(" %d %d ", &n, &m);
      for(int i=0; i<m; i++)
	{
	  scanf(" %d ", &c[i][0][0]);
	  for(int j=0; j<n; j++) r[j]=0;
	  for(int j=1; j<=c[i][0][0]; j++)
	    {
	      scanf(" %d %d ", &c[i][j][0], &c[i][j][1]);
	      c[i][j][0]--;
	    }
	}
      printf("Case #%d:", cs);

      int fix=0;
      while(!fix)
	{
	  fix=1;
	  for(int i=0; i<m; i++)
	    {
	      int ok=0;
	      int malt=-1;
	      for(int j=1; j<=c[i][0][0]; j++)
		{
		  if (c[i][j][1]) malt=c[i][j][0];
		  if (r[c[i][j][0]]==c[i][j][1]) ok=1;
		}
	      if (!ok)
		{
		  fix=0;
		  if ((malt>=0) && (!r[malt]))
		    r[malt]=1;
		  else
		    {
		      printf(" IMPOSSIBLE");
		      goto weiter;
		    }
		}
	    }
	}

      for(int i=0; i<n; i++)
	printf(" %d", r[i]);
    weiter:;
      printf("\n");
    }
  return 0;
}
