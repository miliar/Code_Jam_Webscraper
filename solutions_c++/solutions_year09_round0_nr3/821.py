#include <cstdio>

int dt[600][30];

int main()
{
  int N;
  scanf("%d\n",&N);

  char line[600];
  char c;
  char text[30]="welcome to code jam"; //19


  for (int i=0; i<N; i++)
    {
      int l=0;
      while (true)
	{
	  int eof=scanf("%c",&c);
	  if (c=='\n' || eof==EOF)
	    {
	      for (int j=0; j<19; j++)
		dt[0][j]=0;

	      for (int j=0; j<l; j++)
		{
		  dt[j+1][0]=(dt[j][0]+(line[j]=='w'))%10000;
		  for (int k=1; k<19; k++)
		    {
		      dt[j+1][k]=dt[j][k];
		      if (line[j]==text[k])
			dt[j+1][k]=(dt[j+1][k]+dt[j][k-1])%10000;
		    }
		}

	      printf("Case #%d: %04d\n",i+1,dt[l][18]);
	      break;
	    }
	  else
	    {
	      line[l]=c;
	      l++;
	    }
	}
    }

  return 0;
}
