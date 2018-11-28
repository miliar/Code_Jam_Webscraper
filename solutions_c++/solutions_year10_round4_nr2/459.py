/*
 * File:   main.cpp
 * Author: tanaeem
 *
 * Created on June 5, 2010, 8:47 PM
 */
#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <string.h>
#include <map>
#include <algorithm>
#include <vector>
using namespace std;
typedef long long ll;
int P[11][1111];
int M[11][1111];
int cs;
int vis[11][11][1111];
ll cache[11][11][1111];
ll opt(int p, int m, int ps)
{
  if(vis[p][m][ps]==cs)
    return cache[p][m][ps];
  vis[p][m][ps]=cs;
  if(p==0)return cache[p][m][ps]=0;
  cache[p][m][ps]=P[p][ps]+opt(p-1,m,2*ps)+opt(p-1,m,2*ps+1);
  if(m<M[p][ps])
  {
    ll tmp=opt(p-1,m+1,2*ps)+opt(p-1,m+1,2*ps+1);
    cache[p][m][ps]=min(cache[p][m][ps],tmp);
  }
  return cache[p][m][ps];
}
int main()
{
  freopen("B.in", "r", stdin);
  freopen("B2.op", "w", stdout);
  int t;
  scanf("%d", &t);
  for (cs=1; cs <= t; cs++)
  {
    ll sln=0;int p;
    scanf("%d",&p);
    for (int j=0; j < (1<<p); j++)
    {
      scanf("%d",&M[0][j]);
    }

    for (int i=1; i <= p; i++)
    {
      for (int j=0; j < 1<<(p-i); j++)
      {
        scanf("%d",&P[i][j]);
        M[i][j]=min(M[i-1][2*j],M[i-1][2*j+1]);
      }
    }
    sln=opt(p,0,0);

    printf("Case #%d: %lld\n", cs, sln);
  }

  return (0);
}

