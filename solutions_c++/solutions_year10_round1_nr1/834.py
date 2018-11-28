#include <cstdio>
#include <algorithm>
#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <set>
#include <map>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

int T;

char s[110][110];



int n, k, r;

int dx[4][110];
int dy[4][110];

void transform()
{
	for (int i = 0; i < n; ++i)
	{
	  int p = r;
	  int j = r;
	  while (j >= 0)
	  {
	    while (j >= 0 && s[i][j] == '.') --j;
	    if (j >= 0)
	    {
	      s[i][p] = s[i][j];
		  if (p > j)
			  s[i][j] = '.';
	      p = p-1;
		  --j;
	    }
	  }
	}
}

bool check(int i1, int j1, char c)
{
  bool b = false;
  for (int m = 0; m < 4; ++m)
  {
    bool b1 = true;
    for (int i = 0; i < k; ++i)
    {
      int x = j1 + dx[m][i];
      int y = i1 + dy[m][i];
      if (x < 0 || x >= n || y < 0 || y >= n || s[y][x] != c)
      {
         b1 = false;
         break;
      }
      
    }
	if (b1)
        return true;
  }
  return false;
}

int main()
{
  for (int i = 0; i < 100; ++i)
  {
  	dx[0][i] = i;
  	dy[0][i] = 0;

  	dx[1][i] = 0;
  	dy[1][i] = i;

  	dx[2][i] = i;
  	dy[2][i] = i;

  	dx[3][i] = -i;
  	dy[3][i] = i;
  }
  scanf("%d", &T);
  for (int t = 0; t < T; ++t)
  {
    scanf("%d %d", &n, &k);
    char c[50];
			gets(c);
    for (int i = 0; i < n; ++i)
      gets(s[i]);
    r = 0;
    for (int i = 0; i < n; ++i)
    {
      for (int j = n-1; j >= 0; --j)
        if (s[i][j] != '.')
        {
          r = max(r, j);
          break;
        }
    } 
    transform();
    bool b1 = false;
    bool b2 = false;
    for (int i = 0; i < n; ++i)
    {
      for (int j = 0; j < n; ++j)
      {
        if (check(i, j, 'R'))
          b1 = true;
        if (check(i, j, 'B'))
          b2 = true;
      }
    }
  	printf("Case #%d: ", t+1);
  	if (!b1 && !b2)
  	  printf("Neither\n");
  	if (b1 && b2)
  	  printf("Both\n");
  	if (b1 && !b2)
  	 printf("Red\n");
  	if (!b1 && b2)
  	  printf("Blue\n");
  	/*for (int i = 0; i < n; ++i)
  	  printf("%s\n", s[i]);
  	  */
  }
	return 0;
}