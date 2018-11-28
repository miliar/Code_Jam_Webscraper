#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;

int n, k;
char tab[400][400];
char buf[160000];

char needle[200];
bool find(int c)
{
  bool found = false;
  memset(needle, c, sizeof(needle));
  needle[k] = 0;

  {
    int p=0;
    for (int i=0; i<n; ++i)
      {
	for (int j=0; j<n; ++j)
	  buf[p++] = tab[i][j];
	buf[p++] = '.';
      }
    buf[p++] = 0;
    //printf("%s\n", buf);
    if (strstr(buf, needle) != 0) found = true;
  }
  
  {
    int p=0;
    for (int i=0; i<n; ++i)
      {
	for (int j=0; j<n; ++j)
	  buf[p++] = tab[j][i];
	buf[p++] = '.';
      }
    buf[p++] = 0;
    //printf("%s\n", buf);
    if (strstr(buf, needle) != 0) found = true;
  }

  {
    int p=0;
    for (int i=0; i<=2*n; ++i)
      {
	for (int j=0; j<n; ++j)		       
	  if (i-j >=0 && i-j < n)
	    buf[p++] = tab[i-j][j];
	buf[p++] = '.';
      }
    buf[p++] = 0;
    //printf("%s\n", buf);
    if (strstr(buf, needle) != 0) found = true;
  }

  {
    int p=0;
    for (int i=-n; i<=n; ++i)
      {
	for (int j=0; j<n; ++j)		       
	  if (i+j >= 0 && i+j<n)
	    buf[p++] = tab[i+j][j];
	buf[p++] = '.';
      }
    buf[p++] = 0;
    //printf("%s\n", buf);
    if (strstr(buf, needle) != 0) found = true;
  }

  return found;
}

int main()
{
  int ntests;
  scanf(" %d", &ntests);
  for (int test=0; test<ntests; ++test)
    {
      scanf(" %d %d", &n, &k);
      memset(tab, 0, sizeof(tab));
      for (int i=0; i<n; ++i)
	for (int j=0; j<n; ++j)
	  scanf(" %c", &tab[i][j]);
      for (int i=0; i<n; ++i)
	for (int j=n-1, k=n-1; j>=0; --j)
	  if (tab[i][j] != '.')
	    swap(tab[i][j], tab[i][k--]);

      // for (int i=0; i<n; ++i)
      // 	{
      // 	  for (int j=0; j<n; ++j)
      // 	    printf("%c", tab[i][j]);
      // 	  printf("\n");
      // 	}

      bool fb = find('B');
      bool fr = find('R');
      printf("Case #%d: ", test+1);
      if (fb && fr) printf("Both\n");
      else if (fb) printf("Blue\n");
      else if (fr) printf("Red\n");
      else printf("Neither\n");
    }
  return 0;
}

