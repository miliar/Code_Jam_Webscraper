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

typedef long long ll;
ll mod=100003;

ll bc[555][555];
ll cc[555][555];

ll bi(int n, int k)
{
  if (n < k) return 0;
  if (n == k) return 1;
  if (bc[n][k] != -1) return bc[n][k];
  return bc[n][k]=(bi(n - 1, k) + bi(n - 1, k - 1)) % mod;
}

ll cnt(int n, int k)
{
  if (k == 1)return 1;
  if (n == 1 || n - 1 < k) return 0;
  if (cc[n][k] != -1)return cc[n][k];
  cc[n][k]=0;
  for (int i=1; i < k; i++)
  {
    cc[n][k]=(cc[n][k] + bi(n - k - 1, k - i - 1) * cnt(k, i)) % mod;
  }
  return cc[n][k];
}

int main()
{
  freopen("C.in", "r", stdin);
  freopen("C0.op", "w", stdout);
  int t;
  memset(bc, -1, sizeof (bc));
  memset(cc, -1, sizeof (cc));
  scanf("%d", &t);
  for (int cs=1; cs <= t; cs++)
  {
    ll sln=0;
    int n;
    scanf("%d",&n);
    for (int k=1; k < n ; k++)
    {
      sln+=cnt(n, k);sln%=mod;
    }

    printf("Case #%d: %lld\n", cs, sln);
  }

  return (0);
}

