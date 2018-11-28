
#include <set>
#include <map>
#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

using namespace std;

#define MAX_I 1000000
static int miss[1024];
static int m[1024];
static int pr[10][1024];

static int po(int p) {
  return 1<< p;
}

static int search(int p, int pos)
{
  if (p <= 1) {
    if (miss[2 * pos] <= m[2 * pos] && miss[2 * pos + 1] <= m[2 * pos + 1])
      return 0;
    else if (miss[2 * pos] <= m[2 * pos] + 1 && miss[2 * pos + 1] <= m[2 * pos + 1] + 1)
      return 1;
    return MAX_I;
  } 

  for (int k = pos * po(p); k < (pos + 1) * po(p); k++) {
    miss[k]--;
  }
  int ret = search(p - 1, pos * 2) + search(p - 1, pos * 2 + 1) + 1;
  for (int k = pos * po(p); k < (pos + 1) * po(p); k++) {
    miss[k]++;
  }
  ret = min(ret, search(p - 1, pos * 2) + search(p - 1, pos * 2 + 1));
  return ret;
}

static int solve(int p)
{
  for (int i = 0 ;i < po(p); i++)
    miss[i] = p;
  return search(p, 0);
}


int main()
{

  int T;
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  scanf("%d", &T);

  for (int i = 1; i <= T; i++) {
    int p;

    scanf("%d", &p);

    for (int k = 0 ; k < po(p); k++) {
      scanf("%d", &m[k]);
    }
    for (int l = 0; l < p; l++)
      for (int k = 0; k < po(p - l - 1); k++) 
        scanf("%d", &pr[l][k]);
    printf ("Case #%d: %d\n", i, solve(p));
  }
  return 0;
}