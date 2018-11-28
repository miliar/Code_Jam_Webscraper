#include <stdio.h>
#include <string.h>

int n, res, as, uu, aq;
char s[101], se[100][101], u[100];

int main()
{
  gets(s);
  sscanf(s, " %d ", &n);
  for(int cs=1; cs<=n; cs++)
    {
      gets(s);
      sscanf(s, " %d ", &as);
      for(int i=0; i<as; i++)
	{
	  gets(se[i]);
	  u[i]=0;
	}
      res=0; uu=as;
      gets(s);
      sscanf(s, " %d ", &aq);
      while(aq--)
	{
	  gets(s);
	  int pos;
	  for(pos=0; pos<as; pos++)
	    if (!strcmp(s, se[pos]))
	      break;
	  if (!u[pos])
	    {
	      u[pos]=1;
	      if (!(--uu))
		{
		  for(int i=0; i<as; i++) u[i]=0;
		  u[pos]=1;
		  uu=as-1;
		  res++;
		}
	    }
	}
      printf("Case #%d: %d\n", cs, res);
    }
  return 0;
}
