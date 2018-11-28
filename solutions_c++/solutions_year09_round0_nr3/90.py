#include <cstdio>
#include <cstring>

int tab[20][550];
char s1[] = " welcome to code jam";
char s2[550];
int l1 = strlen(s1) - 1;

int main()
{
  int ntests;
  scanf(" %d ", &ntests);
  for(int test = 1; test <= ntests; ++test)
    {
      fgets(&s2[1], 549, stdin);
      int l2 = strlen(&s2[1]) - 1;
      memset(tab, 0, sizeof(tab));
      for(int i=0; i<550; ++i)
	tab[0][i] = 1;
      for(int i=1; i<=l1; ++i)
	for(int j=1; j<=l2; ++j)
	  {
	    for(int k=1; k<=j; ++k)
	      if(s1[i] == s2[k])
		{
		  tab[i][j] += tab[i-1][k-1];
		  tab[i][j] %= 10000;
		}
	  }
      printf("Case #%d: %04d\n", test, tab[l1][l2]);
    }
}
