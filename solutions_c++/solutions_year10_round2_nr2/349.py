/*
 * File:   main.cpp
 * Author: tanaeem
 *
 * Created on May 22, 2010, 10:33 PM
 */

#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <string.h>
#include <map>
using namespace std;
int x[110], v[110];

int main()
{
  freopen("B.in", "r", stdin);
  freopen("B1.op", "w", stdout);
  int t;
  scanf("%d", &t);
  for (int cs=1; cs <= t; cs++)
  {
    int n, k, b, T;
    scanf("%d%d%d%d", &n, &k, &b, &T);

    for (int i=0; i < n; i++)
    {
      scanf("%d", &x[i]);
    }

    for (int i=0; i < n; i++)
    {
      scanf("%d", &v[i]);
    }
    int ot=0, ac=0;
    int sln=0;
    for (int i=n - 1; i >= 0 && ac < k; --i)
    {
      if (T * v[i] + x[i] < b)
      {
        ot++;
      } else
      {
        ac++;
        sln+=ot;
      }
    }
    if (ac == k)
      printf("Case #%d: %d\n", cs, sln);
    else
      printf("Case #%d: IMPOSSIBLE\n", cs);
  }

  return (0);
}

