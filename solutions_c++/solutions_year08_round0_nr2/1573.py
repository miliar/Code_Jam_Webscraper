#include <stdio.h>
#include <stdlib.h>

int n, a, b, t[400], e[400], s[400], na, nb, aa, ab, tt;

int cmp(const void *a, const void *b)
{
  if (t[*((int*)a)]<t[*((int*)b)]) return -1;
  if (t[*((int*)a)]>t[*((int*)b)]) return 1;
  if (e[*((int*)a)]==1) return -1;
  if (e[*((int*)a)]==3) return -1;
  if (e[*((int*)b)]==1) return 1;
  if (e[*((int*)b)]==3) return 1;
  return 0;
}

int main()
{
  scanf(" %d ", &n);
  for(int cs=1; cs<=n; cs++)
    {
      a=b=na=nb=0;
      scanf(" %d %d %d ", &tt, &aa, &ab);
      for(int i=0; i<aa; i++)
	{
	  int d1, d2, d3, d4;
	  scanf(" %d:%d %d:%d ", &d1, &d2, &d3, &d4);
	  t[i*2]=d1*60+d2;
	  e[i*2]=0;
	  s[i*2]=i*2;
	  t[i*2+1]=d3*60+d4+tt;
	  e[i*2+1]=1;
	  s[i*2+1]=i*2+1;
	}
      for(int i=aa; i<aa+ab; i++)
	{
	  int d1, d2, d3, d4;
	  scanf(" %d:%d %d:%d ", &d1, &d2, &d3, &d4);
	  t[i*2]=d1*60+d2;
	  e[i*2]=2;
	  s[i*2]=i*2;
	  t[i*2+1]=d3*60+d4+tt;
	  e[i*2+1]=3;
	  s[i*2+1]=i*2+1;
	}
      qsort(s, (aa+ab)*2, sizeof(int), cmp);
      for(int i=0; i<2*(aa+ab); i++)
	{
	  switch(e[s[i]])
	    {
	    case 0:
	      if (--na<0)
		{
		  na=0;
		  a++;
		}
	      break;
	    case 2:
	      if (--nb<0)
		{
		  nb=0;
		  b++;
		}
	      break;
	    case 1:
	      nb++;
	      break;
	    case 3:
	      na++;
	      break;
	    }
	  // printf("%d %d %d %d %d\n", s[i], a, b, na, nb);
	}
      printf("Case #%d: %d %d\n", cs, a, b);
    }
  return 0;
}
