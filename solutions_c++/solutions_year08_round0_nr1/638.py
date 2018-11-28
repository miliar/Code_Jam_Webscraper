#include <cstdio>
#include <algorithm>
#include <map>
#include <string>


using namespace std;

int n, s, q;
int seq[2000];
int tab[2000][2000];

int main()
{
  scanf(" %d ", &n);
  for(int test=1; test<=n; ++test)
    {
      map<string, int> se;
      scanf(" %d ", &s);
      for(int i=0; i<s; ++i)
	{
	  char buf[200];
	  fgets(buf, 200, stdin);
	  se[string(buf)] = i;
	}
      scanf(" %d ", &q);
      for(int i=0; i<q; ++i)
	{
	  char buf[200];
	  fgets(buf, 200, stdin);
	  seq[i] = se[string(buf)];
	}
      for(int i=0; i<s; ++i)
	{
	  tab[0][i] = 0;
	  if(seq[0]==i)
	    tab[0][i] = 0x3f3f3f3f;
	}
      for(int i=1; i<q; ++i)
	for(int j=0; j<s; ++j)
	  {
	    int vmin = 0x3f3f3f3f;
	    for(int k=0; k<s; ++k)
	      if(tab[i-1][k] + (j!=k) < vmin)
		{
		  vmin = tab[i-1][k] + (j!=k);
		}
	    tab[i][j] = vmin;
	    if(j == seq[i])
	      tab[i][j] = 0x3f3f3f3f;
	  }
      int vmin = 0x3f3f3f3f;
      for(int i=0; i<s; ++i)
	vmin = min(vmin, tab[q-1][i]);
      printf("Case #%d: %d\n", test, vmin);
    }
  return 0;
}
