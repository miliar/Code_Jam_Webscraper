#include <map>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cmath>
#include <ctime>
#include <cstdio>
#include <cassert>
#include <cstdlib>
#include <cstring>

using namespace std;

typedef long long LL;

#define fore(i, c) for (typeof ((c).begin ()) i = (c).begin (); i != (c).end (); i++)
#define sz(c) ((int) (c).size ())
#define pb push_back
#define mp make_pair
#define fi first
#define se second

int K;
char s[1000][1000];
int l[1000];

int sym (int x, int c)
{
  if (x < c)
    return c + c - x;
  else if (x > c)
    return c - x - c;
  else
    return c;
}

bool test (int i, int j, char c)
{
  if (i < 0 || i >= 2 * K - 1 || j < 0 || j >= l[i])
    return true;
  return s[i][j] == ' ' || s[i][j] == c;
}

bool check (int ci, int cj)
{
  for (int i = 0; i < 2 * K - 1; i++)
  {
    for (int j = 0; s[i][j] != 0; j++)
      if (isdigit (s[i][j]))
      {
        int si = sym (i, ci);
        if (!test (si, j, s[i][j]))
          return false;
        int sj = sym (j, cj);
        if (!test (i, sj, s[i][j]))
          return false;
      }
  }
  return true;
}

char ss[1000];

int main ()
{
	int cases;
	scanf ("%d\n", &cases);
	for (int test = 1; test <= cases; test++)
	{
		printf ("Case #%d: ", test);
    gets (ss);
    sscanf(ss, "%d", &K);
    
    for (int i = 0; i < 2 * K - 1; i++)
    {
      gets (s[i]);
      while (strlen (s[i]) < 2 * K - 1)
        strcat(s[i], " ");
      l[i] = strlen (s[i]);
    }
        
    int t = 1000000000;
    for (int i = 0; i < 2 * K - 1; i++)
    {
      int j = 0;
      while (s[i][j] != 0)
      {
        if (check (i, j))
        {
          t = min (t, abs (i - K + 1) + abs (j - K + 1));
        }
        j++;
      }
    }
    
    assert (t != 1000000000);
    
    int res = 0;
    for (int i = K; i < K + t; i++)
      res += 2 * i + 1;
    
    printf ("%d\n", res);
	}
	return 0;
}

